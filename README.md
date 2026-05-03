# Parallel Text Handling Processor

This project focuses on analyzing large-scale text datasets using Natural Language Processing (NLP) and parallel processing techniques.  
It performs sentiment analysis on text data and visualizes the results for better understanding.

---

## 📌 Project Overview

Processing large text datasets sequentially can be slow.  
This project improves performance by using **parallel processing** to analyze text efficiently.

The system performs:
- Text cleaning using regex
- Sentiment analysis using NLP
- Parallel processing for faster execution
- Data visualization for insights

---

## 🧠 Problem Statement

Large datasets take significant time to process.  
This project solves:
- Slow processing of text data
- Difficulty in extracting insights from raw text
- Lack of scalable text analysis systems

---

## 🛠️ Technologies & Tools Used

### Programming Language
- Python

### Libraries
- Pandas
- TextBlob
- Matplotlib
- Seaborn
- Scikit-learn
- Multiprocessing
- Regex (re)

---

## ⚙️ Project Workflow

1. Load dataset from CSV file  
2. Clean text (remove noise, special characters)  
3. Apply sentiment analysis (Positive / Negative / Neutral)  
4. Split dataset into chunks  
5. Process chunks in parallel using multiprocessing  
6. Combine results  
7. Generate output CSV  
8. Visualize results using charts  

---

## 📊 Visualizations

The project generates:

- 📌 Bar Chart → Sentiment distribution  
- 📌 Confusion Matrix → Model evaluation  

These help in understanding:
- Overall sentiment trends  
- Model performance  

---

## 📁 Repository Structure
