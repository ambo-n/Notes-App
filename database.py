import sqlite3

class Database:
    def __init__(self, db_name ="notes.db"):
        # establishing db connection
        self.connection = sqlite3.connect(db_name)
        # creates a cursor objectscu
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")
        self.connection.commit()
    
    def add_notes(self, title, body):
        self.cursor.execute("""INSERT INTO notes (title, body) VALUES (?,?)""", (title, body))
        self.connection.commit()
    
    def get_notes(self):
        self.cursor.execute("""SELECT * FROM notes""")
        return self.cursor.fetchall()
    def get_note(self, note_id):
        self.cursor.execute("""SELECT * FROM notes WHERE id=?""", (note_id,))
        return self.cursor.fetchone()

    def update_note(self, note_id, title, body):
        self.cursor.execute("""UPDATE notes SET title=?, body=?, updated_at=CURRENT_TIMESTAMP WHERE id=?""", (title, body, note_id))
        self.connection.commit()
    
    def delete_note(self, note_id):
        self.cursor.execute("""DELETE FROM notes WHERE id=?""", (note_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
