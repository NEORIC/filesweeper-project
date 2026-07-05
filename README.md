# 🧹 FileSweeper

**Automatically organize your messy folders into 17 neat categories.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

---

## 📖 The Problem

Your **Downloads** folder is a disaster. Your **Desktop** is covered in screenshots, PDFs, installers, and random ZIP files. You can never find anything, and you keep scrolling through hundreds of files.

## 💡 The Solution

**One command**, and everything gets sorted into neat folders:

- `Images (Raster)/` – JPG, PNG, GIF, WebP, RAW, PSD, etc.
- `Images (Vector & CAD)/` – SVG, AI, EPS, DWG, DXF, etc.
- `3D Models/` – OBJ, FBX, BLEND, STL, STEP, etc.
- `Documents & E-books/` – PDF, DOCX, TXT, EPUB, MOBI, etc.
- `Spreadsheets/` – XLSX, CSV, ODS, etc.
- `Presentations/` – PPTX, ODP, KEY, etc.
- `Videos/` – MP4, MKV, AVI, MOV, etc.
- `Music & Audio/` – MP3, WAV, FLAC, AAC, etc.
- `Archives & Compression/` – ZIP, RAR, 7Z, TAR, etc.
- `Executables & Installers/` – EXE, MSI, DMG, APK, etc.
- `Code & Scripts/` – Python, JS, HTML, CSS, C++, Java, etc.
- `Databases/` – SQLite, SQL, MDB, etc.
- `Fonts/` – TTF, OTF, WOFF, etc.
- ...and **17 categories total!**

---

## 🚀 Quick Start

### Windows Users (EXE)
1. Download `filesweeper.exe` from the [Releases](https://github.com/NEORIC/filesweeper-project/releases) page.
2. Open **Command Prompt** or **PowerShell**.
3. Navigate to the folder where you saved the EXE.
4. Run:

```cmd
# Dry run (safe - shows what will happen)
filesweeper.exe

# Organize your Downloads folder
filesweeper.exe "C:\Users\YourName\Downloads" --execute

# Organize to a custom destination
filesweeper.exe "C:\Users\YourName\Downloads" --destination "D:\SortedFiles" --execute
