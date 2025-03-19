from database import Database

db = Database()

db.add_notes("First Note", "This is the body of the first note")
notes= db.get_notes()
for note in notes:
    print(note)

db.update_note(6, "Updated Title for the first note", "Updated Body")


db.close()