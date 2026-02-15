import csv
import sys
import io


def csv_to_markdown():
    print("Paste your CSV data (Press Ctrl+D or Ctrl+Z on Windows when finished):")

    # Read all input from the console
    input_data = sys.stdin.read()

    if not input_data.strip():
        print("No data received.")
        return

    # Use io.StringIO to treat the string like a file
    reader = csv.reader(io.StringIO(input_data.strip()))
    rows = list(reader)

    if not rows:
        return

    # Extract headers and data rows
    headers = rows[0]
    data = rows[1:]

    # Create the separator line (e.g., | --- | --- |)
    separator = ["---"] * len(headers)

    # Format the table
    markdown_table = [f"| {' | '.join(headers)} |", f"| {' | '.join(separator)} |"]

    for row in data:
        # Ensure rows match header length to avoid indexing errors
        padded_row = row + [""] * (len(headers) - len(row))
        markdown_table.append(f"| {' | '.join(padded_row)} |")

    # Output the result
    print("\n--- Markdown Output ---\n")
    print("\n".join(markdown_table))


if __name__ == "__main__":
    csv_to_markdown()