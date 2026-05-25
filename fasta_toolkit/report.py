import csv
import os

def write_csv_report(summary, per_seq_stats, duplicates, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Metric", "Value"])
        for key, value in summary.items():
            writer.writerow([key, value])

        writer.writerow([])
        writer.writerow(["Duplicate Headers"])
        if duplicates:
            for item in duplicates:
                writer.writerow([item])
        else:
            writer.writerow(["None"])

        writer.writerow([])
        writer.writerow(["Sequence ID", "Length", "GC Percent"])
        for row in per_seq_stats:
            writer.writerow([row["id"], row["length"], row["gc_percent"]])