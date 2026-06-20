import psycopg2
import json
import os

# Natively routes to the Postgres container via the Docker bridge
DB_HOST = os.getenv("DB_HOST", "host.docker.internal")

def get_db_connection():
    return psycopg2.connect(
        dbname="recon_data",
        user="watchtower_admin",
        password="watchtower_secure_2026",
        host=DB_HOST,
        port="5432"
    )

def log_sweep(target, source, raw_data_dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sweeps (target, source, raw_data) VALUES (%s, %s, %s)",
        (target, source, json.dumps(raw_data_dict))
    )
    conn.commit()
    cursor.close()
    conn.close()
