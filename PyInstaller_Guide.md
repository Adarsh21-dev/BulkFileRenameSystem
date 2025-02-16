# Guide to Creating a Standalone `.exe` File for Bulk File Rename System

## Overview
This guide explains how to convert the `Bulk File Rename System` Python application into a standalone `.exe` file using **PyInstaller**. The goal is to create a single executable file that does not require Python installation and is optimized for small size.

---

## Step 1: Install PyInstaller
To begin, install PyInstaller using `pip`:
```sh
pip install pyinstaller
```

---

## Step 2: Create the `.exe` File
Run the following command to generate a standalone executable:
```sh
pyinstaller --onefile --windowed --noconsole --icon=icon.ico --name=BulkFileRename main.py
```
### Explanation of Flags:
- **`--onefile`** → Generates a single `.exe` file.
- **`--windowed`** → Hides the console window.
- **`--noconsole`** → Ensures no terminal window pops up.
- **`--icon=icon.ico`** → Sets the application icon (optional).
- **`--name=BulkFileRename`** → Names the output file as `BulkFileRename.exe`.

> **Note:** If your application is CLI-based, remove `--windowed` to keep console output visible.

---

## Step 3: Reduce File Size with UPX Compression
PyInstaller generates a large `.exe` file by default. To reduce its size, use **UPX compression**:

1. Install UPX (optional but recommended):
   ```sh
   pip install upx
   ```
2. Generate a compressed `.exe`:
   ```sh
   pyinstaller --onefile --windowed --noconsole --icon=icon.ico --upx-dir=upx --name=BulkFileRename main.py
   ```

---

## Step 4: Locate the `.exe` File
Once PyInstaller completes, your standalone `.exe` file will be in the `dist/` folder. Rename it if needed and move it to your desired location.

---

## Troubleshooting
- **Error: Missing `pyuic5`?**
  ```sh
  pip install pyqt5-tools 
  ```

- **Error: `.exe` not running?** Ensure all required dependencies are included in `main.py`.
- **Need further optimizations?** Consider using **UPX** or manually excluding unused modules.

---

## Conclusion
Now you have a **lightweight, portable `.exe`** file that can run without Python installation. 🎉