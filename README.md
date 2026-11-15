# Dependency Trail

A small command-line tool for exploring dependency relationships in Python projects.

## What it does

- Reads dependency declarations from a project's `pyproject.toml`.
- Prints a clean, deterministic dependency report.
- Can export the discovered direct dependencies as JSON.
- Uses Python's standard library only.

## Quick start

```bash
python dependency_trail.py pyproject.toml
python dependency_trail.py pyproject.toml --json
```

## Scope

The first version focuses on direct dependencies declared in the project metadata. It does not install packages, execute project code, or claim to resolve the complete transitive environment.

## Development

Run the built-in tests with:

```bash
python -m unittest -v
```

## License

MIT
