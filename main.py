import pandas as pd
import sqlite3
import sys

# Read the name of the file
sNameOfFile = sys.argv[1]

# Reading the file
print(f"Reading the file {sNameOfFile}")

# Load excel
xFile = pd.read_excel(sNameOfFile)

# Create a SQLite conn
sqlConnection = sqlite3.connect( sys.argv[2] or "isss-db.db")

# Write to the db
xFile.to_sql("isss", sqlConnection, if_exists="replace", index=True)

sqlConnection.close()