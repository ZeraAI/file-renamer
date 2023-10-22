import os
import re

# make sure to modify where it says "example-folder-name" to your own
def rename_files_in_directory(dir_name="example-folder-name"):
    """
    Renames files in the specified directory by moving the file extension to the end.
    
    Parameters:
    - dir_name (str): The name of the directory where the files are located.

    For example:
    'example-image.jpg-from-google-no-categories-perk-drummer' 
    will be renamed to 
    'example-image-from-google-no-categories-perk-drummer.jpg'
    """
    
    # Iterate through each file in the specified directory
    for filename in os.listdir(dir_name):
        
        # Use a regular expression to identify the file's structure.
        # The pattern we are looking for has four groups:
        # 1. The main part of the filename before the extension.
        # 2. The dot and the image extension (like .jpg, .jpeg, .png, .webp, .gif).
        # 3. The image extension without the dot.
        # 4. The '-from-' part and everything after it.
        match = re.match(r'^(.*?)(\.(jpg|jpeg|png|webp|gif))(-from-.*)$', filename, re.IGNORECASE)
        
        # If the filename matches our pattern, proceed to rename it
        if match:
            print(f"Processing: {filename}")
            
            # Construct the new filename using the matched groups
            new_name = f"{match.group(1)}{match.group(4)}{match.group(2)}"
            
            # Get the full paths for the old and new filenames
            old_path = os.path.join(dir_name, filename)
            new_path = os.path.join(dir_name, new_name)
            
            # Ensure that the old and new paths are different
            # This avoids unnecessary renaming operations
            if old_path != new_path:  
                os.rename(old_path, new_path)
                print(f"Renamed to: {new_name}")
            else:
                print(f"Skipped {filename} as it's already in the desired format.")
        else:
            # If the filename doesn't match our pattern, skip it
            print(f"Skipped {filename} as it doesn't match the expected pattern.")

if __name__ == "__main__":
    # Call the rename function to process files in the 'downloaded-img' directory
    rename_files_in_directory()
