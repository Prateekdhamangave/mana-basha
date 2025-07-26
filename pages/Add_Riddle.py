import streamlit as st
import os
import pandas as pd
from datetime import datetime
from utils.rewards import award_user  # 🎖️ Reward system

# Custom styles
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page title
st.markdown("<h2 style='text-align: center; color: #FF6F00;'>🧠 Share a Telugu Riddle (పొడుపు కథ)</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Got a cool riddle in Telugu or your native dialect? Share it and stump the crowd!</p>", unsafe_allow_html=True)
st.markdown("---")

# Riddle submission form
with st.form("riddle_form"):
    name = st.text_input("Your Name (Optional)")
    dialect = st.selectbox("Dialect", ["తెలుగు (Standard)", "తెలంగాణ తెలుగు", "రాయలసీమ తెలుగు", "ఉత్తరాంధ్ర తెలుగు", "Other"])
    riddle_text = st.text_area("Enter your Riddle here (పొడుపు కథ)", height=200)
    answer = st.text_input("Answer to the Riddle")
    submit = st.form_submit_button("Submit Riddle 🧩")

# Save data and show reward
if submit:
    if riddle_text.strip() == "" or answer.strip() == "":
        st.error("Please enter both the riddle and the answer.")
    else:
        os.makedirs("data", exist_ok=True)
        file_path = "data/riddles.csv"

        new_entry = {
            "name": name.strip() or "Anonymous",
            "dialect": dialect,
            "riddle": riddle_text.strip(),
            "answer": answer.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([new_entry])

        df.to_csv(file_path, index=False)

        st.success("✅ Riddle submitted successfully!")
        st.balloons()

        # 🎖️ Reward system
        reward = award_user("riddle")
        st.info(f"🏆 You earned a badge: **{reward['badge_name_tel']} {reward['badge_emoji']}** ({reward['points']} points)")
