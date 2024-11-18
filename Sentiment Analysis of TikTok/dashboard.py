
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the sentiment data
comments_df = pd.read_csv('comments_with_sentiment.csv')

# Dashboard Title
st.title("TikTok Comment Sentiment Analysis")

# Show data
st.write("### Sample Data")
st.write(comments_df.head(10))

# Sentiment Distribution
st.write("### Sentiment Distribution")
sentiment_counts = comments_df['sentiment'].value_counts()
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Display most positive and negative comments
st.write("### Most Positive Comments")
st.write(comments_df.nlargest(5, 'sentiment_score')[['comment', 'sentiment_score']])

st.write("### Most Negative Comments")
st.write(comments_df.nsmallest(5, 'sentiment_score')[['comment', 'sentiment_score']])
