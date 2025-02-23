import os
import shutil
from pathlib import Path


def move_pdf_files(source_dir, destination_dir):

    source_path = Path(source_dir)
    dest_path = Path(destination_dir)

    # Create destination if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    moved_count = 0
    error_count = 0

    for root, _, files in os.walk(source_path):
        for file in files:
            if file.lower().endswith('.csv'):
                source_file = Path(root) / file
                dest_file = dest_path / file

                # duplicate
                counter = 1
                while dest_file.exists():
                    base_name = dest_file.stem
                    dest_file = dest_path / f"{base_name}_{counter}{dest_file.suffix}"
                    counter += 1

                try:
                    shutil.move(source_file, dest_file)
                    print(f"Moved: {source_file} -> {dest_file}")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {source_file}: {str(e)}")
                    error_count += 1

    return moved_count, error_count


if __name__ == "__main__":
    
    source_directory = "/Where/files/are"
    destination_directory = "/Where/files/are/being/banished/to"

    moved, errors = move_pdf_files(source_directory, destination_directory)
    print(f"\nOperation completed:")
    print(f"Files moved: {moved}")
    print(f"Errors encountered: {errors}")
