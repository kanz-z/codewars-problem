def DNA_strand(dna):
    return "".join(["T" if i == "A" else "A" if i == "T" else "G" if i == "C" else "C" for i in dna])