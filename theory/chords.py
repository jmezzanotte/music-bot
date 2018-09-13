from theory import scales


class MajorTriad(scales.Major):

    def __init__(self, *args, **kwargs):
        super(MajorTriad, self).__init__(*args, **kwargs)

    def triad(self):
        return [self.tonic, self.mediant, self.dominant]

class MinorTriad(scales.Minor):
    pass


class DiminishedTriad(scales.Minor):

    """
    Logic behind building the Triad: 
    We build the dimished triad by first finding its parent minor scale. The parent minor 
    scale is that scale where the root of the dimished chord is the second scale degree. 
    For example, given root b for a dimished chord, the parent minor scale is a_minor. 
    From there we can create the triad by taking the second, fourth, and sixth scale 
    degrees. In order to do this properly, we need to overwrite the scale() method of 
    the parent minor class. The scale that is returned is that minor scale where the 
    given root is the second scale degree.
    """
    def __init__(self, *args, **kwargs):
        super(DiminishedTriad, self).__init__(*args, **kwargs)

    def scale(self):
        temp_root = self.chromatic_scale()[-scales.WHOLE_STEP]
        return scales.Minor(root=temp_root).scale()

    def triad(self):
        return [self.super_tonic, self.subdominant, self.submediant]

