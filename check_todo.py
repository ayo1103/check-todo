import sys
from subprocess import check_output

def check_files_for_todo():
    # Get all files added to the staging area
    files = check_output(['git', 'diff', '--cached', '--name-only']).decode().split()

    # Check each file for 'TODO'
    todo_found = False
    for file in files:
        with open(file, 'r') as f:
            if 'TODO' in f.read():
                print(f'TODO found in {file}, please remove it before committing.')
                todo_found = True

    if todo_found:
        sys.exit(1)

if __name__ == '__main__':
    check_files_for_todo()
