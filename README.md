# 📊 CORD-19 Data Explorer (Frameworks Assignment)

## 📖 Project Overview
This project explores the **CORD-19 dataset** (metadata of COVID-19 research papers).  
We perform:
- Data cleaning & preparation
- Exploratory data analysis
- Visualizations (publication trends, top journals, word cloud of titles)
- An **interactive Streamlit web application** for exploration

The analysis is based on a **sample dataset (`sample_metadata.csv`)** created for testing.

---

## 🗂 Project Structure

pip install -r requirements.txt

pip install pandas matplotlib seaborn streamlit wordcloud

📊 Features
🔹 Data Cleaning

Handles missing values in critical columns (title, publish_time)

Converts publish_time to datetime format

Extracts year column for analysis

Adds abstract_word_count column

🔹 Visualizations

Bar chart: Publications by year

Horizontal bar chart: Top 10 journals

Word cloud: Common words in paper titles

🔹 Streamlit App

Interactive slider to filter year range

Dynamic visualizations (publications over time, top journals)

Displays sample data in a table

📷 Example Outputs

Publications trend chart

Top journals chart

Word cloud visualization

Streamlit app interface with filters

📝 Reflection

Challenges faced:

Handling missing and inconsistent data

Managing dataset size (using sample dataset for testing)

Installing extra libraries (wordcloud, streamlit)

What I learned:

End-to-end workflow of data science (cleaning → analysis → visualization → app)

Basics of Streamlit for building interactive dashboards

Using WordCloud for quick text-based insights

📌 Requirements

Python 3.7+

pandas

matplotlib

seaborn

wordcloud

streamlit
