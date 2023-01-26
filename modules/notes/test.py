from notes import Notes
import unittest
import time

empty_notes = [{"title": "", "date": int(time.time()), "text": ""}]


class Notes_test(unittest.TestCase):
    def test_add_note(self):
        notes = Notes()
        notes.add_note()

        self.assertEqual(notes.get_notes(), empty_notes)

    def test_delete_note(self):
        notes = Notes()
        notes.add_note()
        notes.delete_note(0)
        self.assertEqual(notes.get_notes(), [])

    # def test_add_notes(self):
    #     notes = Notes()
    #     notes.add_note()
    #     notes.edit_title(0, "Hello")
    #     notes.edit_text(0, "Hello world")
    #     notes.save()


if __name__ == "__main__":
    unittest.main()
