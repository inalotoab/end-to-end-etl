import pyodbc

def load(df):
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=host.docker.internal;"
        "Database=CSV_Import_DB;"
        "UID=etluser;"
        "PWD=P@ssw0rd123;"
        "TrustServerCertificate=yes;"
    )

    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO EmployeeData (ID, Name, Department, Salary, LastUpdated) VALUES (?, ?, ?, ?, ?)",
            row['ID'], row['Name'], row['Department'], row['Salary'], row['LastUpdated']
        )
    conn.commit()
    print("Data loaded successfully!")
