# Repository Guidelines

## Project Structure & Module Organization
- Source lives under `Pacman/`; run commands from there. Core engine/helpers: `Pacman/pacman.py`, `Pacman/game.py`, `Pacman/util.py`; graphics: `Pacman/graphicsDisplay.py`, `Pacman/graphicsUtils.py`; human/ghost controllers: `Pacman/keyboardAgents.py`, `Pacman/ghostAgents.py`.
- Student work: `Pacman/search.py` (DFS/BFS/UCS/A*/DLDFS/IDDFS implemented) and `Pacman/searchAgents.py` (problems + heuristics; Corners/Food sections still marked `*** YOUR CODE HERE ***`).
- Layouts live in `Pacman/layouts/*.lay`. Autograder harness: `Pacman/autograder.py` with fixtures in `Pacman/test_cases/q1`-`q8` plus shared runners `Pacman/searchTestClasses.py`/`Pacman/testClasses.py`. Keep `Pacman/__pycache__/` and other generated artifacts out of commits; version marker in `Pacman/VERSION`.
- Report assets are in `report/` (TeX + PDF + placeholder logos). Avoid committing new build outputs outside this folder.

## Build, Test, and Development Commands
- `cd Pacman` before running tools.
- `python autograder.py --no-graphics`: run the full public suite headless.
- `python autograder.py -q q3 --no-graphics`: grade a single question.
- `python autograder.py -t test_cases/q4/astar_0.test --no-graphics`: execute one test file to isolate a failure.
- `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0`: manual BFS sanity check.
- `python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0 -z 0.5`: manual A* + heuristic with faster frames.
- IDDFS/DLDFS samples: `python pacman.py -p SearchAgent -a fn=iddfs,maxDepth=200 --layout mediumMaze --frameTime 0` and `python pacman.py -p SearchAgent -a fn=dldfs,maxDepth=200 --layout mediumMaze --frameTime 0` to see depth parsing + metrics.

## Coding Style & Naming Conventions
Follow PEP 8 with 4-space indents and readable 80-100 char lines. Keep logic deterministic (autograder seeds randomness). Use data structures from `util.py` (`Stack`, `Queue`, `PriorityQueue`) instead of new dependencies. Functions stay snake_case, classes CamelCase; heuristics end with `Heuristic` and accept `(state, problem)`. Only edit sections marked `*** YOUR CODE HERE ***`; preserve docstrings/signatures so autograder imports cleanly.

## Testing Guidelines
Prefer headless runs with `--no-graphics` to avoid rendering overhead. When a question fails, open the matching `.test`/`.solution` under `Pacman/test_cases/qN` to check expected path length or expansions. Validate heuristics by comparing `pacman.py` reported path cost to autograder expectations. Aim for passing public suites before custom layouts; remove temporary traces before submission.

## Commit & Pull Request Guidelines
Use short, imperative summaries keyed to the question (e.g., `q3: implement uniform cost search` or `q7: add corners heuristic`). Describe the algorithmic change and assumptions; list commands run (autograder invocations, manual `pacman.py` tests). Link assignment prompts/issues if available. Screenshots are optional unless graphics/controls change; otherwise include failing-to-passing evidence from the relevant autograder question.

## Iterative Deepening DFS Notes
- `search.py` provides `iterativeDeepeningSearch` (alias `iddfs`) and `depthLimitedSearch` (alias `dldfs`) built on `depth_limited_dfs`; both accept optional `max_depth` (`None` = unbounded, default 1000) and print expansions + timing.
- `searchAgents.py` forwards a `maxDepth` arg to any search that consumes `max_depth`/`limit` and exposes `IterativeDeepeningAgent` as a wrapper.
- `pacman.py` accepts `--maxDepth` to pass limits via agent args; leave unset to use search defaults.
- Example run: `python pacman.py -p SearchAgent -a fn=iddfs,maxDepth=200 --layout mediumMaze --frameTime 0` (prints status if the cap is too low). Depth-limited DFS direct: `python pacman.py -p SearchAgent -a fn=dldfs,maxDepth=200 --layout mediumMaze --frameTime 0`.

## Report Folder
- `report/report.tex` embeds full code for depth-limited DFS + IDDFS with explanations, standalone DLDFS output, an evaluation comparing DLDFS vs IDDFS (time and node counts), CLI usage, and algorithm comparisons; team names/presenters on the title page via `\today`.
- Placeholders `report/engineering_logo_placeholder.jpg` and `report/university_logo_placeholder.png` should be replaced with real assets before final export. Compile with `pdflatex report/report.tex`; `report/report.pdf` is the current build.
