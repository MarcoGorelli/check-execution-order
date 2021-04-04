[![Build Status](https://github.com/MarcoGorelli/check-execution-order/workflows/tox/badge.svg)](https://github.com/MarcoGorelli/check-execution-order/actions?workflow=tox)
[![Coverage](https://codecov.io/gh/MarcoGorelli/check-execution-order/branch/main/graph/badge.svg)](https://codecov.io/gh/MarcoGorelli/check-execution-order)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MarcoGorelli/check-execution-order/main.svg)](https://results.pre-commit.ci/latest/github/MarcoGorelli/check-execution-order/main)

check-execution-order
===========

A tool and pre-commit hook to automatically check execution order in Jupyter Notebooks.

<p align="center">
    <a href="#readme">
        <img alt="demo" src="https://raw.githubusercontent.com/nbQA-dev/nbQA-demo/master/check-execution-order.gif">
    </a>
</p>

## Installation

```console
$ pip install check-execution-order
```

## Usage as a pre-commit hook (recommended)

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/MarcoGorelli/check-execution-order
    rev: v0.1.0
    hooks:
    -   id: check-execution-order
```

## Command-line example

```console
$ check-execution-order bad.ipynb 
Cell 1 comes after 2 in file 'bad.ipynb'
```

## Configuration

None yet. Got any requests? Please let me know!
