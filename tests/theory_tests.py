import unittest
from theory.scales import *

class TestScale(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestScale, self).__init__(*args, **kwargs)
        self.scale_dict = {
            'c': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'g': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
            'd': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
            'a': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
            'e': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
            'b': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
            'f': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
            'eb': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
            'ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],

        }

    def test_major(self):

        for key, value in self.scale_dict.items():
            self.assertEqual(Major(root=key).scale(), value)




if __name__ == "__main__":
    unittest.main()