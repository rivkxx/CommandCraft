import os
import curses

# Function to create or open a file
def create_or_open_file():
    try:
        file_name = input("Enter file name: ")
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                print("File opened successfully!\n")
                return content
        else:
            print("File doesn't exist. Creating a new file...\n")
            return ""
    except Exception as e:
        print("Error:", e)
        return ""

# Function to save the content to a file
def save_file(content):
    try:
        file_name = input("Enter file name to save: ")
        with open(file_name, 'w') as file:
            file.write(content)
            print("File saved successfully!\n")
    except Exception as e:
        print("Error:", e)

# Function to compile the code
def compile_code():
    try:
        compiler_cmd = input("Enter compiler command: ")
        os.system(compiler_cmd)
    except Exception as e:
        print("Error:", e)

# Function to run the compiled code
def run_code():
    try:
        run_cmd = input("Enter run command: ")
        os.system(run_cmd)
    except Exception as e:
        print("Error:", e)

# Function to handle key press events
def handle_keypress(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Terminal Code Editor!\n")
    stdscr.addstr("Press Ctrl+S to save, Ctrl+O to open/create a file, Ctrl+E to compile, Ctrl+F to run, or Ctrl+C to exit.\n")

    while True:
        key = stdscr.getch()
        if key == curses.KEY_EXIT or key == 3:  # Ctrl+C
            break
        elif key == curses.KEY_SAVE:  # Ctrl+S
            save_file(content)
        elif key == curses.KEY_OPEN:  # Ctrl+O
            content = create_or_open_file()
        elif key == ord('e'):  # Ctrl+E
            compile_code()
        elif key == curses.KEY_RUN:  # Ctrl+F
            run_code()

# Main function
if __name__ == "__main__":
    content = ""
    curses.wrapper(handle_keypress)


               __
              / _)
     _.----._/ /
    /         /
 __/ (  |  (  |
/__.-'|_|--|__|
