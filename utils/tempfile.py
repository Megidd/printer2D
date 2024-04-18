import tempfile
import os

def create_temp_file(prefix, suffix, dir=None):
    # Create a temporary file using tempfile.mkstemp
    # This function returns a tuple containing the OS-level handle and the absolute pathname of the temp file
    fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dir)
    
    # Close the file descriptor to avoid leaking
    os.close(fd)
    
    # Return the path of the temp file for further use
    return path
