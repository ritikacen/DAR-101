# scispacy en_core_sci_sm 
import spacy
import scispacy
import os

# Load the en_core_sci_sm model
nlp = spacy.load("en_core_sci_sm")

with open("M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\csv1.txt", 'r') as file:
    text = file.read()

# Process the text with the spaCy pipeline
doc = nlp(text)

# Extract drugs and diseases
drugs = []
diseases = []

for ent in doc.ents:
    if ent.label_ == "CHEMICAL":
        drugs.append(ent.text)
    elif ent.label_ == "DISEASE":
        diseases.append(ent.text)

# Print the extracted drugs and diseases
print("Drugs:", drugs)
print("Diseases:", diseases)
