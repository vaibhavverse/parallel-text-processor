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
parallel-text-processor/
│
├── code/
│   └── main.py
│
├── input/
│   └── Dataset-SA.csv
│
├── output/
│
├── requirements.txt
├── README.md
└── .gitignore

## ▶️ How to Run the Project

1. Clone the repository:

=> git clone https://github.com/vaibhavverse/parallel-text-processor.git


2. Navigate to project folder:

=> cd parallel-text-processor


3. Install dependencies:

=> pip install -r requirements.txt


4. Run the project:

=> python code/main.py


---

## 🎯 Key Outcomes

- Efficient processing of large datasets using parallel computing  
- Accurate sentiment classification using NLP  
- Clean and structured data pipeline  
- Clear visualization of results  

---

## 📚 Use Cases

- Product review analysis (e-commerce)
- Social media sentiment analysis
- Customer feedback analysis
- NLP learning projects
- Data analysis pipelines

---

## 📊 Results

- Successfully classified text into Positive, Negative, and Neutral  
- Improved processing speed using multiprocessing  
- Generated meaningful visual insights  
- Achieved consistent sentiment prediction on large datasets  

---

## 🏁 Conclusion

This project demonstrates how combining NLP with parallel processing improves performance and scalability.  
It provides a practical approach to handling real-world text datasets efficiently.

---

## 🔮 Future Scope

- Use deep learning models (BERT, LSTM) for better accuracy  
- Real-time streaming sentiment analysis  
- Deploy as web application (API-based)  
- Support multi-language text processing  
- Integrate with dashboards for live analytics  

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Author

Vaibhav Kumar  
GitHub: https://github.com/vaibhavverse
