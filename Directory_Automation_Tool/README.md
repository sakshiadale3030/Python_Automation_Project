# 📂 Directory Automation Tool

A Python-based automation tool that periodically scans a specified directory and performs intelligent file management tasks. The application automatically removes empty files, deletes duplicate files using SHA-256 hashing, removes temporary files, generates log reports, and sends the reports via email.

---

## 🚀 Features

- Scan a directory automatically at scheduled intervals
- Delete empty files
- Detect and remove duplicate files using SHA-256 hashing
- Delete temporary files (.tmp, .temp, .bak, .log, .cache)
- Generate detailed log reports
- Store log reports inside a dedicated **Logs** folder
- Send log reports automatically via Gmail
- Cross-platform support (Windows, Linux, macOS)

---

## 📁 Project Structure

```
DirectoryAutomationTool/
│
├── DirectoryAutomation_Final.py
├── requirements.txt
├── README.md
│
├── Logs/
│   ├── ScanFolder_Mon_Jul_01_12_30_05_2026.log
│   ├── ScanFolder_Mon_Jul_01_12_31_05_2026.log
│   └── ...
│
└── ScanFolder/
    ├── file1.txt
    ├── file2.tmp
    ├── duplicate.pdf
    └── ...
```

---

## ⚙️ Technologies Used

- Python 3
- os
- sys
- hashlib
- schedule
- smtplib
- email.message

---

## 📌 Functionalities

### 1. Directory Scanning

- Scans the specified directory recursively.
- Counts total files.
- Removes empty files.

---

### 2. Duplicate File Detection

- Generates SHA-256 hash for every file.
- Identifies duplicate files.
- Deletes duplicate copies automatically.

---

### 3. Temporary File Cleaner

Automatically deletes files having extensions:

- `.tmp`
- `.temp`
- `.bak`
- `.log`
- `.cache`

---

### 4. Log Generation

Creates timestamp-based log files containing:

- Total files scanned
- Empty files deleted
- Temporary files deleted
- Duplicate files deleted

Example:

```
Logs/
ScanFolder_Mon_Jul_01_12_30_05_2026.log
```

---

### 5. Email Notification

After every successful scan, the generated log file is automatically sent as an email attachment.

Uses:

- Gmail SMTP
- SSL Connection
- App Password Authentication

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DirectoryAutomationTool.git
```

Move into project directory

```bash
cd DirectoryAutomationTool
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script

```bash
python DirectoryAutomation_Final.py ScanFolder
```

where

```
ScanFolder
```

is the directory you want to monitor.

---

## 📧 Email Configuration

Update these values inside the code:

```python
sender = "your_email@gmail.com"

password = "your_gmail_app_password"

receiver = "receiver_email@gmail.com"
```

> Enable **2-Step Verification** on your Gmail account and generate an **App Password**.

---

## 📄 Sample Log

```
----------------------------------------------------
This is a log file created by Directory Automation Tool

This is a Directory Cleaner Script

Total Files Scanned : 25

Empty Files Deleted : 3

Temporary Files Deleted : 5

Duplicate Files Deleted : 2

----------------------------------------------------
```

---

## 📌 Future Enhancements

- GUI using Tkinter or PyQt
- Real-time directory monitoring using Watchdog
- File backup before deletion
- PDF log report generation
- ZIP compression of logs
- Cloud backup support
- Database logging
- Multi-directory monitoring
- Command-line options
- Configuration file support

---

## 👩‍💻 Author

**Sakshi Adale**

Date - **02/07/2026**