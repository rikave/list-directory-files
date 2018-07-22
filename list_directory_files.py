import os
import sys
from collections import OrderedDict


def directory_walker(directory):
    """Perform os.walk in directory"""
    return os.walk(directory)


def print_files(names, show_all):
    """Print filenames or extensions from a list"""
    for name, file_list in names.items():
        print("\n#### {} ####".format(name))
        for file in file_list:
            print("{}".format(file))
        #Return after printing desired files (dicts are sorted
        if not show_all:
            return


def print_summary(names, show_all):
    """Print amount of certain files or extensions found"""
    print("\n#### Summary ####")
    for name in names:
        print("---> {} found: {}".format(name, len(names[name])))
        if not show_all:
            return


def list_files(directory, extensions, sorting=1, all_files=1):
    """
    Print names of files with specified extension(s) in given directory
    and its subdirectories. By default list other files and extensions found

    - Print names of files with specified extensions
    - Print names of other files and extensions found -- optional
    - Print set of other file extensions -- optional

    Keyword arguments:
    - directory  -- path of the folder to be used
    - extensions -- str or tuple, list or set of desired extensions as strings
    - sorting:   -- determines if files should be sorted (default 1)
        = 1             -- sort file names
        = <other value> -- leave default order in which the files were found
    - all_files  -- determines if other files should be included (default 1)
        = 1             -- show all files divided into desired and other
        = <other value> -- show only desired files
    """

    if not isinstance(directory, str):
        print("A string with path is expected.")
        return

    try:
        " ".endswith(tuple(extensions))
    except:
        print("\nWrong extensions format:\n" \
              "Extensions must be a:\n" \
              "\t- string\n"\
              "\t- tuple/list/set of strings")
        return

    names = {
        "Desired files":    [],
        "Other files":      [],
        "Other extensions": set(),
    }

    # Older python versions compatibility
    if sys.version < "3.6":
        order = ["Desired files", "Other files", "Other extensions"]
        names = OrderedDict(sorted(names.items(),
                                   key=lambda x: order.index(x[0])))

    # Walk through files and add their names to lists
    for _, _, files in directory_walker(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                names["Desired files"].append(file)
            elif all_files == 1:
                names["Other files"].append(file)
                names["Other extensions"].add("." + file.split(".")[-1])

    if sorting == 1:
        names["Desired files"] = sorted(names["Desired files"],
                                        key=lambda x: x.lower())
        names["Other files"] = sorted(names["Other files"],
                                      key=lambda x: x.lower())
        names["Other extensions"] = sorted(names["Other extensions"],
                                           key=lambda x: x.lower())

    print_files(names, all_files)
    print_summary(names, all_files)


if __name__ == "__main__":
    #e.g. directory = "E:/Music"
    directory = "your/folder/location"
    # e.g. [".mp3", ".wav"]
    extensions = [".mp3"]
    # list_files(directory, extensions, sorting=1, all_files=1)
    list_files(directory, extensions)
