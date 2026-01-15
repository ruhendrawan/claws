import csv
from pathlib import Path
from statistics import mean, median, stdev
from collections import defaultdict
from matplotlib import pyplot as plt

from s10x_settings import *



def load_scores_csv(path: str):
    scores = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ex = row["exercise_name"].strip()
            leaf = row["leaf"].strip()
            ontology = row.get("ontology", "").strip()
            score = int(row["score"])
            scores[ex].append((leaf, ontology, score))
    return scores

def compute_label_counts(scores, threshold=1, ontology="parser"):
    counts = []
    for ex, preds in scores.items():
        rec_labels = {leaf for (leaf, o, s) in preds if s >= threshold and o == ontology}
        counts.append(len(rec_labels))
    return counts

def compute_label_stats(counts):
    if not counts:
        return {}
    stats = {
        "n_exercises": len(counts),
        "min_labels": min(counts),
        "max_labels": max(counts),
        "mean_labels": mean(counts),
        "median_labels": median(counts),
        "stdev_labels": stdev(counts) if len(counts) > 1 else 0.0,
    }
    return stats



def plot_distribution(counts, title="Distribution of Recommended Labels per Exercise"):
    plt.figure(figsize=(7, 5))
    plt.hist(counts, bins=range(min(counts), max(counts)+2), edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Recommended Labels per Exercise")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()






if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATION IN s10x_settings.py


    # THRESHOLD = 5            # score >= threshold ⇒ predicted leaf present
    THRESHOLDS = [3, 4, 5]


    batch_data = []
    # batch_data = load_batch_ids()
    # batch_data = load_batch_splits_ids()
    batch_data += [COMBINED_STATS_ID]


    for batch_id in batch_data:
        SCORES_CSV_FILE = Path(CLAWS_OUTPUT_PATH) / f"scores/{batch_id}.csv"
        scores = load_scores_csv(SCORES_CSV_FILE)
        print(f"\nBatch: {batch_id}")

        for threshold in THRESHOLDS:
            counts = compute_label_counts(scores, threshold=threshold, ontology="parser")
            stats = compute_label_stats(counts)
            print(f"{batch_id} - Recommended Labels per Exercise (threshold={threshold}):")
            for k, v in stats.items():
                print(f"  {k}: {v}")

            plot_distribution(counts, title=f"{batch_id} - Recommended Labels per Exercise (threshold={threshold})")

        # combine into single plot with separate bars
        plt.figure(figsize=(7, 5))
        for threshold in THRESHOLDS:
            counts = compute_label_counts(scores, threshold=threshold, ontology="parser")
            plt.hist(counts, bins=range(min(counts), max(counts)+2), alpha=0.25, label=f"Threshold {threshold}", edgecolor="black")
        plt.xlabel("Number of Recommended Labels per Exercise")
        plt.ylabel("Frequency")
        plt.title(f"{batch_id} - Recommended Labels per Exercise (Combined Thresholds)")
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()
