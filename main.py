import os
import zipfile
import subprocess
import sys

COUNT_FILES = [".cs", ".html", ".css", ".py", ".kt", ".java", ".rs"]

RED = "\033[91m"
RESET = "\033[0m"  # Reset color to default

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f"Error counting lines in '{file_path}': {e}")
        return 0


def zip_directory(path, output_path, blacklist_folders=[], blacklist_extensions=[]):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            # Remove blacklisted folders
            for folder in blacklist_folders:
                if folder in dirs:
                    dirs.remove(folder)

            for file in files:
                extension = os.path.splitext(file)[-1].lower()
                if extension not in blacklist_extensions:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, path)
                    zipf.write(file_path, arcname=arcname)
                    if extension in COUNT_FILES:
                        line_count = count_lines(file_path)
                        print(f"Lines in '{arcname}': {RED}{line_count}{RESET}")


if __name__ == '__main__':
    source_path = ""
    if len(sys.argv) > 1:
        source_path = sys.argv[1]
        print("Zipping " + source_path)
    else:
        source_path = input("Enter the source directory path: ")
    output_path = input("Enter the output zip file path: ")
    if "/" not in output_path:
        output_path = os.path.join(source_path, os.path.join(source_path, output_path) + ".zip")

    # Define the folder and extension blacklist
    folder_blacklist = [".git", ".idea", ".vs", "bin", "obj"]
    extension_blacklist = [".user", ".git", ".zip"]

    zip_directory(source_path, output_path, folder_blacklist, extension_blacklist)
    print("Zip file created successfully.")

    # Open the parent directory
    parent_directory = os.path.dirname(output_path)
    try:
        if os.name == 'nt':  # Check if the operating system is Windows
            subprocess.Popen(['explorer', '/select,', output_path])
        elif os.name == 'posix':  # Check if the operating system is macOS or Linux
            subprocess.Popen(['xdg-open', parent_directory])
        else:
            print("Opening the parent directory is not supported on this operating system.")
    except Exception as e:
        print(f"An error occurred while opening the parent directory: {e}")
    last_word = input("Input any key to exit.")
