import argparse
from note import Note

def create_note(title, body):
    note = Note(title=title, body=body)
    note.save()
    print(f"Note {title} created.")

def view_notes():
    notes = Note.get_all_notes()
    if not notes:
        print("No notes found")
    for note in notes:
        print(f"\nID: {note.id}")
        print(f"Title: {note.title}")
        print(f"Body: {note.body}")
        print(f"Created at: {note.create_at}")
        print(f"Updated at: {note.updated_at}")

def update_note(note_id, title, body):
    notes = Note.get_all_notes()
    note = next((n for n in notes if n.id == note_id), None)
    if note:
        note.title = title
        note.body = body
        note.save()
        print(f"Note {note_id} updated successfully")
    else:
        print(f"Unable to find note with ID: {note_id}")

def delete_note(note_id):
    notes = Note.get_all_notes()
    note = next((n for n in notes if n.id == note_id),None)
    if note:
        note.delete()
        print(f"Note {note_id} deleted successfully!")
    else:
        print(f"Unable to find Note with ID: {note_id}")

def main():
    parser = argparse.ArgumentParser(description="Notes App CLI")
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Create a new note")
    create_parser.add_argument("title", type=str, help="Tile of the note")
    create_parser.add_argument("body", type=str, help="Body of the note")

    subparsers.add_parser("view", help="View all notes")

    update_parser = subparsers.add_parser("update", help="Update an existing note")
    update_parser.add_argument("note_id", type=int, help="ID of the note to update")
    update_parser.add_argument("title", type=str, help="New title of the note")
    update_parser.add_argument("body",type=str, help="Body of the note to update")

    delete_parser = subparsers.add_parser("delete", help="Delete an existing note")
    delete_parser.add_argument("note_id", type=int, help="ID of the note to delete")

    args = parser.parse_args()

    if args.command == "create":
        create_note(args.title, args.body)
    elif args.command == "view":
        view_notes()
    elif args.command == "update":
        update_note(args.note_id, args.title, args.body)
    elif args.command == "delete":
        delete_note(args.note_id)
    else:
        print("Invalid command. Use --help to see available commands.")


if __name__ == "__main__":
    main()