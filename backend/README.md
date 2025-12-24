To run locally 
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Commands to create database using SQL shell locally 
```bash
- ALTER USER postgres WITH PASSWORD 'postgres'; 
- CREATE DATABASE sitesage;

- \l
```