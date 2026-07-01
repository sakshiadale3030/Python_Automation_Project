import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

# =============================================================================
# Function Name : GetHash()
# Description   : Generates the SHA-256 hash value of a given file.
#                 This hash is used to identify duplicate files.
#
# Parameters    : path (str)
#                 -> Complete path of the file.
#
# Returns       : str
#                 -> SHA-256 hash value of the file.
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def GetHash(path):
    hashobj = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hashobj.update(data)

    return hashobj.hexdigest()

# =============================================================================
# Function Name : DeleteDuplicateFiles()
# Description   : Scans the specified directory recursively, identifies
#                 duplicate files using SHA-256 hashing, and deletes
#                 duplicate copies.
#
# Parameters    : directory (str)
#                 -> Directory path to scan.
#
# Returns       : int
#                 -> Total number of duplicate files deleted.
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def DeleteDuplicateFiles(directory):

    HashTable = {}

    DuplicateCount = 0

    for FolderName, SubFolder, FileNames in os.walk(directory):

        for fname in FileNames:

            FilePath = os.path.join(FolderName, fname)

            try:

                FileHash = GetHash(FilePath)

                if FileHash in HashTable:

                    print("Duplicate File Found :", FilePath)

                    os.remove(FilePath)

                    DuplicateCount += 1

                else:

                    HashTable[FileHash] = FilePath

            except Exception as e:

                print("Unable to process :", FilePath)

                print("Error :", e)

    print("Total Duplicate Files Deleted :", DuplicateCount)

    return DuplicateCount

# =============================================================================
# Function Name : DeleteTemporaryFiles()
# Description   : Deletes temporary files having predefined extensions
#                 such as .tmp, .temp, .bak, .log and .cache.
#
# Parameters    : DirName (str)
#                 -> Directory path to scan.
#
# Returns       : int
#                 -> Total number of temporary files deleted.
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def DeleteTemporaryFiles(DirName):

    temp_extensions = (
        ".tmp",
        ".temp",
        ".bak",
        ".log",
        ".cache"
    )

    TempCount = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):

        for fname in FileNames:

            FilePath = os.path.join(FolderName, fname)

            if FilePath.lower().endswith(temp_extensions):

                os.remove(FilePath)

                TempCount += 1

                print("Temporary file deleted :", FilePath)

    return TempCount

# =============================================================================
# Function Name : SendMail()
# Description   : Sends the generated log file as an email attachment
#                 using Gmail SMTP server.
#
# Parameters    : LogFilename (str)
#                 -> Path of the log file to be attached.
#
# Returns       : None
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def SendMail(LogFilename):

    sender = "sakshiadale3030@gmail.com"
    password = "xxxx xxxx xxxx xxxx"

    receiver = "sakshiadale30@gmail.com"

    msg = EmailMessage()

    msg["Subject"] = "Directory Automation Report"

    msg["From"] = sender

    msg["To"] = receiver

    msg.set_content("Please find attached the latest directory scan report.")

    with open(LogFilename, "rb") as f:
        data = f.read()

    msg.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename=LogFilename
    )

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)

# =============================================================================
# Function Name : DirectoryScanner()
# Description   : Performs complete directory automation by scanning the
#                 directory, deleting empty files, removing temporary files,
#                 deleting duplicate files, generating a log report,
#                 and sending the report via email.
#
# Parameters    : DirName (str)
#                 -> Directory to be scanned.
#
# Returns       : None
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def DirectoryScanner(DirName = "ScanFolder"):
    Border = "-"*52
    timestamp = time.ctime()

    # Create Logs directory if it does not exist
    LogDirectory = "Logs"

    if not os.path.exists(LogDirectory):
        os.mkdir(LogDirectory)

    LogFilename = "ScanFolder_" + timestamp
    LogFilename = LogFilename.replace(" ", "_")
    LogFilename = LogFilename.replace(":", "_")
    LogFilename += ".log"

    LogPath = os.path.join(LogDirectory, LogFilename)

    fobj = open(LogPath, "w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Directory Automation Tool\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write("This log file is created as : "+timestamp+"\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)  

            if(os.path.getsize(fname) == 0):                 # Empty File
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    # Call Temporary File Cleaner
    TempDeleted = DeleteTemporaryFiles(DirName)

        # Call Duplicate File Cleaner
    DuplicateDeleted = DeleteDuplicateFiles(DirName)            
 
    fobj.write("Total files scaned : "+str(FileCount)+"\n")
    fobj.write("Total empty file Count : "+str(EmptyFileCount)+"\n") 
    fobj.write("Temporary Files Deleted       : " + str(TempDeleted) + "\n")
    fobj.write("Duplicate Files Deleted       : " + str(DuplicateDeleted) + "\n")
    fobj.write(Border+"\n") 

    print("Directory Scan Completed Successfully.")
    print("Log File :", LogPath)

    fobj.close()

    try:
        SendMail(LogPath)
        print("Email sent successfully.")
    except Exception as e:
        print("Unable to send email.")
        print(e)   

# =============================================================================
# Function Name : main()
# Description   : Entry point of the application.
#                 Validates command-line arguments, schedules the directory
#                 scanning process, and continuously executes scheduled jobs.
#
# Parameters    : None
#
# Returns       : None
#
# Author        : Sakshi Ashok Adale
# Date          : 01/02/2026
# =============================================================================

def main():
    Border = "-"*52
    print(Border)
    print("----------Directory Automation Tool-----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return
    
    schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("----------Directory Automation Tool-----------")
    print(Border)
    
if __name__ == "__main__":
    main()    
