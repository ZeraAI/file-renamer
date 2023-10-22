# Rename your files

## Introduction

This script was created out of a necessity to manage large amounts of images downloaded from a specific website. When these images were downloaded, the website's naming structure placed the file extension within the filename rather than at the end. This disrupted the ability for most software to recognize and properly open the images. To address this, the script was designed to restructure these filenames, ensuring the file extension is positioned correctly at the end.

## Overview

Files with names like:
`example-image.jpg-from-google-no-categories-perk-drummer`
will be renamed to:
`example-image-from-google-no-categories-perk-drummer.jpg`


## Prerequisites

- Python 3.x

## Usage

1. Place the renaming script in the same directory as your `downloaded-img` folder or adjust the `dir_name` in the script accordingly.
2. Run the script:
```
python3 rename-file.py
```
3. The script will process each file in the directory, renaming those that match the pattern and skipping others.

## How it Works

The script utilizes regular expressions to match file patterns and restructure their names. It specifically searches for filenames with misplaced extensions (such as `.jpg`, `.jpeg`, `.png`, and `.webp`) and moves the extension to the end of the filename.

Files that already match the desired pattern or don't fit the recognized patterns are skipped.

## Limitations

The script is designed specifically for the provided filename patterns. If the website changes its file naming conventions or if used with other types of files, modifications to the script may be necessary.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Feedback and improvements are always welcome!
