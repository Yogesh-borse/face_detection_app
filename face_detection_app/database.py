import os
import psycopg2
import sqlite3
from urllib.parse import urlparse

# Get database URL from environment (Heroku provides DATABASE_URL)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """Return a PostgreSQL connection on Heroku, else fallback to SQLite locally."""
    if DATABASE_URL:
        result = urlparse(DATABASE_URL)

        return psycopg2.connect(
            database=result.path[1:],
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
    else:
        # Local development fallback
        return sqlite3.connect("users.db")

def init_db():
    """Initialize database tables if not exist."""
    conn = get_connection()
    c = conn.cursor()

    # For PostgreSQL, need SERIAL instead of AUTOINCREMENT
    c.execute('''CREATE TABLE IF NOT EXISTS users_auth (
                    user_id SERIAL PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS users_info (
                    info_id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    full_name TEXT,
                    activity_log TEXT,
                    FOREIGN KEY(user_id) REFERENCES users_auth(user_id)
                )''')

    conn.commit()
    conn.close()

def insert_user(email, password_hash, full_name=""):
    """Insert new user into both tables (transaction)."""
    conn = get_connection()
    c = conn.cursor()
    try:
        # Insert into users_auth
        c.execute("INSERT INTO users_auth (email, password_hash) VALUES (%s, %s) RETURNING user_id",
                  (email, password_hash))
        user_id = c.fetchone()[0]

        # Insert into users_info
        c.execute("INSERT INTO users_info (user_id, full_name, activity_log) VALUES (%s, %s, %s)",
                  (user_id, full_name, "Signed up"))

        conn.commit()
        return user_id
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()

def get_user_by_email(email):
    """Fetch user authentication record by email."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT user_id, password_hash FROM users_auth WHERE email = %s", (email,))
    row = c.fetchone()
    conn.close()
    return row

def log_activity(user_id, activity):
    """Update user activity log."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users_info SET activity_log = %s WHERE user_id = %s", (activity, user_id))
    conn.commit()
    conn.close()
