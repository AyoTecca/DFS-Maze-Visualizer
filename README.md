# 🧠 DFS Virtual Maze

A Python + Pygame project demonstrating Depth-First Search (DFS) traversal inside a **virtualized maze environment**.

This educational tool simulates how a DFS algorithm operates within an abstract, modular virtual space, helping students understand recursion, graph traversal, and the concept of virtualization in algorithm design.

---

## 🧠 What Makes It Virtual?

Unlike standard visualizations, this project introduces a **VirtualMaze** abstraction:

- Each maze cell is represented as a `VirtualCell` with attributes like `is_wall` and `visited`
- The DFS algorithm interacts with this virtual environment rather than a raw grid
- This simulates a **virtual execution layer**, similar to how operating systems virtualize memory or devices

---

## 🎮 Features

- ✅ DFS traversal inside a virtual environment (`VirtualMaze`)
- 🟦 UI labeled with mode: **“Virtual Maze”**
- 🔊 Sound feedback for step, backtrack, and goal detection
- 🟧 Clickable start-point selection
- 🧱 Dynamic maze generation with wall density (difficulty)
- 🧠 “No path found” indicator if DFS cannot reach the goal
- 🕒 Timer and step counter

---

## 🧱 VirtualMaze Architecture

Each `VirtualMaze` is a 2D grid of `VirtualCell` objects:

```
VirtualMaze
├── VirtualCell[0][0] → is_wall: False, visited: True
├── VirtualCell[0][1] → is_wall: True, visited: False
...
```

This allows the DFS algorithm to work within a simulated, modular graph space.

---

## 🎨 Color Legend

| Color  | Meaning               |
|--------|------------------------|
| ⚪ White | Walkable              |
| ⚫ Black | Wall / Blocked        |
| 🟧 Orange | Currently visiting   |
| 🟥 Red    | Backtracking         |
| 🟩 Green  | Path to exit         |
| 🔵 Blue   | Exit node            |

---

## 🧪 How to Run

```bash
git clone https://github.com/AyoTecca/DFS-Virtual-Maze.git
cd DFS-Virtual-Maze
pip install -r requirements.txt
python main.py
```

---

## ⌨️ Controls

| Action            | Control                        |
|-------------------|--------------------------------|
| Restart           | `R` or Restart Button          |
| New Maze          | `N` or New Maze Button         |
| Set Start Point   | Click any walkable tile        |
| Difficulty        | Keys `1` (Easy), `2` (Medium), `3` (Hard) |
| Exit              | Close the window or press `Ctrl+C` |

---

## 📁 Project Structure

| File           | Description                     |
|----------------|---------------------------------|
| `main.py`       | Core logic + virtualization     |
| `maze.py`       | Maze generation and parameters  |
| `visualizer.py` | UI rendering and sound effects  |
| `assets/`       | Sound files (`.wav`)            |
| `README.md`     | This file                       |

---

## 🙌 Credits

- Developed by [@AyoTecca](https://github.com/AyoTecca)
- Built with [Python](https://www.python.org/) and [Pygame](https://www.pygame.org/)