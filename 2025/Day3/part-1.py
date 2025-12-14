banks = [line for line in open(0)]
def find_jolts(battries:str)->int:
    jolts = float('-inf')
    for i in range(len(battries)):
        single_jolt = float('-inf')
        for j in range(i+1,len(battries)):
            single_jolt = max(single_jolt,int(battries[i]+battries[j]))
        jolts = max(jolts,single_jolt)
    return jolts
total = 0
for i in banks:
    total+=find_jolts(i)
print(total)
