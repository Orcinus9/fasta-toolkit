import argparse
from Bio import SeqIO

from fasta_toolkit.parser_utils import load_fasta_records, find_duplicate_headers
from fasta_toolkit.stats import fasta_summary, per_sequence_gc
from fasta_toolkit.filters import filter_by_min_length, reverse_complement_records
from fasta_toolkit.report import write_csv_report

def main():
    parser = argparse.ArgumentParser(
        description="FASTA Toolkit: summary, GC content, duplicate header check, filtering, reverse complement, and CSV report."
    )

    parser.add_argument("input", help="Path to input FASTA file")
    parser.add_argument("--summary", action="store_true", help="Print FASTA summary statistics")
    parser.add_argument("--gc", action="store_true", help="Print per-sequence GC content")
    parser.add_argument("--duplicates", action="store_true", help="Find duplicate sequence headers")
    parser.add_argument("--filter-min", type=int, help="Filter sequences shorter than this length")
    parser.add_argument("--revcomp", action="store_true", help="Write reverse complemented sequences")
    parser.add_argument("--report", help="Write CSV report to output path")
    parser.add_argument("--out", help="Output FASTA file for filtered or reverse-complemented sequences")

    args = parser.parse_args()
    records = load_fasta_records(args.input)

    if args.summary:
        summary = fasta_summary(records)
        print("\nFASTA Summary")
        for key, value in summary.items():
            print(f"{key}: {value}")

    if args.gc:
        print("\nPer-sequence GC content")
        for row in per_sequence_gc(records):
            print(f'{row["id"]}\tlength={row["length"]}\tgc={row["gc_percent"]}%')

    if args.duplicates:
        duplicates = find_duplicate_headers(records)
        print("\nDuplicate headers")
        if duplicates:
            for item in duplicates:
                print(item)
        else:
            print("No duplicate headers found")

    modified_records = records

    if args.filter_min is not None:
        modified_records = filter_by_min_length(modified_records, args.filter_min)
        print(f"\nFiltered sequences retained: {len(modified_records)}")

    if args.revcomp:
        modified_records = reverse_complement_records(modified_records)
        print(f"\nReverse complemented sequences generated: {len(modified_records)}")

    if args.out:
        SeqIO.write(modified_records, args.out, "fasta")
        print(f"\nOutput written to: {args.out}")

    if args.report:
        summary = fasta_summary(records)
        gc_stats = per_sequence_gc(records)
        duplicates = find_duplicate_headers(records)
        write_csv_report(summary, gc_stats, duplicates, args.report)
        print(f"\nCSV report written to: {args.report}")