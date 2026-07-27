from fastapi import FastAPI
import pyodbc

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from Backend"}



conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:myserver.database.windows.net,1433;"
    "Database=mydb;"
    "Uid=myadmin;"
    "Pwd=YourPassword123;"
    "Encrypt=yes;"
)

@app.get("/users")
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 name FROM users")
    rows = cursor.fetchall()
    return {"users": [r[0] for r in rows]}
