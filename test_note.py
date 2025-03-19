from note import Note

new_note= Note(title="My Second Note", body="This is a test note.")
new_note.save()

notes = Note.get_all_notes()
for note in notes:
    print(note)
    print(note.to_dict())

if notes:
    first_note = notes[0]
    first_note.title = "Updated Title"
    first_note.body = "Updated Content"
    first_note.save()
    print(first_note.title)


if notes:
    first_note.delete()