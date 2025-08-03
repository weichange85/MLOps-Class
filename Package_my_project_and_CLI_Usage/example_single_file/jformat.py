import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    try:
        data = json.loads(string)
        return json.dumps(data, indent=indent, sort_keys=sort_keys)
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"

def main():
    parser = argparse.ArgumentParser(description="Format a file's content as JSON.")
    parser.add_argument("path", help="Path to the JSON file to format")
    parser.add_argument("--no-sort", action="store_true", help="Don't sort JSON keys")
    parser.add_argument("--indent", type=int, default=4, help="Number of spaces to indent")
    args = parser.parse_args()

    path = args.path
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        sys.exit(1)

    with open(path, 'r') as file:
        content = file.read()

    formatted_content = formatter(
        content,
        sort_keys=not args.no_sort,
        indent=args.indent,
    )
    print(formatted_content)

if __name__ == "__main__":
    main()
