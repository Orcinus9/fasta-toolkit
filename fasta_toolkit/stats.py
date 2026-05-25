def gc_content(sequence):
    seq = str(sequence).upper()
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)

def sequence_lengths(records):
    return [len(record.seq) for record in records]

def fasta_summary(records):
    lengths = sequence_lengths(records)

    if not lengths:
        return {
            "num_sequences": 0,
            "total_length": 0,
            "min_length": 0,
            "max_length": 0,
            "avg_length": 0,
            "n50": 0
        }

    return {
        "num_sequences": len(lengths),
        "total_length": sum(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "avg_length": round(sum(lengths) / len(lengths), 2),
        "n50": calculate_n50(lengths)
    }

def calculate_n50(lengths):
    if not lengths:
        return 0

    sorted_lengths = sorted(lengths, reverse=True)
    half_total = sum(sorted_lengths) / 2
    running_sum = 0

    for length in sorted_lengths:
        running_sum += length
        if running_sum >= half_total:
            return length

    return 0

def per_sequence_gc(records):
    results = []
    for record in records:
        results.append({
            "id": record.id,
            "length": len(record.seq),
            "gc_percent": gc_content(record.seq)
        })
    return results