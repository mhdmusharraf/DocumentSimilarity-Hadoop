# Document Similarity using Hadoop Streaming

---

## 📌 Project Title

**Document Similarity – Compute Cosine Similarity between Documents using Word Vectors**

---

## 📂 Dataset

- **Dataset Source:** [Kaggle - 20 Newsgroups Dataset](https://www.kaggle.com/datasets/crawford/20-newsgroups)
- The dataset contains text data from 20 different newsgroups which is widely used for text classification and NLP tasks.

---

## 🎯 Objective

The objective of this project is to:

- Build a text similarity system using cosine similarity.
- Process large-scale text data using **Hadoop Streaming** with **Python**.
- Use **TF-IDF (Term Frequency - Inverse Document Frequency)** for vector representation of documents.
- Calculate pairwise cosine similarity across documents.
- Run the entire solution in distributed fashion using **HDFS** and **YARN**.

---

## 🛠 Technologies Used

- **Hadoop 3.3.6 (Standalone Mode on WSL2 - Windows Subsystem for Linux 2)**
- **HDFS - Hadoop Distributed File System**
- **YARN - Yet Another Resource Negotiator**
- **Hadoop Streaming (for running Python scripts)**
- **Python 3.x**
- **Virtual Environment (venv) for package isolation**
- **scikit-learn** - for TF-IDF vectorization
- **nltk** - for text preprocessing (stopwords removal)
- **WSL2 (Ubuntu 24.04 on Windows 11)**

---

## 📑 Project Folder Structure

```bash
DocumentSimilarity-Hadoop/
│
├── 20_newsgroups/        # Raw dataset files (optional, downloaded from Kaggle)
├── dataset/              # Cleaned dataset after preprocessing
│   └── cleaned_data.txt
├── scripts/              # All Python source codes
│   ├── preprocess.py     # Dataset cleaning & preprocessing
│   └── mapper.py         # Hadoop Streaming mapper (cosine similarity calculation)
│   └── reducer.py        # (optional, not used in final version)
├── venv.tar.gz           # Packaged virtual environment for Hadoop Streaming
├── results/              # Sample output files (optional)
├── logs/                 # Hadoop job logs/screenshots (optional)
├── README.md             # Project documentation
└── .git/                 # Git repository

