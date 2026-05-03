import pandas as pd
from textblob import TextBlob
from multiprocessing import Pool
import matplotlib.pyplot as plt
import re
import os

# Optional (for evaluation)
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "..", "input", "Dataset-SA.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")

# Create output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- CLEAN TEXT ----------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# ---------- SENTIMENT ----------
def analyze_sentiment(text):
    text = clean_text(text)
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# ---------- PARALLEL ----------
def process_chunk(chunk):
    chunk['Predicted_Sentiment'] = chunk['Review'].apply(analyze_sentiment)
    return chunk

# ---------- MAIN ----------
if __name__ == "__main__":

    print("Loading dataset...")
    df = pd.read_csv(INPUT_PATH)

    # Handle missing values
    df = df.dropna(subset=['Review'])

    print(f"Total records: {len(df)}")

    # Chunking
    chunk_size = 5000
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

    print(f"Processing in {len(chunks)} chunks...")

    # Parallel processing
    with Pool(4) as p:
        results = p.map(process_chunk, chunks)

    # Combine results
    final_df = pd.concat(results)

    # ---------- SAVE OUTPUT ----------
    output_csv = os.path.join(OUTPUT_DIR, "output.csv")
    final_df.to_csv(output_csv, index=False)

    # ---------- VISUALIZATION ----------
    counts = final_df['Predicted_Sentiment'].value_counts()
    counts.plot(kind='bar')
    plt.title("Predicted Sentiment Distribution")

    chart_path = os.path.join(OUTPUT_DIR, "chart.png")
    plt.savefig(chart_path)
    plt.close()

    # ---------- EVALUATION ----------
    if 'Sentiment' in final_df.columns:
        actual = final_df['Sentiment'].str.lower()
        predicted = final_df['Predicted_Sentiment'].str.lower()

        acc = accuracy_score(actual, predicted)
        print("Accuracy:", acc)

        cm = confusion_matrix(actual, predicted)

        plt.figure()
        sns.heatmap(cm, annot=True, fmt='d')
        plt.title("Confusion Matrix")

        cm_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
        plt.savefig(cm_path)
        plt.close()

    print("\n✅ DONE")
    print(f"Saved: {output_csv}")
    print(f"Saved: {chart_path}")