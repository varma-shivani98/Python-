seq1 = "AATGCCGTAGCTGA"
seq2 = "GGTGCCGTAGCGGA"
x = [i for i in range(len(seq1)) if seq1[i] != seq2[i]]
print("Positions at which seq1 is mutated : ",x)
y = [i for i in range(len(seq1)) if (seq1[i] == seq2[i])]
print("Positions at which seq1 is similiar to seq2: ",y)
