import streamlit as st
import os
import pandas as pd
from datetime import datetime
from utils.rewards import award_user

# Custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and Instructions
st.markdown("<h2 style='text-align: center; color: #D32F2F;'>😂 Share a Telugu Meme</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a funny meme in Telugu. Let the world laugh with our local flavor!</p>", unsafe_allow_html=True)
st.markdown("---")

# Meme Upload Form
with st.form("meme_form"):
    uploader_name = st.text_input("Your Name (Optional)")
    language = st.selectbox("Language", ["తెలుగు (Telugu)", "English", "Other"])
    meme_file = st.file_uploader("Upload your meme (image file)", type=["jpg", "jpeg", "png"])
    caption = st.text_area("Write a funny caption (optional)", height=100)
    submitted = st.form_submit_button("Upload Meme 😄")

# Save and Reward
if submitted:
    if meme_file is None:
        st.error("Please upload an image file.")
    else:
        # Create folder
        os.makedirs("data/memes", exist_ok=True)

        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{meme_file.name}"
        filepath = os.path.join("data/memes", filename)

        # Save image
        with open(filepath, "wb") as f:
            f.write(meme_file.read())

        # Save metadata to CSV
        meta_path = "data/memes.csv"
        new_entry = {
            "filename": filename,
            "uploader": uploader_name.strip() or "Anonymous",
            "language": language,
            "caption": caption.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if os.path.exists(meta_path):
            df = pd.read_csv(meta_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([new_entry])
        
        df.to_csv(meta_path, index=False)

        st.success("✅ Meme uploaded successfully!")
        st.image(filepath, width=300)
        st.balloons()

        # Reward 🎁
        reward = award_user("meme")
        st.info(f"🏆 You earned a badge: **{reward['badge_name_tel']} {reward['badge_emoji']}** ({reward['points']} points)")
