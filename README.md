# FASTA Toolkit

A Python command-line toolkit for basic FASTA file analysis and preprocessing.

This project reads FASTA files and performs common bioinformatics tasks such as sequence summary statistics, GC-content calculation, duplicate header detection, reverse-complement generation, short-sequence filtering, and CSV report export.

## Features

- FASTA summary statistics
- GC-content calculation for each sequence
- Duplicate sequence header detection
- Sequence filtering by minimum length
- Reverse-complement generation
- CSV report export
- N50 calculation for contig statistics

## Why I built this

I built this project to strengthen my bioinformatics programming skills after completing my MSc, with a focus on Linux, Python, biological sequence parsing, and genomics-oriented data analysis.

The goal was to create a small but practical tool that demonstrates active learning in computational biology and shows my growing ability to work with real biological file formats.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Orcinus9/fasta-toolkit.git
cd fasta-toolkit
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Project structure

```text
fasta-toolkit/
├── main.py
├── README.md
├── requirements.txt
├── sample_data/
│   └── example.fasta
├── output/
└── fasta_toolkit/
    ├── __init__.py
    ├── cli.py
    ├── parser_utils.py
    ├── stats.py
    ├── filters.py
    └── report.py
```

## Example input

The repository includes a small test FASTA file in:

```text
sample_data/example.fasta
```

## Usage

### Show FASTA summary statistics

```bash
python main.py sample_data/example.fasta --summary
```

### Show GC content for each sequence

```bash
python main.py sample_data/example.fasta --gc
```

### Detect duplicate headers

```bash
python main.py sample_data/example.fasta --duplicates
```

### Filter short sequences and save output

```bash
python main.py sample_data/example.fasta --filter-min 13 --out output/filtered.fasta
```

### Generate reverse complements and save output

```bash
python main.py sample_data/example.fasta --revcomp --out output/revcomp.fasta
```

### Export CSV report

```bash
python main.py sample_data/example.fasta --report output/report.csv
```

## Output files

Depending on the command used, the toolkit can generate:

- Filtered FASTA files
- Reverse-complement FASTA files
- CSV summary reports

These outputs are written to the `output/` folder.

## Skills demonstrated

- Python programming
- Command-line interface development
- FASTA parsing using Biopython
- Modular code organization
- Basic genomics statistics
- Bioinformatics preprocessing workflows
- Reproducible project structure using Git and GitHub

## Future improvements

- Unit tests for core functions
- Support for compressed FASTA files
- Sequence validation warnings
- Plotting of sequence length distributions
