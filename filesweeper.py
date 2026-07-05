#!/usr/bin/env python3
import os
import shutil
import argparse
from pathlib import Path

# ============================================
# CATEGORIES (17 detailed types)
# ============================================
CATEGORIES = {
    "Images (Raster)": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif", ".psd", ".xcf", ".raw", ".cr2", ".nef", ".heic", ".heif", ".ico", ".tga", ".exr"],
    "Images (Vector & CAD)": [".svg", ".ai", ".eps", ".cdr", ".dwg", ".dxf", ".dgn"],
    "3D Models": [".obj", ".fbx", ".dae", ".3ds", ".blend", ".gltf", ".glb", ".max", ".ply", ".stl", ".step", ".stp"],
    "Documents & E-books": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".tex", ".wpd", ".md", ".pages", ".epub", ".mobi", ".azw3", ".djvu", ".xps"],
    "Spreadsheets": [".xlsx", ".xls", ".ods", ".csv", ".tsv", ".numbers", ".xlsm", ".xlsb"],
    "Presentations": [".pptx", ".ppt", ".odp", ".key", ".pps", ".ppsx", ".sldx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".ts", ".vob", ".rm", ".swf", ".ogv"],
    "Music & Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".alac", ".aiff", ".mid", ".midi", ".amr", ".opus", ".pcm"],
    "Archives & Compression": [".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".lz", ".cab", ".sit", ".sitx"],
    "Executables & Installers": [".exe", ".msi", ".bat", ".cmd", ".app", ".dmg", ".bin", ".elf", ".deb", ".rpm", ".pkg", ".apk", ".appimage", ".run"],
    "System & Libraries": [".sys", ".dll", ".so", ".drv", ".ini", ".cfg", ".plist", ".vbs"],
    "Code & Scripts": [".py", ".js", ".ts", ".html", ".htm", ".css", ".scss", ".less", ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".go", ".rs", ".php", ".rb", ".swift", ".kt", ".sh", ".pl", ".lua", ".dart", ".vb", ".asm"],
    "Data & Configuration": [".json", ".xml", ".yaml", ".yml", ".toml", ".env", ".graphql", ".ini"],
    "Databases": [".db", ".sqlite", ".sqlite3", ".mdf", ".ldf", ".sql", ".mdb", ".accdb", ".dbf"],
    "Disk Images & VMs": [".iso", ".img", ".vmdk", ".vdi", ".qcow2", ".vhd", ".vhdx", ".toast", ".cue"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".fnt", ".fon", ".eot"]
}

def get_category(filename):
    """Return the category for a given filename based on its extension."""
    ext = Path(filename).suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_folder(folder_path, dry_run=True):
    """
    Organize files in the given folder into subfolders by category.
    dry_run: If True, only print what would be moved, don't actually move.
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"❌ Error: Folder '{folder_path}' does not exist.")
        return
    
    if not folder.is_dir():
        print(f"❌ Error: '{folder_path}' is not a folder.")
        return
    
    print(f"📂 Scanning: {folder_path}")
    print(f"🧪 Dry-run mode: {'ON' if dry_run else 'OFF'}\n")
    
    moved_count = 0
    skipped_count = 0
    
    # Loop through all items in the folder
    for item in folder.iterdir():
        # Skip if it's a directory (we don't organize folders)
        if item.is_dir():
            skipped_count += 1
            continue
        
        # Get the category
        category = get_category(item.name)
        target_folder = folder / category
        
        # If dry-run, just print what would happen
        if dry_run:
            print(f"📄 Would move: {item.name} -> {category}/")
            moved_count += 1
        else:
            # Create the target folder if it doesn't exist
            target_folder.mkdir(exist_ok=True)
            
            # Move the file
            try:
                shutil.move(str(item), str(target_folder / item.name))
                print(f"✅ Moved: {item.name} -> {category}/")
                moved_count += 1
            except Exception as e:
                print(f"❌ Error moving {item.name}: {e}")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"📊 Summary:")
    print(f"   Files processed: {moved_count}")
    print(f"   Folders skipped: {skipped_count}")
    
    if dry_run:
        print(f"\n💡 This was a DRY RUN. No files were actually moved.")
        print(f"   Run with --execute to actually organize the files.")
    else:
        print(f"\n✅ Organization complete! Your folder is now clean.")

def main():
    parser = argparse.ArgumentParser(
        description="🧹 FileSweeper: Automatically organize messy folders.",
        epilog="Example: python filesweeper.py ~/Downloads --execute"
    )
    
    # Make the folder argument OPTIONAL (nargs="?")
    parser.add_argument(
        "folder",
        nargs="?",
        default=None,
        help="Path to the folder you want to organize. If omitted, defaults to your Pictures folder."
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually move the files (without this, it's a dry-run)"
    )
    
    args = parser.parse_args()
    
    
    if args.folder:
        folder_path = os.path.expanduser(args.folder)
    else:
        
        folder_path = str(Path.home() / "Pictures")
        print(f"📂 No folder specified. Defaulting to: {folder_path}\n")
    
    # Run the organizer
    organize_folder(
        folder_path=folder_path,
        dry_run=not args.execute
    )

if __name__ == "__main__":
    main()
