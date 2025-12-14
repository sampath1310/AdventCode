grid = [list(line) for line in open(0).read().strip().split("\n")]
def get_adjacent(arr,x,y):
    directions = [(-1,0),(1,0),(0,-1),(0,1),(0,0),(-1,-1),(-1,1),(1,-1),(1,1)]
    cnt = 0
    for dx,dy in directions:
        nx,ny = x+dx,y+dy
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
            if arr[nx][ny] == '@':
                cnt += 1
    return cnt
total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue
            adj = get_adjacent(grid,i,j)
            if adj <= 4:
                total += 1      
print(total)