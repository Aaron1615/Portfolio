class sequence(object):
    """Sequence object can be either DNA, RNA, or Protein"""

    def __init__(self, data, name):
        self.D_nucleotides = {
            "A":"Adenine",
            "T":"Thymine",
            "G":"Guanine",
            "C":"Cytosine" 
        }
        self.R_nucleotides = {
            "A":"Adenine",
            "U":"Uracil",
            "G":"Guanine",
            "C":"Cytosine" 
        }
        self.RNA_to_amino_acid = {}
        self.amino_acids = {
            "A":"ala", "R":"arg", "N":"asn", "D":"asp", 
            "Y":"tyr", "C":"cys", "E":"glu", "Q":"gln",
            "G":"gly", "V":"val", "H":"his", "I":"ile", 
            "L":"leu", "K":"lys", "M":"met", "F":"phe", 
            "P":"pro", "S":"ser", "T":"thr", "W":"trp", 
        } 
        # check to see that the type is DNA,RNA,or PROTEIN, if not raise an error
        if name.upper() == "DNA" or name.upper() == "RNA" or name.upper() == "PROTEIN":
            self.seq_type = name.upper()    
        else:
            raise TypeError("name argument must be DNA, RNA, PROTEIN, or None")
        #Check to ensure each sequence has proper subunits.
        self.check_sequence(data)

    

    def is_DNA(self,data):
        if self.seq_type == "DNA":
            for nucleotide in data:
                if not(nucleotide in self.D_nucleotides):
                    return False
            return True
        else:
            return False 

    def is_RNA(self,data):
        if self.seq_type == "RNA":
            for nucleotide in data:
                if not(nucleotide in self.R_nucleotides):
                    return False
            return True
        else:
            return False 

    def is_protein(self,data):
        if self.seq_type == "PROTEIN":
            for amino_acid in data:
                if not(amino_acid in self.amino_acids):
                    return False 
            return True
        else:
            return False

    def check_sequence(self,data):
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
        if self.seq_type == "PROTEIN":
            return "-".join([self.amino_acids[x] for x in self.seq])

        else:
            return self.seq

