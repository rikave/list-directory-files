import os
import sys
from collections import OrderedDict


def print_files(names, show_all):
    """Print filenames or extensions from a list"""
    for name, file_list in names.items():
        print("\n#### {} ####".format(name))
        for filename in file_list:
            print("{}".format(filename))
        #Return after printing desired files
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
        print("\nDirectory should be a path to your folder in string format.")
        return

    try:
        " ".endswith(tuple(extensions))
    except:
        print("\nExtensions should be a:\n"
              "\t- string\n"
              "\t- tuple/list/set of strings")
        return

    names = {
        "Desired files":    [],
        "Other files":      [],
        "Other extensions": set(),
    }

    # Older Python versions compatibility
    # Note: dicts keep original order since Python 3.6
    if sys.version < "3.6":
        order = ["Desired files", "Other files", "Other extensions"]
        names = OrderedDict(sorted(names.items(),
                                   key=lambda x: order.index(x[0])))

    # Walk through files and add their name/extension to lists
    for _, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(tuple(extensions)):
                names["Desired files"].append(filename)
            elif all_files == 1:
                names["Other files"].append(filename)
                names["Other extensions"].add("." + filename.split(".")[-1])

    if sorting == 1:
        for name in names:
            names[name] = sorted(names[name], key=lambda x: x.lower())

    print_files(names, all_files)
    print_summary(names, all_files)


if __name__ == "__main__":
    # e.g. directory = "E:/Music"
    directory = "your/folder/location"
    # e.g. extensions = [".mp3", ".wav"]
    extensions = [".mp3", ".wav"]
    # e.g. list_files(directory, extensions, sorting=1, all_files=1)
    list_files(directory, extensions)
