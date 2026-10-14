# Code Practice

Personal Python coding and object-oriented design practice.

## Design Persistent Key-Value Store

- [Original question](OOD/original_question.md): the supplied problem statement, API, constraints, and examples.
- [My answer](OOD/persistent_kv_store.py): my latest independently rewritten implementation, exported unchanged from the notebook. Includes the supplied example runners.
- [Practice notebook](OOD/persistent_kv_store_practice.ipynb): the original question, guided exercises, earlier attempts, and my rewrite.

The store saves string keys and values in a custom binary snapshot using UTF-8 byte lengths and restores them through the provided Medium abstraction.

## Run

Use Python 3.12 or newer. The standalone answer uses only the standard library:

```sh
python3 OOD/persistent_kv_store.py
```

The bundled example runners print actual results and expected-value comments; they are not assertion-based tests.

For notebook editing, open this folder in VS Code with its Python and Jupyter extensions. Select the Python environment in `OOD/.venv`, or create one:

```sh
python3 -m venv OOD/.venv
OOD/.venv/bin/python -m pip install ipykernel
```

## Scope

The implementation assumes complete, valid snapshots. Corrupted-data validation, concurrent access, and crash-safe storage are follow-up topics. The supplied InMemoryMedium demonstrates the interface; its contents do not survive process restarts.

## Source

The question is preserved from the problem statement supplied during practice. The original question-bank URL has not been recorded. Interview metadata is reproduced as supplied, not independently verified. The practice notebook includes AI-assisted explanations and scaffolding.
