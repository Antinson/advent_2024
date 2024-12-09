# Directions: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_map(input_map):
    grid = [list(row) for row in input_map.strip().split("\n")]
    start_pos = None
    start_dir = None

    # Find starting position and direction
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in "^>v<":
                start_pos = (r, c)
                start_dir = "^>v<".index(cell)
                grid[r][c] = "."
    return grid, start_pos, start_dir

def simulate(grid, start_pos, start_dir, obstruction=None):
    rows, cols = len(grid), len(grid[0])
    r, c = start_pos
    direction = start_dir
    visited = set()
    path = set()

    if obstruction:
        grid[obstruction[0]][obstruction[1]] = "#"

    while 0 <= r < rows and 0 <= c < cols:
        if (r, c, direction) in visited:
            break  # Loop detected
        visited.add((r, c, direction))
        path.add((r, c))

        dr, dc = DIRECTIONS[direction]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            r, c = nr, nc
        else:
            direction = (direction + 1) % 4  # Turn right

    if obstruction:
        grid[obstruction[0]][obstruction[1]] = "."
    return visited, path

def find_obstruction_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    _, initial_path = simulate(grid, start_pos, start_dir)

    valid_positions = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "." and (r, c) != start_pos:
                _, new_path = simulate(grid, start_pos, start_dir, obstruction=(r, c))
                if len(new_path) < len(initial_path):
                    valid_positions.add((r, c))
    return valid_positions

# Example Input
input_map = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# Parse the input map
grid, start_pos, start_dir = parse_map(input_map)

# Find valid obstruction positions
valid_positions = find_obstruction_positions(grid, start_pos, start_dir)

# Output the result
print(f"Number of valid positions: {len(valid_positions)}")
