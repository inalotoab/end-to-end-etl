# 🛠️ End-to-End ETL Pipeline with Airflow, Docker, and SQL Server

This project is a complete ETL (Extract, Transform, Load) pipeline using:
- **Apache Airflow** (via Docker)
- **Pandas** for data manipulation
- **SQL Server** as the destination database
- **CSV** as the source data format

---

## 📦 Project Structure

```
airflow/
├── dags/                  # Airflow DAGs
│   └── etl_dag.py         # Main DAG file
├── etl_project/           # Core ETL logic
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── Dockerfile             # Custom Airflow image with ODBC driver
├── docker-compose.yaml    # Orchestrates Airflow + Postgres
```

---

## 🔁 ETL Flow

1. **Extract**: Read data from a local CSV
2. **Transform**: Clean/filter/modify rows using Pandas
3. **Load**: Insert the data into a SQL Server table using `pyodbc`

---

## 🚀 Running It

### 1. Clone the repo

```bash
git clone https://github.com/your-username/end-to-end-etl.git
cd end-to-end-etl/airflow
```

### 2. Build and start Airflow

```bash
docker-compose build
docker-compose up -d
```

### 3. Access Airflow

- Open your browser: http://localhost:8080  
- Username: `admin`  
- Password: `admin`

Enable the DAG and trigger a manual run to see your ETL pipeline in action.

---

## 🗄️ SQL Server Connection Setup

Make sure:
- SQL Server is running on the host machine
- Mixed-mode authentication is enabled
- A login (`etluser`) is created with access to the `CSV_Import_DB` database

Update `load.py` with your actual username/password:

```python
pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=host.docker.internal;"
    "Database=CSV_Import_DB;"
    "UID=etluser;"
    "PWD=your_password;"
)
```

---

## 🧪 Testing

Use the Airflow UI to trigger DAG runs. Monitor logs per task and verify that rows appear in SQL Server.

---

## 📌 Notes

- This setup runs Airflow locally with a custom Dockerfile that includes the Microsoft ODBC driver.
- The DAG is modular (extract → transform → load) for better monitoring and separation of concerns.

---

## 📜 License

MIT — use freely and modify as needed.
