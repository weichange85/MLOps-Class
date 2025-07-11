import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    """
    Format a string as JSON.
    
    :param string: The string to format.
    :param sort_keys: Whether to sort the keys in the JSON output.
    :return: Formatted JSON string.
    """
    try:
        data = json.loads(string)
        return json.dumps(data, indent=4, sort_keys=sort_keys)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"
    
def main(path):
    """
    Read a file and format its content as JSON.
    
    :param path: Path to the file to read.
    """
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        sys.exit(1)
    
    with open(path, 'r') as file:
        content = file.read()
    
    formatted_content = formatter(content)
    print(formatted_content)

if __name__ == "__main__":
    # print(sys.argv)
    # main(sys.argv[-1])
    parser = argparse.ArgumentParser(description="Format a file's content as JSON.")
    args = parser.parse_args()