"""Main script"""


import sys
from pathlib import Path
from colorama import Fore, Back, Style


def show_directory_structure(directory: Path, prefix=""):
    """
    Recursively shows the directory structure.
    
    :param directory: The path to the directory, 
    the structure of which must be shown
    :param prefix: Prefix for indentation (used for recursion)
    """

    for item in sorted(directory.iterdir()):
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{Back.YELLOW} {item.name}{Style.RESET_ALL}")
            # Using recursion if there is a directory
            show_directory_structure(item, prefix + "  ")
        else:
            print(f"{prefix}{Fore.YELLOW}{Back.BLUE} {item.name}{Style.RESET_ALL}")

def main():
    """
    The main function that handles command line arguments 
    and calls the function that shows the directory structure
    """

    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: Please enter the path to the directory.{Style.RESET_ALL}")
        print(f"Using: python {sys.argv[0]} /path/to/directory")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    # Check if directory exists
    if not directory_path.exists():
        print(f"{Fore.RED}Error: Directory {directory_path} doesn't exist.{Style.RESET_ALL}")
        sys.exit(1)

    # Check if path is not a directory
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: {directory_path} is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}{Back.GREEN} The structure of directory \
          {directory_path}:{Style.RESET_ALL}")

    show_directory_structure(directory_path)

if __name__ == '__main__':
    main()
