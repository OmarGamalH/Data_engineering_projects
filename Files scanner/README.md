#  File Scanner and Database Logger

This Python project scans a directory and logs file information (name and size) into a local SQLite database. It allows users to filter files based on count or size and view the results sorted by size and name.

---

##  Features

- Recursively scan all files in a given directory.
- Filter options:
  1. Limit results to **no more than 20 files**.
  2. Include only files **larger than a user-defined size** (in MB).
  3. Default option: **include all files**.
- Save the file name and size into a **SQLite database**.
- View the scanned files sorted by **size (descending)** and **name (ascending)**.

---

##  Getting Started

###  Requirements

- Python 3.x
- `pandas` (installed but not used in the current version)
- No external dependencies beyond Python standard libraries

###  Installation

Clone or download this repository to your local machine.

---

##  Usage

###  Command

```bash
python Project.py <directory_path>
