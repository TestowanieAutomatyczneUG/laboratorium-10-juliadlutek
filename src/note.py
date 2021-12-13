class Note:
    def __init__(self, note, name=''):
        if type(name) != str or name == '':
            raise Exception
        elif type(note) != float:
            raise Exception
        elif note < 2 or note > 6:
            raise Exception
        self.name = name
        self.note = note

    def getName(self):
        return self.name

    def getNote(self):
        return self.note


note1 = Note(5.0, "Julia")
print(note1.getName())
