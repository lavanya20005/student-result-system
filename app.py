from db_config import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            roll_no VARCHAR(20),
            subject VARCHAR(50),
            marks INT
        )
    """)
    conn.commit()
    conn.close()

def insert_result(name, roll_no, subject, marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (name, roll_no, subject, marks) VALUES (%s, %s, %s, %s)",
                   (name, roll_no, subject, marks))
    conn.commit()
    conn.close()

def fetch_results():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results")
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_result("Lavanya", "21MCA01", "Python", 95)
    insert_result("Ravi", "21MCA02", "Java", 88)
    print("📊 Student Results:")
    fetch_results()
