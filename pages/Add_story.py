import streamlit as st
import os
import pandas as pd
from datetime import datetime

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page title
st.markdown("<h2 style='text-align: center; color: #6A1B9A;'>📖 Share Your Telugu Story</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Tell us about your village, your family traditions, or a story you grew up hearing.</p>", unsafe_allow_html=True)
st.markdown("---")

# Story Form
with st.form("story_form"):
    title = st.text_input("Story Title")
    author = st.text_input("Your Name (Optional)")
    language = st.selectbox("Language", ["తెలుగు (Telugu)", "English", "Other"])
    story = st.text_area("Write your story here", height=250)
    submitted = st.form_submit_button("Submit Story ✍️")

# Save to CSV
if submitted:
    if title.strip() == "" or story.strip() == "":
        st.error("Please enter both a title and your story before submitting.")
    else:
        # Prepare file
        os.makedirs("data", exist_ok=True)
        file_path = "data/stories.csv"

        new_entry = {
            "title": title.strip(),
            "author": author.strip() or "Anonymous",
            "language": language,
            "story": story.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Save
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([new_entry])
        
        df.to_csv(file_path, index=False)

        st.success("✅ Story submitted successfully! Thank you for contributing.")
        st.balloons()
