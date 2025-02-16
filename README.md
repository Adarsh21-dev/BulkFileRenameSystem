# 📝 BULK FILE RENAME SYSTEM

## 🔰 Introduction
The **Bulk File Rename System** is a powerful and user-friendly tool designed to rename multiple files efficiently. Whether you need to add prefixes, suffixes, remove characters, or change file extensions in bulk, this software provides an intuitive interface to get the job done quickly and accurately.

## ✨ Features
- 🔄 **Batch Renaming**: Rename multiple files at once with a few clicks.
- 🏷️ **Custom Modifications**: Add or remove text at the beginning or end of filenames.
- 📂 **Extension Modification**: Easily change file extensions.
- 🔍 **Search and Filter**: Find specific files before renaming.
- 🖥️ **Graphical Interface**: Simple and easy-to-use UI with clear instructions.
- ⚙️ **Dynamic UI Handling**: If `bulkgui.ui` is available, it loads dynamically; otherwise, it falls back to `bulkqtUi.py`.
- ❌ **Error Handling**: Displays appropriate messages when files or operations are invalid.

## 📸 Screenshots
Below are some screenshots of the application in action:

*(Add relevant screenshots here)*

## 📁 Files and Their Requirements
### 1. `main.py`
- **📝 Purpose**: The main entry point of the application.
- **📌 Requirements**:
  - Dynamically loads the UI from `bulkgui.ui` if available.
  - Falls back to `bulkqtUi.py` if `bulkgui.ui` is missing.
  - Implements file renaming logic, UI event handling, and directory selection.
  - Uses PyQt5 modules (`QMainWindow`, `QFileDialog`, `QMessageBox`, etc.).

### 2. `bulkgui.ui`
- **🎨 Purpose**: UI file created using Qt Designer, providing the visual layout of the application.
- **📌 Requirements**:
  - Should be in the same directory as `main.py` to be auto-loaded.
  - Can be edited using Qt Designer if layout modifications are needed.

### 3. `bulkqtUi.py`
- **💻 Purpose**: Python-converted version of `bulkgui.ui`, acting as a backup UI.
- **📌 Requirements**:
  - Contains the `Ui_MainWindow` class, defining the UI elements.
  - Used when `bulkgui.ui` is missing.
  - Must be updated if `bulkgui.ui` undergoes significant changes.

## ⚙️ Installation and Running the Application
### 1. 📥 Install dependencies:
```sh
pip install PyQt5
```
### 2. 🎨 Install Qt5 Designer (optional but recommended for UI modifications):
```sh
pip install pyqt5-tools
```
### 3. ▶️ Run the application:
```sh
python main.py
```

### 4. 🛠️ Running Qt Designer (optional for UI modifications):
```sh
pyqt5-tools designer
```
*If this doesn't work, ensure your Python scripts folder is in your system PATH.*

## 🔧 How It Works
The application provides two main panels:
1. 📂 **Side Selection** - Choose the files you want to rename.
2. 🗑️ **Side Remove** - Select unwanted files for exclusion.

At the bottom, users can apply specific renaming operations:
- ➕ **Add First / Add Last**: Insert text at the beginning or end of filenames.
- ➖ **Remove First / Remove Last**: Delete a set number of characters from filenames.
- 🔄 **Add New Name**: Completely rename files with a new naming scheme.
- ✅ **Apply Changes**: Execute the selected renaming operation.

## 🚀 Future Development & Scope
- 🖱️ **Drag & Drop Support**: Allow users to drag files directly into the application.
- 🔄 **Undo Feature**: Implement a rollback mechanism for rename actions.
- 👀 **Preview Changes**: Display how filenames will change before applying them.
- 🔠 **Custom Naming Patterns**: Allow users to create advanced renaming templates.
- 🌍 **Multilingual Support**: UI localization in multiple languages.
- 🖥️ **Cross-Platform Compatibility**: Enhance support for Linux and macOS.

## 🖥️ Hardware Requirements
### 📌 Minimum Requirements:
- **💻 Processor**: Intel Core i3 / AMD Ryzen 3 (or equivalent)
- **🛠️ RAM**: 2GB
- **💾 Storage**: 200MB free space
- **🖥️ OS**: Windows 7/8/10/11, Linux, macOS

### 📌 Recommended Requirements:
- **🚀 Processor**: Intel Core i5/i7 / AMD Ryzen 5/7 (or equivalent)
- **⚡ RAM**: 4GB or higher
- **💽 Storage**: 500MB free space
- **🖥️ OS**: Windows 10/11, Latest Linux distributions, macOS

## ❗ Error Handling
- ⚠️ If neither `bulkgui.ui` nor `bulkqtUi.py` is found, the application displays an error message and exits.
- 🚫 If an invalid rename operation is attempted, an appropriate warning is shown.
- 🔄 If Qt Designer UI is modified, update `bulkqtUi.py` using:
```sh
pyuic5 bulkgui.ui -o bulkqtUi.py
```

## 📥 Download Standalone EXE
For users who do not want to install Python, the application is available as a **standalone .exe file**.

[⬇️ Download Bulk File Rename System](https://github.com/Adarsh21-dev/Bulk-File-Rename-Exe_Release.git)

## 🤔 Why Use This Tool?
- ⏳ Saves time when renaming large numbers of files.
- 🏆 Eliminates manual effort and potential errors.
- 🔍 Provides an organized and structured renaming process.

This software is particularly useful for professionals, content creators, developers, and anyone who regularly manages bulk files.

---

For further details on `.exe` generation, refer to the **[Standalone `.exe` Guide](PyInstaller_Guide.md)**.

For further details on regex usage, refer to the **Regex Patterns Guide**.
