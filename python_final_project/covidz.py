import pandas as pd

df = pd.read_csv("sample_metadata.csv")
print(df.shape)
print(df.info())
print(df.head())

print(df.isnull().sum())

df = df.dropna(subset=["title", "publish_time"])

df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

year_counts = df["year"].value_counts().sort_index()
year_counts.plot(kind="bar", title="Publications by Year")

top_journals = df["journal"].value_counts().head(10)
top_journals.plot(kind="barh", title="Top 10 Journals")

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(df["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("sample_metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Filter by year
years = st.slider("Select Year Range", 2015, 2023, (2019, 2021))
filtered = df[(df["year"] >= years[0]) & (df["year"] <= years[1])]

# Publications by Year
st.subheader("Publications Over Time")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="barh", ax=ax)
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered.head(10))

