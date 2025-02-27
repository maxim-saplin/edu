import os
import sys
import statistics

def find_cpp_files(directory):
    cpp_files = [(root, file) for root, dirs, files in os.walk(directory) for file in files if file.endswith('')]
    return cpp_files

def file_sizes(cpp_files):
    sizes = [os.path.getsize(os.path.join(root, file)) for root, file in cpp_files]
    return sizes

def main(directory):
    cpp_files = find_cpp_files(directory)
    sizes = file_sizes(cpp_files)

    min_size = min(sizes)
    max_size = max(sizes)
    avg_size = statistics.mean(sizes)

    min_file = [os.path.join(root, file) for root, file in cpp_files if os.path.getsize(os.path.join(root, file)) == min_size]
    max_file = [os.path.join(root, file) for root, file in cpp_files if os.path.getsize(os.path.join(root, file)) == max_size]
    avg_files = sorted(cpp_files, key=lambda x: abs(os.path.getsize(os.path.join(x[0], x[1])) - avg_size))[:3]

    print(f"Files: {len(cpp_files)}")
    print(f"Min size: {min_size}, File: {min_file}")
    print(f"Max size: {max_size}, File: {max_file}")
    print(f"Avg size: {avg_size}, Files: {avg_files}")

if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)