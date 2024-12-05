with open('2.txt') as file:
    data = file.read().strip().split('\n')


grid = [list(row) for row in data]
word = "XMAS"

directions = [
    (0, 1),   # Horizontal (left to right)
    (0, -1),  # Horizontal (right to left)
    (1, 0),   # Vertical (top to bottom)
    (-1, 0),  # Vertical (bottom to top)
    (1, 1),   # Diagonal (top-left to bottom-right)
    (-1, -1), # Diagonal (bottom-right to top-left)
    (1, -1),  # Diagonal (top-right to bottom-left)
    (-1, 1)   # Diagonal (bottom-left to top-right)
]

rows = len(grid)
cols = len(grid[0])
ans = 0

def search_from(x, y, dx, dy):

    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
            return False
    
    return True

for r in range(rows):
    for c in range(cols):

        for dx, dy in directions:
            if search_from(r, c, dx, dy):
                ans += 1

print(ans)