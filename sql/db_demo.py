import sqlite3
import os

DB_FILE = "devinsight_test.db"

def run_db_demo():
    print("Initializing SQLite demo database...")
    # Ensure a fresh database for demonstration
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    
    conn = sqlite3.connect(DB_FILE, isolation_level=None)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE developers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE pull_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        status TEXT NOT NULL,
        FOREIGN KEY (author_id) REFERENCES developers(id)
    );
    """)

    # Populate tables
    cursor.execute("INSERT INTO developers (username, email) VALUES ('Anika Rao', 'anika@example.com')")
    cursor.execute("INSERT INTO developers (username, email) VALUES ('Mateo Chen', 'mateo@example.com')")
    
    # Run transaction workflow for Pull Request merge simulation
    print("Simulating PR merge transaction...")
    try:
        conn.execute("BEGIN TRANSACTION;")
        
        # 1. Insert PR record
        cursor.execute("INSERT INTO pull_requests (title, author_id, status) VALUES ('Implement Leaderboard', 1, 'merged')")
        
        # 2. Insert test validation statement
        cursor.execute("SELECT last_insert_rowid()")
        pr_id = cursor.fetchone()[0]
        
        # Commit the transaction
        conn.commit()
        print(f"Transaction completed. Merged PR #{pr_id} successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Transaction rolled back due to error: {e}")

    # Query rankings (grouping and count)
    print("\nQuerying developers and PR counts:")
    cursor.execute("""
    SELECT d.username, COUNT(pr.id) as merge_count
    FROM developers d
    LEFT JOIN pull_requests pr ON d.id = pr.author_id AND pr.status = 'merged'
    GROUP BY d.username
    ORDER BY merge_count DESC;
    """)
    for row in cursor.fetchall():
        print(f"  Developer: {row[0]}, Merged PRs: {row[1]}")

    conn.close()
    
    # Clean up file
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

if __name__ == "__main__":
    run_db_demo()
