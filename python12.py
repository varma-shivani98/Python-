seq1="AATGCCGTAGTCGAATGCC"
seq2="ATTCTTTTGAAAAGGGGGC"
y = [i for i in range(len(seq1)) if (seq1[i] == seq2[i])]
print("Positions at which seq1 is similiar to seq2: ",y)
x=len(y)
percentage=(float(x)/19) * 100
print("Percentage similarity between two sequence: ",percentage,)
