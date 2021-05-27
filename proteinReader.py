# This py file will read a RNA sequence and determine the amino acids built in the sequence.
# todo try to find a way to figure out what protein is built

class NucleicAcid:
    def __init__(self, data):
        self.a = None
        self.u = None
        self.c = None
        self.g = None
        self.data = data


def build_tree(root):
    acids = ["A", "U", "C", "G"]
    newRoot = NucleicAcid(root)
    count = 2
