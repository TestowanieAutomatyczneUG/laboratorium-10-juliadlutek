import unittest
from unittest.mock import *
from src.notesStorage import NotesStorage
from src.notesService import NotesService
from src.note import Note


class TestNotesService(unittest.TestCase):
    def test_add_note(self):
        storage = NotesStorage()
        service = NotesService(storage)
        note = Note(5.0, "Julia")
        storage.add = Mock(name="addNote")
        storage.add.return_value = "New node created!"
        self.assertEqual(service.add(note), "New node created!")

    def test_average_of(self):
        storage = NotesStorage()
        service = NotesService(storage)
        storage.getAllNotesOf = Mock(name="getAllNotes")
        storage.getAllNotesOf.return_value = [Note(3.0, "Julia"), Note(4.0, "Julia"), Note(5.0, "Julia")]
        self.assertEqual(service.averageOf("Julia"), 4)

    def test_average_of_empty_storage(self):
        storage = NotesStorage()
        service = NotesService(storage)
        storage.getAllNotesOf = Mock(name="getAllNotes")
        storage.getAllNotesOf.return_value = []
        self.assertEqual(service.averageOf("Julia"), "There are no notes to delete")

    def test_average_incorrect_arg_empty(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf(""))

    def test_average_incorrect_arg_num(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf(50))

    def test_average_incorrect_arg_arr(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf([]))

    def test_average_incorrect_arg_float(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf(0.23))

    def test_average_incorrect_arg_none(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf(None))

    def test_average_incorrect_arg_bool(self):
        storage = NotesStorage()
        service = NotesService(storage)
        with self.assertRaises(Exception):
            (service.averageOf(True))

    def test_clear(self):
        storage = NotesStorage()
        service = NotesService(storage)
        storage.clear = Mock(name="clear")
        storage.clear.return_value = "All notes deleted!"
        self.assertEqual(service.clear(), "All notes deleted!")
