def DNA_strand(dna):
    # code here
    ret = ""
    chars = [char for char in dna]
    for char in chars:
        if char == "A":
            ret += "T"
        elif char == "T":
            ret += "A"
        elif char == "G":
            ret += "C"
        else:
            ret += "G"
    return ret
