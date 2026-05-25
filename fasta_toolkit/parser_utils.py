from Bio import SeqIO

def load_fasta_records(filepath):
    return list(SeqIO.parse(filepath, "fasta"))

def get_headers(records):
    return [record.id for record in records]

def find_duplicate_headers(records):
    seen = set()
    duplicates = set()

    for record in records:
        if record.id in seen:
            duplicates.add(record.id)
        seen.add(record.id)

    return sorted(list(duplicates))