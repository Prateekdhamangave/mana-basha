import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🏆 Leaderboard", layout="centered")

st.markdown("<h2 style='text-align: center; color: #D32F2F;'>🏆 Mana Basha Leaderboard</h2>", unsafe_allow_html=True)
st.markdown("See who’s contributing the most stories, memes, art, and more!")

# Load score data
score_file = "data/user_scores.csv"
if os.path.exists(score_file):
    df = pd.read_csv(score_file)
    df = df.sort_values(by="points", ascending=False).reset_index(drop=True)

    st.table(df.head(10))
else:
    st.info("No contributions yet. Be the first to earn a badge!")
