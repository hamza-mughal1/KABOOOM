import pygame
import csv

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Color for clicked cells

# Define grid dimensions
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 900
CELL_SIZE = 20
NUM_COLS = WINDOW_WIDTH // CELL_SIZE
NUM_ROWS = WINDOW_HEIGHT // CELL_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Clicker")

# Create a 2D list to store cell colors (initially white)
grid = [[WHITE for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# Function to draw the grid
def draw_grid():
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, grid[row][col], (x, y, CELL_SIZE, CELL_SIZE), 9)

# Main game loop
running = True
check = False
remove = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check = True

        elif event.type == pygame.MOUSEBUTTONUP:
            check = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                remove = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                remove = False       

    if check:
        pos = pygame.mouse.get_pos()  # Get mouse position
        cell_x, cell_y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        # Check if clicked within grid boundaries
        if 0 <= cell_x < NUM_COLS and 0 <= cell_y < NUM_ROWS:
            if remove:
                grid[cell_y][cell_x] = WHITE  # Change clicked cell to white
            else:
                grid[cell_y][cell_x] = GREEN  # Change clicked cell to green

    # Fill the background
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()



# with open('my_data.csv', 'w', newline='') as csvfile:  # Use 'w' for writing
#     writer = csv.writer(csvfile)
#     for i in grid:
#         row = []
#         for j in i:
#             if j == WHITE:
#                 row.append(0)
#             elif j == GREEN:
#                 row.append(1)
        
#         writer.writerow(row)




# Quit Pygame
pygame.quit()
