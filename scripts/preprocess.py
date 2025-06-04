import os
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

input_dir = "20_newsgroups"
output_file = "dataset/cleaned_data.txt"

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

with open(output_file, 'w', encoding='utf-8') as outfile:
    doc_id = 0
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                cleaned = clean_text(content)
                outfile.write(f"{doc_id}\t{cleaned}\n")
                doc_id += 1

print("Preprocessing Done.")
