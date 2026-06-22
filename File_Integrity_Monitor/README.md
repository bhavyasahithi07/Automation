# File Integrity Monitor

A Python CLI tool that detects unauthorized file changes using SHA-256 hashing. Inspired by real-world tools like Tripwire, it creates a baseline snapshot of a directory and flags any files that are added, modified, or deleted on later scans.

## How It Works

1. **Create a baseline** - the tool scans a target folder and generates a SHA-256 hash for every file, saving the result to `baseline.json`.
2. **Run an integrity check** - the tool re-scans the same folder and compares current hashes against the baseline.
3. **Get a report** - any new, modified, or deleted files are flagged, printed to the terminal, and saved to `fim_report.txt`.

Even a single character change in a file produces a completely different SHA-256 hash, which makes this approach reliable for detecting tampering.

## Project Structure

The project is split into modular files, each with a single responsibility:
File_Integrity_Monitor/
├── main.py       # CLI menu and entry point
├── hasher.py     # SHA-256 hashing logic
├── baseline.py   # Save and load baseline.json
├── checker.py    # Compare current state vs baseline
└── reporter.py   # Terminal output and .txt report generation

| File | Responsibility |
| `hasher.py` | Hashes individual files and scans directories |
| `baseline.py` | Persists and loads the baseline snapshot |
| `checker.py` | Detects new, modified, and deleted files |
| `reporter.py` | Formats and outputs the scan report |
| `main.py` | Ties everything together via a CLI menu |

## Getting Started

### Requirements

- Python 3.x (no external dependencies — uses only the standard library)

### Running the tool

```bash
git clone https://github.com/bhavyasahithi07/Automation.git
cd Automation/File_Integrity_Monitor
python Main.py
```

### Menu Options
1. Create baseline snapshot
2. Check integrity (compare now)
3. View baseline info
4. Exit

1. Choose **1** and enter the path of the folder you want to monitor. This generates `baseline.json`.
2. Modify, add, or delete a file in that folder.
3. Choose **2** to run a check. Any changes will be flagged in the terminal and saved to `fim_report.txt`.
4. Choose **3** anytime to view what's currently tracked in the baseline.

## Example Output

```
[NEW FILES] - 1 found
  + notes.txt

[MODIFIED FILES] - 1 found
  ~ config.py

[DELETED FILES] - 0 found

SUMMARY: 2 ISSUE(S) DETECTED - Review findings above.
```

## What This Project Demonstrates

- Practical use of cryptographic hashing (SHA-256) for tamper detection
- Core file integrity monitoring concepts used in real security tools

## Background

Built as a hands-on project after completing the Google Cybersecurity Professional Certificate, to apply core concepts like asset monitoring and change detection in a real, working tool.
