import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "spendly.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    with conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT    NOT NULL,
                email         TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL,
                created_at    TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL REFERENCES users(id),
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                date        TEXT    NOT NULL,
                description TEXT,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );
        """)
    conn.close()


def seed_db():
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count > 0:
        conn.close()
        return

    from werkzeug.security import generate_password_hash

    with conn:
        conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", generate_password_hash("demo123", method="pbkdf2:sha256")),
        )

    user_id = conn.execute(
        "SELECT id FROM users WHERE email = ?", ("demo@spendly.com",)
    ).fetchone()["id"]

    sample_expenses = [
        (user_id, 45.00, "Food",          "2026-06-01", "Weekly groceries"),
        (user_id, 32.50, "Transport",     "2026-06-03", "Monthly bus pass top-up"),
        (user_id, 850.00,"Bills",         "2026-06-05", "Rent"),
        (user_id, 18.75, "Health",        "2026-06-08", "Pharmacy"),
        (user_id, 15.99, "Entertainment", "2026-06-10", "Streaming subscription"),
        (user_id, 62.40, "Shopping",      "2026-06-14", "New shoes"),
        (user_id,  8.50, "Other",         "2026-06-18", "Miscellaneous"),
        (user_id, 22.00, "Food",          "2026-06-22", "Dinner out"),
    ]

    with conn:
        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description)"
            " VALUES (?, ?, ?, ?, ?)",
            sample_expenses,
        )

    conn.close()
