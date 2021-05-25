x = ["AAT","TTG","GGA","AUG","CCT","GTA","GCG","TAG","CCA","AAG","GGT","ACG","UAG","ATG","CCT","GAT","CGT"]
index_start = x.index('AUG')
index_stop = x.index('UAG')
for i in x:
    if i== "AUG":
       print("It is the start codon",'\n')
print("The index of AUG:",index_start)
for i in x:
    if i== "UAG":
        print("It is the stop codon",'\n')
print("The index of UAG:",index_stop)
for i in range(3,13):
    print(x[i])
