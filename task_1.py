import shutil
import sys
from pathlib import Path


def copy_files_with_recursion(src, dest):
    try:
        src_path = Path(src)
        dest_path = Path(dest)
        dest_path.mkdir(parents=True, exist_ok=True)

        for item in src_path.iterdir():
            if item.is_dir():
                copy_files_with_recursion(item, dest)
            elif item.is_file():
                file_extention = item.suffix.lower()
                target_dir = dest_path / (
                    file_extention[1:] if file_extention else "no_extention"
                )
                target_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_dir)
                print(f"Copied: {item} to {target_dir}")
    except PermissionError:
        print(f"Permission denied: {src}")
    except FileNotFoundError:
        print(f"File or directory not found: {src}")
    except Exception as e:
        print(f"Error processing {src}:{e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_dir> [destination_dir]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not Path(src_dir).exists() or not Path(src_dir).is_dir():
        print(f"Directory does not exist or invalid: {src_dir}")
        sys.exit(1)

    copy_files_with_recursion(src_dir, dest_dir)
    print(f"Files have been copied and sorted into {dest_dir}.")


if __name__ == "__main__":
    main()
