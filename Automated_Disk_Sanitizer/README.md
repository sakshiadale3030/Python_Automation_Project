# Automated Disk Sanitizer - Directory Automation Tool

## Project Overview

**Automated Disk Sanitizer** is a Python automation project that scans a specified directory, identifies duplicate files using the **MD5 checksum algorithm**, deletes the duplicate copies while keeping one original file, generates a log report of all deleted files, and automatically emails the log file to a registered email address.

The project is designed to automate disk cleaning and help users save storage space by removing unnecessary duplicate files.

---

# Features

* Scan any directory recursively.
* Detect duplicate files using MD5 checksum.
* Automatically delete duplicate files.
* Keep one original copy of each file.
* Generate a detailed log file.
* Automatically send the log file through Gmail.
* Schedule automatic directory scanning every minute.

---

# Technologies Used

* Python 3
* OS Module
* Hashlib
* Schedule
* SMTP (Email Automation)
* EmailMessage
* Time Module

---

# Project Structure

```
Automated_Disk_Sanitizer/
│
├── DirectoryAutomation.py
├── README.md
└── Log Files (Generated Automatically)
```

---

# Modules Used

| Module        | Purpose                       |
| ------------- | ----------------------------- |
| os            | File and directory operations |
| sys           | Command line arguments        |
| hashlib       | Generate MD5 checksum         |
| schedule      | Schedule automatic execution  |
| smtplib       | Send email                    |
| email.message | Email attachment handling     |
| time          | Timestamp generation          |

---

# Working Principle

1. User provides a directory path.
2. The program scans all files recursively.
3. An MD5 checksum is generated for every file.
4. Files having identical checksums are considered duplicates.
5. One copy is retained.
6. Remaining duplicate files are deleted.
7. A log file is created containing deleted file details.
8. The log file is emailed automatically.
9. The entire process repeats every one minute.

---

# Functions Description

### CalculateChksum()

Calculates the MD5 checksum of a file.

**Input**

* File Path

**Output**

* MD5 Hash String

---

### FindDuplicate()

Scans the given directory and identifies duplicate files.

---

### DeleteDuplicate()

Deletes duplicate files, generates a log report, and calls the email function.

---

### SendMail()

Sends the generated log file as an email attachment.

---

### main()

Handles command-line arguments and schedules the automation task.

---

# Command Line Usage

### Display Help

```bash
python DirectoryAutomation.py --h
```

### Display Usage

```bash
python DirectoryAutomation.py --u
```

### Scan a Directory

```bash
python DirectoryAutomation.py "C:\Users\Username\Documents"
```

Linux Example

```bash
python3 DirectoryAutomation.py /home/user/Documents
```

---

# Sample Output

```
------------------------------------------------------
-------------Directory Automation----------------------
------------------------------------------------------

Deleted file :
C:/Users/Admin/Desktop/Test/file2.txt

Deleted file :
C:/Users/Admin/Desktop/Test/file3.txt

Total Deleted File : 2

Log file created successfully.
Email sent successfully.
```

---

# Email Configuration

Update the following details in the `SendMail()` function:

```python
SenderMail = "your_email@gmail.com"
SenderPass = "Your App Password"
ReceiverMail = "receiver@gmail.com"
```

> **Note:** Use a Gmail **App Password** instead of your normal Gmail password.

---

# Advantages

* Saves disk storage automatically.
* Eliminates duplicate files.
* Fully automated execution.
* Generates deletion reports.
* Email notification after every execution.
* Easy to customize.

---

# Limitations

* Uses MD5 hashing (not suitable for cryptographic security).
* Requires Gmail SMTP configuration.
* Permanently deletes duplicate files.
* No recovery option after deletion.

---

# Future Enhancements

* GUI using Tkinter or PyQt.
* Restore deleted files from Recycle Bin.
* Support multiple hashing algorithms (SHA-256, SHA-512).
* Email multiple recipients.
* Cloud backup before deletion.
* Generate PDF reports.
* Logging database integration.
* User confirmation before deletion.

---

# Author

**Sakshi Ashok Adale**

Date: **29/06/2026**

---

# Conclusion

The **Automated Disk Sanitizer** successfully automates the process of identifying and removing duplicate files from a directory. By combining checksum-based duplicate detection, scheduled execution, automated logging, and email reporting, the project provides an efficient solution for maintaining storage hygiene with minimal user intervention.
