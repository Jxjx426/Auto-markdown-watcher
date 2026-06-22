# Auto Markdown Watcher

Automatically monitor a folder and convert newly added files into Markdown using Microsoft's MarkItDown.

Perfect for AI workflows, RAG pipelines, note-taking systems, and document preprocessing.

---

## Features

* Automatically watches a folder for new files
* Converts supported documents to Markdown
* Generates `.md` files with the same filename
* Creates the watch folder automatically if it does not exist
* Zero-click workflow — just drop files into the folder

---

## Supported Formats

Any format supported by MarkItDown, including:

* PDF
* DOCX
* PPTX
* XLSX
* HTML
* TXT
* Images (with supported OCR configurations)

---

## Requirements

* Python 3.10 or newer
* Windows, macOS, or Linux

---

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/auto-markdown-watcher.git
cd auto-markdown-watcher
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install watchdog markitdown
```

---

## Usage

Run the watcher:

```bash
python watch_folder.py
```

The application will automatically create a folder called:

```text
Desktop/To_AI
```

if it does not already exist.

You should see:

```text
==================================================
 Watching folder: C:\Users\YourName\Desktop\To_AI
 Drop files here to convert them to Markdown automatically!
 Press Ctrl+C to stop.
==================================================
```

---

## How It Works

1. Start the watcher.
2. Open the `To_AI` folder on your Desktop.
3. Drag and drop a supported file into the folder.
4. The file is automatically converted.
5. A Markdown file with the same name will be created.

Example:

```text
To_AI/
├── lecture.pdf
└── lecture.md
```

---

## Custom Watch Directory

You can specify a custom folder using the `WATCH_DIR` environment variable.

### Windows (PowerShell)

```powershell
$env:WATCH_DIR="D:\Documents\AI_Files"
python watch_folder.py
```

### Linux / macOS

```bash
export WATCH_DIR="/home/user/AI_Files"
python watch_folder.py
```

---

## Project Structure

```text
Auto-markdown-watcher/
│
├── watch_folder.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Built With

* Microsoft MarkItDown
* Watchdog

