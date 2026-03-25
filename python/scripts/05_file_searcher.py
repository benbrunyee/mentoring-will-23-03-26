# =============================================================================
# FILE SEARCHER
# Concepts: file reading with open(), os.listdir(), string methods,
#           for loops, functions, formatted output, early continue
# =============================================================================
#
# Run 04_file_creator.py first to create the sample_files/ folder.
# This script then searches every .txt file in that folder for a keyword.
# =============================================================================

import os

SEARCH_FOLDER = "sample_files"


def find_matching_lines(filepath, keyword):
    """
    Read a file and return a list of (line_number, line_text) tuples
    for every line that contains the keyword (case-insensitive).
    """
    matches = []

    # "r" mode opens the file for reading
    with open(filepath, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # .lower() on both sides makes the search case-insensitive
            if keyword.lower() in line.lower():
                matches.append((line_number, line.rstrip()))

    return matches


def search_folder(folder, keyword):
    """
    Search every .txt file in the folder for the keyword.
    Returns a dictionary mapping filename -> list of matching lines.
    """
    results = {}

    # os.listdir() gives us all the file/folder names inside a directory
    all_entries = os.listdir(folder)

    for filename in sorted(all_entries):
        # Only process .txt files, skip anything else
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(folder, filename)

        # os.path.isfile() makes sure we're not trying to read a sub-folder
        if not os.path.isfile(filepath):
            continue

        matches = find_matching_lines(filepath, keyword)

        if matches:
            results[filename] = matches

    return results


def display_results(results, keyword, total_files_searched):
    """Print the search results in a readable format."""
    print()
    if not results:
        print(f"No matches found for '{keyword}' in {total_files_searched} file(s).")
        return

    total_matches = sum(len(lines) for lines in results.values())
    print(f"Found '{keyword}' in {len(results)} file(s) — {total_matches} match(es) total.\n")

    for filename, matches in results.items():
        print(f"  {filename}  ({len(matches)} match(es))")
        for line_number, line_text in matches:
            print(f"    Line {line_number:3d}: {line_text}")
        print()


def main():
    print("=== File Searcher ===\n")

    # Check the folder exists before trying to search it
    if not os.path.exists(SEARCH_FOLDER):
        print(f"The folder '{SEARCH_FOLDER}' doesn't exist.")
        print("Please run 04_file_creator.py first to create the sample files.")
        return

    # Count how many .txt files are available
    txt_files = [f for f in os.listdir(SEARCH_FOLDER) if f.endswith(".txt")]
    print(f"Found {len(txt_files)} .txt file(s) in '{SEARCH_FOLDER}/'")
    print()

    while True:
        keyword = input("Enter a keyword to search for (or 'quit' to exit): ").strip()

        if keyword.lower() == "quit":
            print("Goodbye!")
            break

        if not keyword:
            print("Please enter a keyword.\n")
            continue

        results = search_folder(SEARCH_FOLDER, keyword)
        display_results(results, keyword, len(txt_files))


if __name__ == "__main__":
    main()
