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

# 🚀 How to Execute the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/mhdmusharraf/DocumentSimilarity-Hadoop.git
cd DocumentSimilarity-Hadoop
```

## 2️⃣ Setup Python Virtual Environment (WSL)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> ⚠️ If `requirements.txt` is not available, install manually:

```bash
pip install nltk scikit-learn
python3 -m nltk.downloader stopwords
```

## 3️⃣ Dataset Preparation

- Download the **20 Newsgroups Dataset** from [Kaggle](https://www.kaggle.com/) and place it inside the `20_newsgroups/` folder.

- Run preprocessing to clean and prepare data:

```bash
python3 scripts/preprocess.py
```

✅ **Output file:** `dataset/cleaned_data.txt`

## 4️⃣ Package the Virtual Environment for Hadoop Streaming

```bash
tar -czvf venv.tar.gz venv
```

## 5️⃣ Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
jps  # verify all daemons are running (NameNode, DataNode, ResourceManager, NodeManager)
```

## 6️⃣ Upload Input Data to HDFS

```bash
hdfs dfs -mkdir /input
hdfs dfs -put dataset/cleaned_data.txt /input/
```

## 7️⃣ Run Hadoop Streaming Job

```bash
hdfs dfs -rm -r /output

$HADOOP_HOME/bin/yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files scripts/mapper.py \
-archives venv.tar.gz#venv \
-input /input \
-output /output \
-mapper "./venv/bin/python3 mapper.py" \
-reducer cat | tee logs/hadoop_job_log.txt
```

## 8️⃣ Collect Output from HDFS

```bash
hdfs dfs -cat /output/part-00000 > logs/output_raw.txt
```

## 9️⃣ Format Output with Header

```bash
{ printf "%-12s %-12s %-18s\n" "Document_1" "Document_2" "Cosine_Similarity"; cat logs/output_raw.txt; } > logs/output_final.txt
```

## 🔟 Verify Output

```bash
cat logs/output_final.txt
```
