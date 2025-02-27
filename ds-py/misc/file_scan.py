import os
import sys
import datetime

def build_dst_file_index(dst_folder):
    file_index = {}
    for root, _, files in os.walk(dst_folder):
        for file in files:
            try:
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath):  # Check if it's a regular file
                    file_size = os.path.getsize(filepath)
                    file_index[(file, file_size)] = filepath
            except OSError:
                pass  # Ignore files that can't be accessed
    return file_index

def count_files_in_folder(folder):
    total_files = 0
    for _, _, files in os.walk(folder):
        total_files += len(files)
    return total_files

def find_files_and_log(src_folder, file_index, log_file_name):
    total_files_checked = 0
    total_files_found = 0
    src_file_count = count_files_in_folder(src_folder)

    with open(log_file_name, 'w') as log_file:
        for src_dir, _, src_files in os.walk(src_folder):
            for src_file_name in src_files:
                src_file_path = os.path.join(src_dir, src_file_name)
                if not os.path.isfile(src_file_path):
                    continue  # Skip if not a regular file

                try:
                    src_file_size = os.path.getsize(src_file_path)
                    src_file_stat = os.stat(src_file_path)
                    src_file_mtime = datetime.datetime.fromtimestamp(src_file_stat.st_mtime)
                except OSError as e:
                    print(f"Error accessing file '{src_file_path}': {e}")
                    continue

                total_files_checked += 1
                print(f"Files in `src`: {src_file_count}, checked: {total_files_checked}, found in `dst`: {total_files_found}", end='\r')

                if (src_file_name, src_file_size) in file_index:
                    total_files_found += 1
                    log_file.write(f"{src_file_mtime.strftime('%Y-%m-%d %H:%M:%S')} - {src_file_size} - {src_file_name}\n")

    print()  # Ensure the next print statement is on a new line
    return total_files_checked, total_files_found

def main(src_folder, dst_folder):
    if not os.path.exists(src_folder) or not os.path.exists(dst_folder):
        print("Error: Source or destination folder does not exist or cannot be accessed.")
        return

    print(f"Building file index for `dst` folder {dst_folder}...")
    dst_file_index = build_dst_file_index(dst_folder)
    print(f"Total files in `dst`: {len(dst_file_index)}")

    print(f"Starting scanning `src` folder {src_folder}...")
    total_files_checked, total_files_found = find_files_and_log(src_folder, dst_file_index, "files.log")
    print(f"Total files in `src`: {total_files_checked}, files found in `dst`: {total_files_found}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <src_folder> <dst_folder>")
        sys.exit(1)

    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]
    main(src_folder, dst_folder)