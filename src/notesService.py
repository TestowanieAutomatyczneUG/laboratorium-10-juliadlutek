from .notesStorage import NotesStorage
from .note import Note


class NotesService:
    def __init__(self, ns: NotesStorage):
        self.ns = ns

    def add(self, note: Note):
        return self.ns.add(note)

    def averageOf(self, name):
        if type(name) != str or len(name) == 0:
            raise Exception("Incorrect name")
        result = 0
        notes = self.ns.getAllNotesOf(name)
        if len(notes) == 0:
            return "There are no notes to delete"
        for note in notes:
            result += note.note
        return result/len(notes)

    def clear(self):
        return self.ns.clear()
