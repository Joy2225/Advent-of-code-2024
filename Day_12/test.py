from collections import defaultdict

def calculate_total_price(grid):
    def get_neighbors(x, y):
        """Get valid neighbors of a cell (x, y)."""
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(nx, ny) for nx, ny in neighbors if 0 <= nx < rows and 0 <= ny < cols]

    def flood_fill(x, y, region_char):
        """Perform flood fill to identify the region and its properties."""
        stack = [(x, y)]
        visited.add((x, y))
        area = 0
        sides = 0

        while stack:
            cx, cy = stack.pop()
            area += 1

            for nx, ny in get_neighbors(cx, cy):
                if (nx, ny) not in visited:
                    if grid[nx][ny] == region_char:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                    else:
                        sides += 1
                else:
                    sides += 1

        return area, sides

    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                region_char = grid[i][j]
                area, sides = flood_fill(i, j, region_char)
                total_price += area * sides

    return total_price

# Grid input
grid = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]

# Calculate total price
result = calculate_total_price(grid)
print("Total Price:", result)
