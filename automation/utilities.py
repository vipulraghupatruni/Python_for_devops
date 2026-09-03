"""
packages:
    are python functions that can be imported  
    in some other code file
"""

import json
def read_file(filename):
    """
    Reads the contents of a file and returns the lines as a list.
    
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r") as file:
        return file.readlines()

def write_json(filename,json_objects):
    with  open(filename, "w+") as file:
        json.dump(json_objects, file)  # Added indent=4 for pretty JSON formatting
        
