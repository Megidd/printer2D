import shutil
import os

def move_and_overwrite(source, destination):
    # Check if the destination file exists
    if os.path.exists(destination):
        # Remove the existing file to ensure the move operation will overwrite it
        os.remove(destination)
    
    # Move (or rename) the source file to the destination
    shutil.move(source, destination)

def delete(filePath):
    # Check if the destination file exists
    if os.path.exists(filePath):
        # Remove the existing file to ensure the move operation will overwrite it
        os.remove(filePath)
