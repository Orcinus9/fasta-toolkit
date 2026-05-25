from Bio.SeqRecord import SeqRecord

def filter_by_min_length(records, min_length):
    return [record for record in records if len(record.seq) >= min_length]

def reverse_complement_records(records):
    reversed_records = []

    for record in records:
        rc = record.reverse_complement(id=True, name=True, description=True)
        rc.id = f"{record.id}_revcomp"
        rc.description = f"reverse_complement_of_{record.id}"
        reversed_records.append(rc)

    return reversed_records