"""Safely organize files in a folder. Run: python organizer.py"""
import shutil
from pathlib import Path

CATEGORIES = {
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".txt": "Documents", ".rtf": "Documents", ".odt": "Documents",
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".bmp": "Images", ".svg": "Images", ".webp": "Images",
    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos",
    ".avi": "Videos", ".webm": "Videos",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
    ".py": "Code", ".js": "Code", ".html": "Code", ".css": "Code",
    ".java": "Code", ".c": "Code", ".cpp": "Code", ".json": "Code",
}

def unique_destination(destination):
    """Return a non-existing destination path if a filename already exists."""
    if not destination.exists():
        return destination
    parent, stem, suffix = destination.parent, destination.stem, destination.suffix
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1

def organize_folder(folder_path, dry_run=False):
    folder = Path(folder_path).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        raise ValueError("The path does not exist or is not a directory.")

    moved, skipped, errors = [], [], []
    # Only inspect files directly inside the selected folder; don't reorganize subfolders.
    try:
        entries = list(folder.iterdir())
    except PermissionError as exc:
        raise PermissionError(f"Cannot access folder: {exc}") from exc

    for item in entries:
        if not item.is_file():
            continue
        category = CATEGORIES.get(item.suffix.lower())
        if category is None:
            skipped.append(item.name)
            continue
        target_folder = folder / category
        destination = unique_destination(target_folder / item.name)
        if dry_run:
            moved.append((item.name, str(destination.relative_to(folder))))
            continue
        try:
            target_folder.mkdir(exist_ok=True)
            destination = unique_destination(target_folder / item.name)
            shutil.move(str(item), str(destination))
            moved.append((item.name, str(destination.relative_to(folder))))
        except (PermissionError, OSError, shutil.Error) as exc:
            errors.append((item.name, str(exc)))

    return moved, skipped, errors

def main():
    print("=== FILE ORGANIZER ===")
    raw = input("Folder path to organize (or 'q' to quit): ").strip().strip('"')
    if raw.lower() == "q":
        print("Cancelled.")
        return
    confirm = input("Preview only first? (y/n, recommended y): ").strip().lower()
    dry_run = confirm != "n"
    try:
        moved, skipped, errors = organize_folder(raw, dry_run=dry_run)
    except (ValueError, PermissionError) as exc:
        print("Error:", exc)
        return
    print("\n=== SUMMARY ===")
    print("Mode:", "PREVIEW - no files moved" if dry_run else "LIVE - files moved")
    print("Files to relocate / relocated:", len(moved))
    for old, new in moved:
        print(f"  {old} -> {new}")
    print("Unsupported extensions skipped:", len(skipped))
    if skipped:
        print("  " + ", ".join(skipped))
    print("Errors:", len(errors))
    for name, error in errors:
        print(f"  {name}: {error}")
    if dry_run:
        print("\nRun again and answer 'n' to perform the move.")

if __name__ == "__main__":
    main()
