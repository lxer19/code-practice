# Code Practice

Personal interview preparation organized by technical topic and problem pattern. Company names such as OpenAI are metadata/tags in each problem's `notes.md`, rather than directories. A problem can have multiple company tags in its `companies` list without duplicating its solution.

## Structure

```text
code-practice/
├── algorithms/
├── ood/
│   ├── persistent_kv_store/
│   │   ├── question.md
│   │   ├── solution.py
│   │   ├── practice.ipynb
│   │   └── notes.md
│   ├── ttl_cache/
│   └── lru_cache/
├── ml_coding/
├── debugging/
└── README.md
```

- `algorithms/`: algorithm and data-structure patterns.
- `ood/`: object-oriented design problems.
- `ml_coding/`: machine-learning coding exercises.
- `debugging/`: debugging exercises.

Empty folders contain `.gitkeep` placeholders so Git tracks the intended structure. Each problem folder groups its question, solution, practice notebook, and notes. Notes use YAML front matter for `topic`, `patterns`, `companies`, and `status`.

## Persistent Key-Value Store

- [Question](ood/persistent_kv_store/question.md): the supplied problem statement, API, constraints, and examples.
- [My answer](ood/persistent_kv_store/solution.py): my independently rewritten implementation, preserved unchanged. Includes the supplied example runners.
- [Practice notebook](ood/persistent_kv_store/practice.ipynb): the original question, guided exercises, earlier attempts, and my rewrite.
- [Notes](ood/persistent_kv_store/notes.md): pattern and company metadata, constraints, documented format, and follow-up topics.

The store saves string keys and values in a custom binary snapshot using UTF-8 byte lengths and restores them through the provided Medium abstraction.

## Run

Use Python 3.12 or newer. The standalone answer uses only the standard library:

```sh
python3 ood/persistent_kv_store/solution.py
```

The bundled example runners print actual results and expected-value comments; they are not assertion-based tests.

For notebook editing, open this repository folder in VS Code with its Python and Jupyter extensions. Select the existing local environment in `ood/.venv`, or create one:

```sh
python3 -m venv ood/.venv
ood/.venv/bin/python -m pip install ipykernel
```

Python environments and local editor settings are excluded from Git.

## Scope

The implementation assumes complete, valid snapshots. Corrupted-data validation, concurrent access, and crash-safe storage are follow-up topics. The supplied InMemoryMedium demonstrates the interface; its contents do not survive process restarts.

## Source

The question is preserved from the problem statement supplied during practice. The original question-bank URL has not been recorded. Interview metadata is reproduced as supplied, not independently verified. The practice notebook includes AI-assisted explanations and scaffolding.
