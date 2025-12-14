import math
def max_length(tuple_list):
    if math.floor(math.log10(tuple_list[0]))+1%2==0:
        return (math.floor(math.log10(tuple_list[0]))+1,tuple_list[0])
    if math.floor(math.log10(tuple_list[1]))+1%2==0:
        return (math.floor(math.log10(tuple_list[1]))+1,tuple_list[1])
    return (math.floor(math.log10(tuple_list[1])) ,tuple_list[1])

input_lines = open(0).read().strip()
range_ids = [list(map(int,line.split('-'))) for line in input_lines.split(",")]
for i in range_ids:
    half,first_half_start = max_length(i)
    print(i,half,first_half_start)
    half = half//2
    first_half_start = first_half_start//(10**half)
    # print(str(i[0])+'-'+str(i[1])+": ",end="")
    while first_half_start+first_half_start*(10**half) <= i[1]:
        if (math.floor(math.log10(first_half_start+first_half_start*(10**half)))+1)%2==0:
            print(first_half_start+first_half_start*(10**half),end=", ")
        first_half_start += 1
    print()





#solution submitted 1
# input_lines = open(0).read().strip()
# range_ids = [list(map(int,line.split('-'))) for line in input_lines.split(",")]
# numbers = sum(list(list(range(a,b+1))for a,b in range_ids),[])
# total = 0
# for num in numbers:
#     str_num = str(num)
#     half = len(str_num)//2
#     if str_num[:half] == str_num[half:]:
#         total += num
# print(total)






