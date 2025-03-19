from database import Database

class Note:
    def __init__(self, title, body, note_id=None, created_at=None, updated_at=None):
        self.id = note_id
        self.title = title
        self.body = body
        self.create_at = created_at
        self.updated_at = updated_at
    
    def save(self):
        """Saves a new note or updates an existing one."""
        db = Database()
        if self.id is None:
            db.add_notes(self.title, self.body)
        else:
            db.update_note(self.id, self.title, self.body)
        db.close()
    
    def delete(self):
        """Deletes the note from the db"""
        if self.id is not None:
            db = Database()
            db.delete_note(self.id)
            db.close()
    
    def to_dict(self):
        """Returns a dictionary representation of the note"""
        return {
            "id": self.id,
            "title" :self.title,
            "body": self.body,
            "create_at": self.create_at,
            "update_at": self.updated_at
        }
    @staticmethod
    def get_all_notes():
        db = Database()
        all_notes = db.get_notes()
        db.close()
        return[Note(note_id=row[0], title=row[1], body=row[2], created_at=row[3], updated_at=row[4]) for row in all_notes]