# This py file will read a DNA sequence, then make an RNA sequence that will make the proteins
# todo try to find a way to figure out what protein is built


# table of amino acids
aminoAcids = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
              "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

# read file and convert to a string of upper case letters
read = open("sequence.txt")
sequence = read.read()
sequence.replace("\n", "")
sequence.replace("\r", "")
sequence = sequence.upper()

# make RNA string
rna = ""
for letter in sequence:
    if letter == 'A':
        rna = rna + "U"
    elif letter == 'T':
        rna = rna + "A"
    elif letter == 'C':
        rna = rna + "G"
    elif letter == 'G':
        rna = rna + "C"

length = len(rna)
for letters in range(0, length, 3):
    acid = rna[letters]
    acid = acid + rna[letters + 1]
    acid = acid + rna[letters + 2]
    print aminoAcids[acid]
read.close()
