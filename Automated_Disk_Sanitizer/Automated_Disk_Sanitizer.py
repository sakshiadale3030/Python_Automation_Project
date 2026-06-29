###############################################################
# Project        : Automated Disk Sanitizer - Directory Automation Tool
# Description    : Identifies and deletes duplicate files in a directory
# Author         : Sakshi Ashok Adale
# Date           : 11/05/2026
###############################################################

import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

###############################################################
# Function Name  : CalculateChksum
# Description    : Calculates MD5 checksum of a given file
# Parameters     : path (str), BlockSize (int)
# Returns        : str (checksum)
###############################################################

def CalculateChksum(path,BlockSize = 1024):
 
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(BlockSize)

    while(len(Buffer) > 0):

        hobj.update(Buffer)
        Buffer = fobj.read(BlockSize)
    
    fobj.close()

    return hobj.hexdigest()

###############################################################
# Function Name  : SendMail
# Description    : send mail of log file automatically to registered mail
# Parameters     : DirectoryName (str)
# Returns        : dict (checksum -> list of files)
###############################################################
def SendMail(logFile):

    SenderMail = "sakshiadale30@gmail.com"
    SenderPass = "xyz xyz xyz xyz"
    reciverMail = "sakshiadale3030@gmail.com"
    MailServer = "smtp.gmail.com"
    port = 587
    logFilePath = logFile
    print(logFilePath)  

    try:
        msg = EmailMessage()

        msg["From"] = SenderMail
        msg["To"] = reciverMail
        msg["Subject"] = "Log File report"

        fobj = open(logFilePath,"rb")
        
        FileData = fobj.read()
        print("sixe: ",len(FileData))
        FileName = logFile.split("/")[-1]

        msg.add_attachment( 
            FileData,
            maintype = "application",
            subtype = "octet-stream",
            filename = FileName
        )

        Server = smtplib.SMTP(MailServer,port)

        Server.starttls()
        Server.login(SenderMail,SenderPass)
        Server.send_message(msg)
        Server.quit()
        fobj.close()

    except Exception as e:
        print("Exception : ",e)

###############################################################
# Function Name  : FindDuplicate
# Description    : Finds duplicate files based on checksum
# Parameters     : DirectoryName (str)
# Returns        : dict (checksum -> list of files)
###############################################################

def FindDuplicate(DirectoryName = "Marvellous"):

    Flag = os.path.isabs(DirectoryName)

    if(Flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    Flag = os.path.exists(DirectoryName)
    
    if(Flag == False):
        print("The path is invalid !!")
        exit()

    Flag = os.path.isdir(DirectoryName)

    if(Flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolders,FileNames in os.walk(DirectoryName):
        for fName in FileNames:
            fName = os.path.join(FolderName,fName)
            checkSum = CalculateChksum(fName)

            if checkSum in Duplicate:
                Duplicate[checkSum].append(fName)
            else:
                Duplicate[checkSum] = [fName]

    DeleteDuplicate(Duplicate)


###############################################################
# Function Name  : DeleteDuplicate
# Description    : Deletes duplicate files, keeping one copy
# Parameters     : Path (str)
# Returns        : None
###############################################################

def DeleteDuplicate(MyDic):

    result = list(filter(lambda x : len(x) > 1,MyDic.values()))
    
    timestam = time.ctime()

    # Creating file for log
    FileName = "DirCleanLog_%s.log" %(timestam)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")
    
    fobj = open(FileName,"w")

    Border = "-"*54
    fobj.write(Border+"\n")
    
    fobj.write("This is the log file of Marvellous Automation Script"+"\n")
    fobj.write("This is Directory Cleaner Script"+"\n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")
    fobj.write("\n")

    count = 0
    cnt = 0
    for value in result:
        for subvalue in value:
            count += 1
            if(count > 1):

                fobj.write("Deleted File : %s"%(subvalue)+"\n")
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                cnt += 1
        count = 0
    print("Total Deleted file : ",cnt) 

    fobj.write("\n")
    fobj.write(Border+"\n")
    
    fobj.write(Border+"\n")
    
    fobj.write("This is created at "+"\n")
    fobj.write(timestam+"\n")
    
    fobj.write(Border+"\n")  
    fobj.close()

    logPath = os.path.abspath(FileName)
    logPath = logPath.replace("\\","/")
    print(logPath)
    SendMail(logPath)

def main():

    Border = "-"*54
    print(Border)
    print("-------------Directory Automation--------------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform Directory Cleaning")
            print("This is the directory automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1]=="--U")):
            print("Use the given script as")
            print("ScriptName.py  NameOfDirectory")
            print("Plz provide valid Absolute path")
        
        else:
            schedule.every(1).minutes.do(lambda: FindDuplicate(sys.argv[1]))

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid Number of commandline Arguments")
        print("Use the given flag as")
        print("--h used to display help")
        print("--u used to display usage")

    print(Border)
    print("------------Thank you for using our script------------")
    print(Border)

if(__name__=="__main__"):
    main()                