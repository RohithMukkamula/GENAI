import streamlit as st


import pandas as pd
import numpy as np



from wordcloud import WordCloud, STOPWORDS
from google.cloud import bigquery

import warnings
warnings.filterwarnings("ignore")



df = pd.read_csv("https://github.com/RohithMukkamula/GENAI/blob/main/concatenated_df1.csv")

# Sidebar selection
year_selected = st.sidebar.selectbox("Select Year", [0] + df['year'].unique().tolist())
month_selected = st.sidebar.selectbox("Select Month", [0] + df['month'].unique().tolist())

# Filter DataFrame based on selections
if (year_selected != 0) & (month_selected != 0):
    filtered_df = df.loc[((df['year'] == year_selected) & (df['month'] == month_selected))]
    unique_rows_df = filtered_df.drop_duplicates(subset=['key_points'])

    # Apply some CSS styling
    st.markdown(
        """
        <style>
            .highlight {
                background-color: #f5f5f5;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
            }
            .highlight:hover {
                transform: translateY(-2px);
                transition: transform 0.3s ease;
            }
            .Clean_Sentiment-Positive {
                color: green;
            }
            .Clean_Sentiment-Negative {
                color: red;
            }
            .Clean_Sentiment-Mixed {
                color: yellow;
            }
            .legend {
                margin-top: 20px;
                font-size: 16px;
            }
            .legend-item {
                display: inline-block;
                margin-right: 20px;
            }
            .legend-item span {
                margin-right: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.subheader('Data with Key Points and Sentiment')
    
    # Apply styling to each item in the loop
    for i in range(len(unique_rows_df)):
        sentiment = unique_rows_df.iloc[i]["Clean_Sentiment"]
        if sentiment == "Positive":
            sentiment_class = "Clean_Sentiment-Positive"
        elif sentiment == "Mixed":
            sentiment_class = "Clean_Sentiment-Mixed"
        else:
            sentiment_class = "Clean_Sentiment-Negative"
        
        st.markdown(f'<div class="highlight"><span class="{sentiment_class}">●</span> {unique_rows_df.iloc[i]["key_points"]}</div>', unsafe_allow_html=True)

    # Legend explaining the color codes
    st.markdown('<div class="legend"><div class="legend-item"><span class="Clean_Sentiment-Positive">●</span> Positive</div><div class="legend-item"><span class="Clean_Sentiment-Negative">●</span> Negative</div><div class="legend-item"><span class="Clean_Sentiment-Mixed">●</span> Mixed</div></div>', unsafe_allow_html=True)

