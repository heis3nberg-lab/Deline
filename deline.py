import argparse

def modify_file(input_path, output_path, target_string):
    """Modify the file to remove lines containing the specified target string."""
    with open(input_path, 'r') as file:
        lines = file.readlines()

    with open(output_path, 'w') as file:
        for line in lines:
            # Check if the target string is present anywhere in the line
            if target_string in line:
                file.write('\n')  # Write a blank line instead
            else:
                file.write(line)  # Write the original line

def main():
    """Process the command-line arguments and modify the file accordingly."""
    parser = argparse.ArgumentParser(
        description="Remove lines containing a specified string from a file to reduce false positives in data scans.",
        epilog="Example usage: python deline.py -str 'target_string' -i input_file.txt -o output_file.txt"
    )

    parser.add_argument("-str", "--string", type=str, required=True, help="String that identifies the lines to remove")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to the output file")

    args = parser.parse_args()

    # Modify the file based on the specified criteria
    modify_file(args.input, args.output, args.string)

if __name__ == "__main__":
    main()
