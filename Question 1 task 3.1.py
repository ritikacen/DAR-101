#assignment 2 question 3.1 with csv
import csv
from collections import Counter
import re
import os

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
    return word_counts

def list_top_words(word_counts, n=30):
    top_words = word_counts.most_common(n)
    return top_words

def write_to_csv(top_words, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])
        csv_writer.writerows(top_words)

def main():
    file_path = "M:\\WEDS01\Semester 3 2023\HIT137\Assignment 2\csv1.txt"  
    csv_file_path = 'M:/WEDS01/Semester 3 2023/HIT137/Assignment 2/top_words.csv'

    word_counts = count_words(file_path)
    top_words = list_top_words(word_counts)

    print(f"Top {len(top_words)} most common words:")
    for word, count in top_words:
        print(f"{word}: {count}")

    write_to_csv(top_words, csv_file_path)
    print(f"Top words written to {csv_file_path}")

if __name__ == "__main__":
    main()
