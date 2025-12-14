banks = [line for line in open(0)]
total = 0
pick = 12
for bank in banks:
    stack = []
    N =len(bank)
    to_remove = N - pick
    for battery in bank:
        while stack and to_remove>0 and stack[-1] < battery:
            stack.pop()
            to_remove -=1
        stack.append(battery)
        
    if to_remove>0:
        stack = stack[:-to_remove]
    joltages  = stack[:pick]
    
    print(''.join(joltages ))
    total += int(''.join(joltages ))
print(total)

# import sys

# # banks = [[int(n) for n in line] for line in sys.stdin.read().strip().splitlines()]

# PICK = 12
# total = 0

# for bank in banks:
#     n = len(bank)
#     to_remove = n - PICK
#     stack = []
#     for battery in bank:
#         while stack and to_remove > 0 and stack[-1] < battery:
#             stack.pop()
#             to_remove -= 1
#         stack.append(battery)
#     if to_remove > 0:
#         stack = stack[:-to_remove]
#     joltages = stack[:PICK]
#     total += int("".join(map(str, joltages)))
    
# print(total)