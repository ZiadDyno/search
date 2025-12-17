# UC Berkeley Pacman Search (CS188) + IDDFS

This repository contains the UC Berkeley CS188 Pacman search project with added iterative deepening and depth-limited DFS support. Core engine code is kept intact; student-facing implementations live in the `Pacman` folder. Depth-limited DFS (`dldfs`) and iterative deepening DFS (`iddfs`) are implemented and exposed via the CLI.

## Repository Layout
- `Pacman/` — main project root (run all commands from here)
  - `pacman.py` — game harness and CLI (accepts `--maxDepth` for depth-limited agents)
  - `search.py` — DFS, BFS, UCS, A*, depth-limited DFS (`depthLimitedSearch`/`dldfs`), iterative deepening (`iterativeDeepeningSearch`/`iddfs`); `depth_limited_dfs` helper with metrics
  - `searchAgents.py` — problems, heuristics, and agents (includes `IterativeDeepeningAgent`; Corners/Food sections remain `*** YOUR CODE HERE ***` for assignment work)
  - Support files: `game.py`, `util.py`, `graphicsDisplay.py`, `graphicsUtils.py`, `keyboardAgents.py`, `ghostAgents.py`, `pacmanAgents.py`
  - Layouts: `layouts/*.lay`
  - Autograder: `autograder.py`, fixtures in `test_cases/q1`–`q8`, shared runners `searchTestClasses.py` / `testClasses.py`
  - Version marker: `Pacman/VERSION`
- `report/` — LaTeX report (`report.tex`) plus `report.pdf`; placeholder logos `engineering_logo_placeholder.jpg`, `university_logo_placeholder.png`

## Prerequisites
- Python 3 (no external packages required)
- Recommended: run commands from `Pacman/` (`cd Pacman`)
- Use `--no-graphics` for headless runs; graphics require a display

## Quickstart Commands
From inside `Pacman/`:
- Full public autograder: `python autograder.py --no-graphics`
- Single question: `python autograder.py -q q3 --no-graphics`
- Single test file: `python autograder.py -t test_cases/q4/astar_0.test --no-graphics`
- Manual BFS sanity check: `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0`
- Manual A* with Manhattan heuristic: `python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0 -z 0.5`
- Iterative deepening sample: `python pacman.py -p SearchAgent -a fn=iddfs,maxDepth=200 --layout mediumMaze --frameTime 0`
- Depth-limited DFS sample: `python pacman.py -p SearchAgent -a fn=dldfs,maxDepth=200 --layout mediumMaze --frameTime 0`

## Algorithms & Notes
- Implemented searches: `dfs`, `bfs`, `ucs`, `astar`, `dldfs`, `iddfs` (aliases provided)
- Depth limits: `maxDepth`/`max_depth` may be passed via CLI or agent args; `None` means unbounded (default 1000)
- Metrics: DLDFS/IDDFS print expansions and timing to stdout
- Heuristics: `manhattanHeuristic`, `euclideanHeuristic` included; custom heuristics belong in the `*** YOUR CODE HERE ***` sections

## Testing Guidance
- Prefer headless runs (`--no-graphics`) for speed
- When a test fails, inspect the matching `.test`/`.solution` under `Pacman/test_cases/qN`
- Compare `pacman.py` reported path costs with autograder expectations when tuning heuristics
- Remove any temporary print/debug output before submission

## Coding Conventions
- Follow PEP 8 (4-space indents, 80–100 char lines)
- Keep logic deterministic (autograder seeds randomness)
- Use provided data structures in `util.py` (`Stack`, `Queue`, `PriorityQueue`) instead of new dependencies
- Only edit regions marked `*** YOUR CODE HERE ***`; preserve docstrings and function signatures
- Avoid committing generated artifacts (e.g., `__pycache__/`, build outputs)

## Report
- `report/report.tex` documents the DLDFS/IDDFS additions, metrics, and usage; `report/report.pdf` is the current build
- Replace placeholder logos in `report/` before exporting the final PDF
- Compile with `pdflatex report/report.tex`

## License
Original UC Berkeley CS188 license applies (educational use; retain attribution and do not publish solutions).
