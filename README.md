# List Directory Files

A tool used to list all files with specified extension(s) found in directory and all of its subdirectories.

## How it works?
It goes through all subdirectories of the main location and returns filenames which end with specified extensions.
By default all unmatched files and their extensions are also presented in groups after the main list. It allows you
to see whether you've missed something special. At the end it tells you how many entries of each type were found.
[For more see the docs.](#docs)

## Available options
* sorting
* listing other files and extensions

## Docs
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
    
