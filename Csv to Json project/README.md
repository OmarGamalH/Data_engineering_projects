# CSV to JSON Converter

This project scans the current working directory for CSV files, extracts specific fields from them, and writes the extracted data into a single `result.json` file.

## Features

- Automatically finds all `.csv` files in the current directory
- Extracts specific fields: `region`, `variety`, and `rating`
- Combines extracted data from multiple files into one JSON output
- Handles file reading errors gracefully

## Project Structure

```
.
├── files.py        # Helper function to get CSV files from a path
├── Project.py      # Main script to extract data and save as JSON
└── result.json     # Output file (generated after running the script)
```

## Usage

1. Place your `.csv` files in the same directory as the scripts.
2. Make sure each CSV file includes the headers: `region`, `variety`, and `rating`.
3. Run the main script:

```bash
python Project.py
```

4. Check the `result.json` file in the same directory for the output.

## Example CSV Format

```csv
region,variety,rating
Ethiopia,Heirloom,4.5
Colombia,Typica,4.2
```

## Requirements

- Python 3.x

> This project uses only built-in Python modules (`csv`, `json`, `os`, and `glob`), so no additional installation is needed.

## Notes

- If no CSV files are found or the path is invalid, the script will notify the user.
- Files that can't be read properly will be skipped with a warning message.

## License

This project is licensed under the MIT License.
