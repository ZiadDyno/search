# Repository Guidelines

## Project Structure & Module Organization
This repository is the UC Berkeley Pacman Search project (Python). Core engine and helpers live in `pacman.py`, `game.py`, `util.py`, plus graphics in `graphicsDisplay.py`/`graphicsUtils.py` and human/ghost controllers in `keyboardAgents.py`/`ghostAgents.py`. Student implementations go in `search.py` (search algorithms) and `searchAgents.py` (problems + heuristics). Board layouts sit in `layouts/*.lay`. Autograding harness is `autograder.py`, with fixtures in `test_cases/q1`-`q8` and shared runners in `searchTestClasses.py`/`testClasses.py`. Avoid committing generated artifacts beyond `__pycache__/`.

## Build, Test, and Development Commands
- `python autograder.py --no-graphics`: run the full public suite headless.
- `python autograder.py -q q3 --no-graphics`: grade a single question.
- `python autograder.py -t test_cases/q4/astar_0.test --no-graphics`: execute one test file to isolate a failure.
- `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0`: manual BFS sanity check.
- `python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0 -z 0.5`: manual A* + heuristic run with faster frames.

## Coding Style & Naming Conventions
Follow PEP 8 with 4-space indents and readable 80-100 char lines. Keep logic deterministic (the autograder seeds randomness). Use the provided data structures in `util.py` (`Stack`, `Queue`, `PriorityQueue`) rather than new dependencies. Functions remain snake_case, classes CamelCase; heuristics should end with `Heuristic` and accept `(state, problem)` to match calls. Only edit sections marked `*** YOUR CODE HERE ***`; preserve docstrings and signatures so the autograder can import modules cleanly.

## Testing Guidelines
Prefer headless runs with `--no-graphics` to avoid rendering overhead. When a question fails, open the matching `.test`/`.solution` in `test_cases/qN` to see the expected path length or explored states. Validate heuristics by comparing reported path cost from `pacman.py` to autograder expectations. Aim for passing public suites before attempting custom layouts; keep temporary traces (print/logging) local and remove before submission.

## Commit & Pull Request Guidelines
Use short, imperative summaries keyed to the question, e.g., `q3: implement uniform cost search` or `q7: add corners heuristic`. Describe the algorithmic change and any assumptions; list commands run (autograder invocations, manual `pacman.py` tests). Link to assignment prompts or issue IDs if available. Screenshots are optional unless you modify graphics or keyboard controls; otherwise, include failing-to-passing evidence from the relevant autograder question.

## Iterative Deepening DFS Notes
- `search.py` adds `iterativeDeepeningSearch` (alias `iddfs`) and a depth-limited helper, both with optional `max_depth` caps (default 1000 or `None` for unbounded). Runs report depth found plus total expansions.
- `searchAgents.py` forwards a `maxDepth` argument to any search taking `max_depth` and exposes `IterativeDeepeningAgent` as a shortcut wrapper.
- `pacman.py` accepts `--maxDepth` to pass depth limits from the CLI; leave unset to use agent defaults.
- Example run: `python pacman.py -p SearchAgent -a fn=iddfs,maxDepth=200 --layout mediumMaze --frameTime 0` (prints status if the cap is too low).
- Depth-limited DFS is runnable directly via `fn=dldfs`; it uses `maxDepth` as the limit, prints DLDFS metrics, and returns the DFS-ordered path at that cap (not necessarily optimal).

## Report Folder
- Former "AI Report" directory is now `report/`; contents: `report.tex` plus placeholder logos `engineering_logo_placeholder.jpg` and `university_logo_placeholder.png` used on the title page.
- `report.tex` now embeds full code for `depth_limited_dfs` and `iterativeDeepeningSearch` with step-by-step explanations, standalone DLDFS output, an evaluation comparing DLDFS vs IDDFS (time and node counts), plus CLI usage and algorithm comparisons; team names and presenters are on the title page via `\today`.
- Replace placeholder logos with real assets before final export; compile with `pdflatex report/report.tex` (listings/geometry/hyperref already included).
