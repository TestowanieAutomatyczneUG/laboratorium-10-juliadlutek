import unittest
from src.note import Note


class NoteTest(unittest.TestCase):
    def setUp(self):
        self.temp = Note

    def test_init_correct(self):
        self.assertIsInstance(self.temp(5.0, "Julia"), Note)

    def test_init_note_2(self):
        self.assertIsInstance(self.temp(2.0, "Julia"), Note)

    def test_init_note_6(self):
        self.assertIsInstance(self.temp(6.0, "Julia"), Note)

    def test_none_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0, None))

    def test_int_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0, 10))

    def test_float_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0, 12.45))

    def test_bool_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0, True))

    def test_array_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0, ["Name"]))

    def test_empty_name(self):
        with self.assertRaises(Exception):
            (self.temp(5.0))

    def test_note_too_small(self):
        with self.assertRaises(Exception):
            (self.temp(-1.2, "Julia"))

    def test_note_too_big(self):
        with self.assertRaises(Exception):
            (self.temp(10.3, "Julia"))

    def test_str_note(self):
        with self.assertRaises(Exception):
            (self.temp("5.0", "Julia"))

    def test_int_note(self):
        with self.assertRaises(Exception):
            (self.temp(5, "Julia"))

    def test_None_note(self):
        with self.assertRaises(Exception):
            (self.temp(None, "Julia"))

    def test_bool_note(self):
        with self.assertRaises(Exception):
            (self.temp(False, "Julia"))

    def test_array_note(self):
        with self.assertRaises(Exception):
            (self.temp([1, 2, 3], "Julia"))

    def test_get_name(self):
        note = self.temp(5.0, "Julia")
        self.assertEqual(note.getName(), "Julia")

    def test_get_note(self):
        note = self.temp(5.0, "Julia")
        self.assertEqual(note.getNote(), 5.0)



