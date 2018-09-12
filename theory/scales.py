__author__ = 'John Mezzanotte'

FLAT_SYMBOL = 'b'
SHARP_SYMBOL = '#'

CHROMATIC_SCALE_SHARP = ['c', 'c{}'.format(SHARP_SYMBOL), 'd', 'd{}'.format(SHARP_SYMBOL), 'e', 'f',
                         'f{}'.format(SHARP_SYMBOL), 'g', 'g{}'.format(SHARP_SYMBOL), 'a', 'a{}'.format(SHARP_SYMBOL),
                         'b']
CHROMATIC_SCALE_FLAT = ['c', 'd{}'.format(FLAT_SYMBOL), 'd', 'e{}'.format(FLAT_SYMBOL), 'e', 'f',
                        'g{}'.format(FLAT_SYMBOL),'g', 'a{}'.format(FLAT_SYMBOL), 'a', 'b{}'.format(FLAT_SYMBOL), 'b']

ROOT = 0
HALF_STEP = 1
WHOLE_STEP = 2

MAJOR_SCALE_FORMULA = [ROOT, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP]
MINOR_SCALE_FORMULA = [ROOT, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP]

TONIC = 0
SUPERTONIC = 1
MEDIANT = 2
SUBDOMINANT = 3
DOMINANT = 4
SUBMEDIANT = 5
LEADING_TONE = 6


class ChromaticScale:

    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.root = self.args.pop(0).lower() if len(self.args) > 0 else kwargs.get('root', 'c').lower()
        self.use_flats = args[0] if len(self.args) > 0 else kwargs.get('use_flats', [])

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        # validation, ensure this is a string
        try:
            self.__root = root.lower()
        except AttributeError as e:
            print(e)

    def chromatic_scale(self):

        # list of scales that should use flat, even if root symbol is not
        chromatic_scale = CHROMATIC_SCALE_FLAT if len(self.root) == 2 and len(self.root.split(FLAT_SYMBOL)) >= 2 or \
                                                  self.root in self.use_flats else CHROMATIC_SCALE_SHARP


        return chromatic_scale[chromatic_scale.index(self.root):] + \
            chromatic_scale[:chromatic_scale.index(self.root) - len(chromatic_scale)]


class DiatonicScale(ChromaticScale):

    '''
        Purpose
    '''

    def __init__(self, *args, **kwargs):
        super(DiatonicScale, self).__init__(*args, **kwargs)
        self.args = list(args)
        self.formula = self.args.pop(0) if len(self.args) > 0 else kwargs.get('formula', [])

    def scale(self):

        # Designed to pull the proper chromatic scale to build from
        chromatic_scale = self.chromatic_scale()

        counter = 0
        prev = 0
        scale = []
        while counter < len(self.formula):
            current = prev + self.formula[counter]
            scale.append(chromatic_scale[current])
            prev = current
            counter += 1

        return scale

    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula):

        if not isinstance(formula, list):
            raise TypeError("formula attribute must be a list")

        if len(formula) != 7:
            raise AttributeError("Diatonic Scale formula must consists of 7 elements.")

        self.__formula = formula

    @property
    def tonic(self):
        return self.scale()[TONIC]

    @property
    def super_tonic(self):
        return self.scale()[SUPERTONIC]

    @property
    def mediant(self):
        return self.scale()[MEDIANT]

    @property
    def subdominant(self):
        return self.scale()[SUBDOMINANT]

    @property
    def dominant(self):
        return self.scale()[DOMINANT]

    @property
    def submediant(self):
        return self.scale()[SUBMEDIANT]

    @property
    def leadingtone(self):
        return self.scale()[LEADING_TONE]

    @property
    def relative(self):
        return self.scale()[SUBMEDIANT]

    def __str__(self):
        return ' '.join(self.scale())


class Major(DiatonicScale):

    def __init__(self, root='c'):
        super(Major, self).__init__(root=root, use_flats=['f'], formula=MAJOR_SCALE_FORMULA)

    def __str__(self):
        return ' '.join([note.upper() if len(note) == 1 else note[0].upper() + note[1] for note in self.scale()])

    def scale(self):

        cb_flag = False
        if self.root == 'cb':
            cb_flag = True
            self.root = 'c'

        scale = [note.upper() if len(note) == 1 else note[0].upper() + note[1] for note in super(Major, self).scale()]

        if cb_flag:
            scale = ["{0}{1}".format(note, 'b') for note in scale]
            # Change the root back
            self.root = 'cb'

        if self.root == 'gb':
            # Correction for G flat major
            scale[scale.index('B')] = 'Cb'

        # F Sharp correction
        if self.root == 'f#':
            scale[scale.index('F')] = 'E#'

        return scale


class Minor(DiatonicScale):

    def __init__(self, root='a'):
        super(Minor, self).__init__(root=root, major=False, use_flats=['c', 'd', 'f', 'g'], formula=MINOR_SCALE_FORMULA)

    def scale(self):

        scale = super(Minor, self).scale()
        if self.root == 'eb':
            scale[scale.index('b')] = 'cb'
        return scale

    def __str__(self):
        return ' '.join(self.scale())


if __name__ == "__main__":

    d = Major('d')
    print(d)
    print(d.relative)
    b_minor = Minor(root='b')
    print(b_minor)

    dmin = Minor(root='d')
    print(dmin)

    fmaj = Major('F')
    print(fmaj.root)
    fmaj.root = 'F'
    print(fmaj.root)

    ebmajor = Major('eb')
    print(ebmajor)

    fs = Major(root='f#')
    print(fs)