# AI Agent

This repository is a guided project based on the Boot.dev course "Build an AI Agent in Python". It provides a lightweight AI agent toolkit for programmatic file and code operations and follows the course exercises and learning path.

A lightweight AI agent toolkit for programmatic file and code operations. This repository provides small, focused functions to read, write, inspect, and execute Python files, plus a simple CLI harness and test suite to validate behavior.

**Key features**
- **File operations:** read and write file contents programmatically.
- **Workspace inspection:** list and inspect files and metadata.
- **Execution helper:** run Python files in a controlled subprocess.
- **Prompts & integration:** configurable prompt templates for conversational or agent-driven workflows.
- **Tests:** unit tests that demonstrate and validate the core behaviors.

**Getting Started**

- **Prerequisites:** Python 3.10+ and Git.
- **Clone:** `git clone https://github.com/mmuchsin/ai-agent.git`
- **Create virtualenv:** `python -m venv .venv && source .venv/bin/activate`
- **Install dependencies:** if a dependency manager is provided use it (for example `pip install -e .` or `pip install -r requirements.txt`).

**Quick Usage**

- Run the main CLI (example):

```bash
python main.py
```

**Project files of interest**
- `pyproject.toml`: project metadata and declared dependencies (requires Python >= 3.12).
- `uv.lock`: lockfile for the `uv` package manager (included for reproducible installs).
- `prompts.py`: system and prompt templates used by the agent.
- `functions/`: implementations for `get_file_content`, `get_files_info`, `run_python_file`, and `write_file`.

**Using uv (recommended)**

This project includes a `uv.lock` file and is compatible with the `uv` Python package manager. If you prefer `uv` over `pip` or `pipx`, install `uv` and sync dependencies from the lockfile.

Example (install `uv` with `pipx` and sync):

```bash
pipx install uv
uv sync
```

For full installation options and platform-specific instructions, see the official `uv` docs:

https://docs.astral.sh/uv/getting-started/installation/

If you do not use `uv`, install dependencies with pip or your preferred tool:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Run with uv**

Once dependencies are synced with `uv`, use `uv run` to execute the CLI or tests inside the project environment.

Run the CLI (two forms shown — some shells require `--` to separate `uv` args):

```bash
uv run python main.py "Calculate 3 + 5" --verbose
# or, if your shell needs it:
uv run -- python main.py "Calculate 3 + 5" --verbose
```

Run tests with `uv`:

```bash
uv run pytest -q
# or a single test file:
uv run pytest test_get_file_content.py -q
```

- Run the package tests with pytest:

```bash
pip install -U pytest
pytest -q
```

**Repository layout**
- **functions/**: core function implementations used by the agent (file I/O and execution helpers).
- **calculator/**: example package and helper scripts used by tests and demos.
- **test_*.py**: top-level test files validating integration and behavior.
- **main.py, call_function.py, prompts.py, config.py**: CLI and orchestration helpers.

**Project tree (approximate)**

```text
ai-agent/
├─ .env.example
├─ LICENSE
├─ README.md
├─ pyproject.toml
├─ uv.lock
├─ call_function.py
├─ config.py
├─ main.py
├─ prompts.py
├─ test_get_file_content.py
├─ test_get_files_info.py
├─ test_run_python_file.py
├─ test_write_file.py
├─ functions/
│  ├─ get_file_content.py
│  ├─ get_files_info.py
│  ├─ run_python_file.py
│  └─ write_file.py
└─ calculator/
	├─ lorem.txt
	├─ main.py
	├─ README.md
	├─ tests.py
	└─ pkg/
		├─ calculator.py
		├─ morelorem.txt
		└─ render.py
```

**Development**

- Run a single test file:

```bash
pytest tests/test_file_name.py -q
```

- Add new functions under `functions/` and add matching unit tests.

**Contributing**

- Open an issue to discuss major changes or features.
- Create a branch for your work, add tests, and submit a pull request.

**Support**

- For questions or issues, open a [GitHub issue](https://github.com/mmuchsin/ai-agent/issues).
- For course-specific help, refer to the [Boot.dev course](https://www.boot.dev/courses/build-ai-agent-python).
- For general AI agent concepts, check the course materials and project documentation.

**Project Status**

This is a guided learning project based on the Boot.dev course "Build an AI Agent in Python". It is maintained for educational purposes and demonstrates fundamental AI agent patterns using OpenRouter/OpenAI APIs. The project structure follows the course curriculum.

**License**

[MIT](LICENSE) — See [LICENSE](LICENSE) file for details.

**Course Reference & Attribution**

This project is implemented as part of the Boot.dev guided course: [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python). The exercises, project structure, and learning objectives are derived from that course. This repository is intended for learning and experimentation—please refer to the course for the canonical curriculum and full exercise instructions.

**Learning Goals**

- Understand the basic architecture of an AI agent (prompting, action loop, environment).
- Implement programmatic file operations and safe execution helpers.
- Build and run tests to validate agent behaviors and integrations.
- Experiment with prompt templates and simple orchestration flows.

**Project Overview**

- **Purpose:** A Boot.dev guided project that implements a small LLM-driven agent for learning how to inspect a workspace, read and write files, and execute Python scripts in a controlled environment.
- **Repository:** https://github.com/mmuchsin/ai-agent
- **Entry points:** `main.py` (CLI + OpenRouter/OpenAI client), `call_function.py` (maps LLM tool calls to local helpers).
- **Prompts:** `prompts.py` provides the system prompt used to guide the agent's behavior.
- **Core capabilities (tools):** `get_files_info`, `get_file_content`, `run_python_file`, `write_file` (implemented in `functions/`).
- **Example workspace:** `calculator/` contains a small calculator app used by tests and tool-call examples.

**Developer Notes**

- **Working directory / sandbox:** Each function validates that target paths are contained within a declared `working_directory` (via `os.path.commonpath`). `call_function.py` currently injects `working_directory="./calculator"` for tool calls — change this there if you need a different sandbox.
- **Limits & safety:** File reads are truncated at `MAX_CHARS` (see `config.py`, default 10000). `run_python_file` enforces a 30s timeout and only executes files ending with `.py`.
- **Adjusting behavior:** Change `MAX_CHARS` in `config.py` or the subprocess timeout in `functions/run_python_file.py` as needed for development experiments.
- **Security warning:** These helpers perform basic containment checks but do not fully sandbox untrusted code. Do NOT expose this agent to untrusted LLM outputs or untrusted users without additional isolation (containers, sandboxes, strict permissioning).
- **Testing:** Top-level `test_*.py` scripts exercise each function against the example `calculator/` workspace. Use these for local validation and as templates for new tests.
- **Environment:** `main.py` expects `OPENROUTER_API_KEY` (see `.env.example`). Keep real secrets out of source control and add `.env` to `.gitignore`.



