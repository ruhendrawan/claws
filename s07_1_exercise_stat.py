import matplotlib.pyplot as plt
import numpy as np

from s10x_settings import *



def split_code_exercises(input_file):
    with open(input_file, 'r') as f:
        code_exercises = f.read()

    code_snippets = code_exercises.split('#CODE_SNIPPET')
    code_snippets = [s.strip() for s in code_snippets if s.strip()]

    # remove first three lines from each snippet
    #exercise type:
    #exercise name:
    #problem description:
    code_snippets = ['\n'.join(s.splitlines()[3:]).strip() for s in code_snippets if len(s.splitlines()) > 3]

    return code_snippets



def exercise_length_distribution(input_file, bin_size=50):
    code_snippets = split_code_exercises(input_file)
    lengths = [len(snippet) for snippet in code_snippets]
    max_len = max(lengths)
    bins = np.arange(0, max_len + bin_size, bin_size)
    plt.hist(lengths, bins=bins, edgecolor='black', alpha=0.7)
    plt.title("Distribution of Exercise Lengths")
    plt.xlabel("Length of exercise (characters)")
    plt.ylabel("Frequency")
    plt.show()
    return lengths



def exercise_comment_distributions(input_file, bin_size=10):
    code_snippets = split_code_exercises(input_file)

    # lengths in lines
    lengths = [snippet.count("\n") + 1 for snippet in code_snippets]

    # comment lines per snippet
    comment_counts = [
        sum(1 for line in snippet.splitlines() if line.strip().startswith("#"))
            for snippet in code_snippets
    ]

    # define bins
    max_len = max(lengths)
    max_comments = max(comment_counts)
    length_bins = np.arange(0, max_len + bin_size, bin_size)
    comment_bins = np.arange(0, max_comments + 1, 1)  # 1-step bins for comments

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(lengths, bins=length_bins, edgecolor='black', alpha=0.7)
    plt.title("Distribution of Exercise Lengths (lines)")
    plt.xlabel("Length of exercise (lines)")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(comment_counts, bins=comment_bins, edgecolor='black', alpha=0.7)
    plt.title("Distribution of Comment Lines per Exercise")
    plt.xlabel("Number of comment lines")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    return lengths, comment_counts



if __name__ == "__main__":

    # DON'T FORGET TO SET THE PARAMETERS IN s10x_settings.py


    lengths = exercise_length_distribution(PROMPT_INPUT_SNIPPET, bin_size=50)
    print(f"Processed {len(lengths)} code exercises.")
    print(f"Average length: {np.mean(lengths):.2f} characters.")
    print(f"Median length: {np.median(lengths)} characters.")
    print(f"Max length: {max(lengths)} characters.")
    print(f"Min length: {min(lengths)} characters.")

    lengths, comment_counts = exercise_comment_distributions(PROMPT_INPUT_SNIPPET, bin_size=10)
    print(f"Processed {len(comment_counts)} code exercises for comments.")
    print(f"Average comment lines: {np.mean(comment_counts):.2f}.")
    print(f"Median comment lines: {np.median(comment_counts)}.")
    print(f"Max comment lines: {max(comment_counts)}.")
    print(f"Min comment lines: {min(comment_counts)}.")