# xlsx-to-sqlite

`xlsx-to-sqlite` is a Python tool that converts Excel (`.xlsx`) files into SQLite databases. This project provides an easy way to import data from Excel spreadsheets into a SQLite database, allowing for efficient data management and querying.

## Features

- **Convert Excel to SQLite:** Transform Excel spreadsheets into SQLite database files.
- **Multiple Sheets:** Handle multiple sheets within an Excel file.
- **Simple CLI:** Easy-to-use command-line interface for quick conversions.

## Requirements

- **Python 3.6+**: Ensure Python 3.6 or higher is installed.
- **Dependencies**: `pandas`, `openpyxl`, `sqlite3` (included in Python standard library)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kevingcfcb88/xlsx-to-sqlite.git
   cd xlsx-to-sqlite
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To convert an Excel file to a SQLite database, use the following command:

```bash
python xlsx_to_sqlite.py path/to/yourfile.xlsx path/to/output.db
```

### Command-Line Options

- **Input File:** Path to the `.xlsx` file you want to convert.
- **Output File:** Path to the SQLite database file to be created.

### Example

Convert an Excel file named `data.xlsx` to an SQLite database named `data.db`:

```bash
python xlsx_to_sqlite.py data.xlsx data.db
```

## Notes

- The script processes all sheets in the Excel file and creates corresponding tables in the SQLite database.
- Ensure that the Excel file has column headers as they will be used as column names in the SQLite tables.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **pandas:** For data manipulation.
- **openpyxl:** For reading Excel files.

---

Feel free to adjust the content as needed based on additional features or specific details about the project.
