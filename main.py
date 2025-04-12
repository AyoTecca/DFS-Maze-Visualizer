import pygame
pygame.mixer.init()
import sys
import time
from maze import generate_maze, reset_visited, get_exit_cell, ROWS, COLS
from visualizer import (
    draw_maze,
    draw_cell,
    play_sound,
    step_sound,
    found_sound,
    reverse_sound,
    ORANGE,
    GREEN,
    BLUE,
    RED,
    TILE_SIZE,
    draw_buttons
)

pygame.init()

WIDTH, HEIGHT = 900, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DFS Maze Visualization")

DIFFICULTY = 0.3

maze = generate_maze(DIFFICULTY)
visited = reset_visited()
exit_cell = get_exit_cell()
final_path = []
steps_taken = 0
found_exit = False
started = False
start_cell = None
start_time = 0
solve_time = 0
search_finished = False


def dfs(x, y, path):
    global found_exit, steps_taken, final_path, solve_time, search_finished

    if found_exit or not (0 <= x < ROWS and 0 <= y < COLS):
        return
    if visited[x][y] or maze[x][y] == 0:
        return

    visited[x][y] = True
    path.append((x, y))
    steps_taken += 1

    draw_cell(win, x, y, ORANGE)
    play_sound(step_sound)
    update_info_panel()
    pygame.time.delay(150)

    if (x, y) == exit_cell:
        found_exit = True
        final_path = path.copy()
        solve_time = time.time() - start_time
        play_sound(found_sound)
        for px, py in final_path:
            draw_cell(win, px, py, GREEN)
            pygame.time.delay(120)
        draw_cell(win, exit_cell[0], exit_cell[1], BLUE)
        update_info_panel()
        return

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        dfs(x + dx, y + dy, path)

    if not found_exit:
        draw_cell(win, x, y, RED)
        play_sound(reverse_sound)
        pygame.time.delay(130)

    path.pop()

    if len(path) == 0 and not found_exit:
        search_finished = True
        update_info_panel()


def update_info_panel():
    font = pygame.font.SysFont(None, TILE_SIZE)
    pygame.draw.rect(win, (0, 0, 0), (610, 10, 180, 100))

    text = font.render("Steps: " + str(steps_taken), True, (255, 255, 255))
    win.blit(text, (610, 50))

    difficulty_label = ""
    if DIFFICULTY == 0.2:
        difficulty_label = "Easy"
    elif DIFFICULTY == 0.3:
        difficulty_label = "Medium"
    elif DIFFICULTY == 0.5:
        difficulty_label = "Hard"

    d_text = font.render("Difficulty: " + difficulty_label, True, (255, 255, 255))
    win.blit(d_text, (610, 10))

    if search_finished and not found_exit:
        t_text = font.render("No path found", True, (255, 100, 100))
        win.blit(t_text, (610, 80))
    elif started and not found_exit:
        t_text = font.render("Searching...", True, (255, 255, 0))
        win.blit(t_text, (610, 80))

    if found_exit:
        t_text = font.render("Time: {:.2f}s".format(solve_time), True, (255, 255, 255))
        win.blit(t_text, (610, 80))

    pygame.display.update(pygame.Rect(610, 10, 180, 100))


def reset():
    global visited, final_path, steps_taken, found_exit, started, solve_time, search_finished
    visited = reset_visited()
    found_exit = False
    steps_taken = 0
    final_path = []
    started = False
    solve_time = 0
    search_finished = False
    draw_maze(win, maze, exit_cell, steps_taken)
    draw_buttons(win)
    update_info_panel()


def regenerate_maze():
    global maze
    maze = generate_maze(DIFFICULTY)
    reset()


def main():
    global started, start_cell, DIFFICULTY, start_time
    reset()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                elif event.key == pygame.K_RETURN:
                    reset()
                elif event.key == pygame.K_n:
                    regenerate_maze()
                elif event.key == pygame.K_1:
                    DIFFICULTY = 0.2
                    regenerate_maze()
                elif event.key == pygame.K_2:
                    DIFFICULTY = 0.3
                    regenerate_maze()
                elif event.key == pygame.K_3:
                    DIFFICULTY = 0.5
                    regenerate_maze()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE

                if 610 <= x <= 790 and 100 <= y <= 140:
                    reset()
                elif 610 <= x <= 790 and 150 <= y <= 190:
                    regenerate_maze()
                elif 610 <= x <= 790 and 250 <= y <= 280:
                    DIFFICULTY = 0.2
                    regenerate_maze()
                elif 610 <= x <= 790 and 290 <= y <= 320:
                    DIFFICULTY = 0.3
                    regenerate_maze()
                elif 610 <= x <= 790 and 330 <= y <= 360:
                    DIFFICULTY = 0.5
                    regenerate_maze()
                elif not started and (0 <= row < ROWS and 0 <= col < COLS):
                    if maze[row][col] == 1:
                        start_cell = (row, col)
                        started = True
                        start_time = time.time()
                        dfs(row, col, [])

        pygame.display.update()


if __name__ == "__main__":
    main()
