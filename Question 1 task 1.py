#assignment 2 question 1

#These lines import the csv module for working with CSV files and the os module for interacting with the operating system
import csv
import os

#This line defines a function named extract_csv_to_text that takes two parameters: csv_folder (the folder containing CSV files) and output_text_file (the name of the output text file)
def extract_csv_to_text(csv_folder, output_text_file):
    
    all_rows = [] #this will create an empty list to store rows from all CSV files

    # This line starts a loop that iterates through all files in the specified folder (csv_folder) using os.listdir.
    for filename in os.listdir(csv_folder):
        if filename.endswith(".csv"): #this checks if the file is a .csv file
            csv_path = os.path.join(csv_folder, filename)
            
            # This line opens the CSV file in read mode ('r') using a with statement, ensuring that the file is properly closed after reading.
            with open(csv_path, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader: #This loop iterates through each row in the CSV file and appends the row to the all_rows list.
                    all_rows.append(row)

    # this block writes the combined rows to the output text file
    with open(output_text_file, 'w') as text_file:
        for row in all_rows:
            # This loop iterates through each row in the all_rows list, converts the row to a string by joining its elements with commas, and writes it to the output text file followed by a newline
            text_file.write(','.join(row) + '\n')

# This block specifies the folder containing CSV files (csv_folder) and the name of the output text file (output_text_file).
csv_folder = "M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\csv"
output_text_file = "M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\csv1.txt"

# Call the function to extract CSV to text
extract_csv_to_text(csv_folder, output_text_file)

