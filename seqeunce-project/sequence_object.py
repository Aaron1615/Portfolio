class sequence(object):
    """Sequence object can be either DNA, RNA, or Protein"""

    def __init__(self, data, name):
        
        # Dictionary of DNA Nucleotide names, for quicker lookup and later usage
        self.D_nucleotides = {
            "A":"Adenine",
            "T":"Thymine",
            "G":"Guanine",
            "C":"Cytosine" 
        }
        # Dictionary of RNA Nucleotide names, for quicker lookup and later usage
        self.R_nucleotides = {
            "A":"Adenine",
            "U":"Uracil",
            "G":"Guanine",
            "C":"Cytosine" 
        }
        # Dictionary that converts any nucleotide type to RNA, for quick lookup.
        #Also useful for getting complementary strands of RNA, which may be implemented later.
        self.NA_to_RNA = {
            "A":"U",
            "T":"A",
            "U":"A",
            "G":"C",
            "C":"G"
        }
        # Dictionary that converts any nucleotide type to DNA, for quick lookup.
        # Also useful for getting complementary strands of DNA, which may be implemented later.
        # could also be used for a reverse transcription method.
        self.NA_to_DNA = {
            "A":"T",
            "T":"A",
            "U":"A",
            "G":"C",
            "C":"G"
        } 
        # Dictionary for converting RNA into amino acids.
        self.RNA_to_amino_acid = {
            "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
            "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
            "UAU":"Y", "UAC":"Y", "UAA":"0", "UAG":"0", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
            "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
            "UGU":"C", "UGC":"C", "UGA":"0", "UGG":"W", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
            "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"   
        }
        #Dictionary for showing 3 letter codes of amino acids. A more readable format for some.
        self.amino_acids = {
            "A":"ala", "R":"arg", "N":"asn", "D":"asp", 
            "Y":"tyr", "C":"cys", "E":"glu", "Q":"gln",
            "G":"gly", "V":"val", "H":"his", "I":"ile", 
            "L":"leu", "K":"lys", "M":"met", "F":"phe", 
            "P":"pro", "S":"ser", "T":"thr", "W":"trp",
            "0":"STOP", 
        } 
        # check to see that the type is DNA,RNA,or PROTEIN, if not raise an error
        if name.upper() == "DNA" or name.upper() == "RNA" or name.upper() == "PROTEIN":
            self.seq_type = name.upper()    
        else:
            raise TypeError("name argument must be DNA, RNA, PROTEIN, or None")
        #Check to ensure each sequence has proper subunits.
        self.check_sequence(data)

    

    def is_DNA(self,data):
        """This function takes in a string of values (data) and checks if the string 
        is DNA. Returns True or False"""
        if self.seq_type == "DNA":
            for nucleotide in data.upper():
                if not(nucleotide in self.D_nucleotides):
                    return False
            return True
        else:
            return False 

    def is_RNA(self,data):
        """This function takes in a string of values (data) and checks if the string 
        is RNA. Returns True or False"""
        if self.seq_type == "RNA":
            for nucleotide in data.upper():
                if not(nucleotide in self.R_nucleotides):
                    return False
            return True
        else:
            return False 

    def is_protein(self,data):
        """This function takes in a string of values (data) and checks if the string 
        is PROTEIN. Returns True or False"""
        if self.seq_type == "PROTEIN":
            for amino_acid in data:
                if not(amino_acid in self.amino_acids):
                    return False 
            return True
        else:
            return False

    def check_sequence(self,data):
        """Helper function used when creating sequence object. Ensures the 
        data of the object is the same type as the specified sequence type."""
        # May later add multiple object classes under sequence data type,
        #in which case this function can be used to determine type of sequence
        # for the user.
        if self.seq_type == "PROTEIN":
            if self.is_protein(data):
                self.seq = data.upper()
            else:
                raise TypeError("One or more errors in amino acid sequence")
        elif self.seq_type == "RNA":
            if self.is_RNA(data):
                self.seq = data.upper()
            else:
                raise TypeError("One or more errors in RNA sequence")
        else:
            if self.is_DNA(data):
                self.seq = data.upper()
            else:
                raise TypeError("One or more errors in DNA sequence")

    def __str__(self):
        """String function, modified for better looking Protein
        printing."""
        if self.seq_type == "PROTEIN":
            return "-".join([self.amino_acids[x] for x in self.seq])
        else:
            return self.seq
    def reverse_transcribe(self):
        """Converts an RNA sequence into a DNA sequence. Returns the new sequence and
        also changes the current object."""
        if self.seq_type != "RNA":
            raise TypeError("Only RNA can be Reverse-Transcribed")
        else:
            self.seq = list(self.seq)
            for index in range(len(self.seq)):
                self.seq[index] = self.NA_to_DNA[self.seq[index]]
            self.seq = "".join(self.seq)
            self.seq_type = "DNA"
            return self.seq

    def transcribe(self):
        """This function converts a DNA sequence into its complementary RNA sequence.
        Also changes the type of sequence to RNA. Returns the new sequence and also 
        changes the current object."""
        #Still a work in progress, would like to add ability to choose which strand
        #of DNA is transcribed.
        if self.seq_type != "DNA":
            raise TypeError("Only DNA can be Transcribed")
        else:
            self.seq = list(self.seq)
            for index in range(len(self.seq)):
                self.seq[index] = self.NA_to_RNA[self.seq[index]]
            self.seq = "".join(self.seq)
            self.seq_type = "RNA"
            return self.seq

    def translate(self):
        """This function converts the DNA or RNA sequence into a sequence of amino acids.
        Also changes the type of sequence to PROTEIN. Returns the new sequence and also 
        changes the current object."""
        #Still a work in progress, would like to add ability to choose which strand
        #of DNA is transcribed before translation occurs.
        #Also would like to add start and Stop codon functionality. 
        #May convert to a different method if that is the case.
        if self.seq_type == "PROTEIN":
            raise TypeError("This protein has already been translated")
        elif self.seq_type == "DNA":
            self.transcribe()
        codons = []
        codon = ""
        triple = 0
        for nucleotide in self.seq:
            if triple < 3:
                codon = codon + nucleotide
                triple += 1
            if triple >= 3:
                codons.append(codon)
                codon = ""
                triple = 0
        self.seq = ""
        for part in codons:
            self.seq = self.seq + self.RNA_to_amino_acid[part]
        self.seq_type = "PROTEIN"
        return self.__str__()

