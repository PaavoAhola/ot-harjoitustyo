import unittest
from entities.crosswords import Crossword, Square


class TestCrossword(unittest.TestCase):
    def setUp(self):
        self.cross = Crossword("Pallo", "Pelle")

    def test_crossword_name_correct(self):
        cross = Crossword("PelleHermanni69", "123456789")
        name = cross.name

        self.assertEqual(name, "PelleHermanni69")

    def test_crossword_creator_correct(self):
        cross = Crossword("PelleHermanni69", "123456789")
        creator = cross.creator

        self.assertEqual(creator, "123456789")

    def test_crossword_has_correct_size(self):
        cross = Crossword("Pallo", "Pelle")
        counter = 0
        for row in cross.squares:
            for block in row:
                counter += 1

        self.assertEqual(counter, 100)

    def test_not_too_many_highscores(self):
        for i in range(11):
            self.cross.add_highscore(i, "Mika")

        amount = len(self.cross.highscores)
        self.assertEqual(amount, 10)

    def test_highscores_in_order(self):
        for i in range(5):
            self.cross.add_highscore(10-i, "Mika")

        first = self.cross.highscores[0][0]
        self.assertEqual(first, 6)

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(1,1)

    def test_switching(self):
        value1 = self.square.on
        self.square.switch()
        value2 = self.square.on

        self.assertEqual(value1, not value2)

    def test_changeable_letter(self):
        self.square.insert_letter("v")
        x = self.square.letter

        self.assertEqual(x, "v")
