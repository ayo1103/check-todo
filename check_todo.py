import sys
from subprocess import check_output, CalledProcessError

def check_for_todo():
    try:
        # Get a list of all staged files
        files = check_output(['git', 'diff', '--cached', '--name-only']).decode().splitlines()
        todo_found = False

        for file in files:
            try:
                with open(file, 'r') as f:
                    if any('TODO' in line for line in f):
                        print(f'TODO found in {file}')
                        todo_found = True
            except Exception as e:
                print(f"Error reading {file}: {e}")

        if todo_found:
            print("Commit blocked because 'TODO' was found in the files above.")
            sys.exit(1)

    except CalledProcessError as e:
        print(f"Failed to get staged files: {e}")
        sys.exit(1)

def main():
    check_for_todo()

if __name__ == "__main__":
    main()
