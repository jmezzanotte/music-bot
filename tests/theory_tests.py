import unittest
from theory.scales import *

class TestScale(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestScale, self).__init__(*args, **kwargs)
        self.major_scale_dict = {
            'c': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'g': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
            'd': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
            'a': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
            'e': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
            'b': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
            'f': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
            'bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
            'eb': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
            'ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
            'db': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
            'gb': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],


        }
        self.minor_scale_dict = {
            'c#': ['c#', 'd#', 'e', 'f#', 'g#', 'a', 'b'],
            'c': ['c', 'd', 'eb', 'f', 'g', 'ab', 'bb'],
            'd': ['d', 'e', 'f', 'g', 'a', 'bb', 'c'],
            'e': ['e', 'f#', 'g', 'a', 'b', 'c', 'd'],
            'eb': ['eb','f', 'gb', 'ab', 'bb', 'cb', 'db'],
            'f': ['f', 'g', 'ab', 'bb', 'c', 'db', 'eb'],
            'g#': ['g#', 'a#', 'b', 'c#', 'd#', 'e', 'f#'],
            'g': ['g', 'a', 'bb', 'c', 'd', 'eb', 'f']
        }

    def test_major(self):

        for key, value in self.major_scale_dict.items():
            self.assertEqual(Major(root=key).scale(), value)

    def test_minor(self):
        for key, value in self.minor_scale_dict.items():
            self.assertEqual(Minor(root=key).scale(), value)


if __name__ == "__main__":
    unittest.main()