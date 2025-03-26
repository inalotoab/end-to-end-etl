FROM apache/airflow:2.7.0

USER root

# Install Microsoft ODBC Driver 17 for SQL Server
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev && \
    apt-get clean -y

# Switch back to airflow user to install Python package
USER airflow

# Install pyodbc (now as airflow user)
RUN pip install pyodbc
