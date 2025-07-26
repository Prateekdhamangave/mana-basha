import streamlit as st
import os
from datetime import datetime
from utils.rewards import award_user  # 👈 Reward system

st.markdown("<h2 style='text-align: center; color: #1E88E5;'>🎨 Upload Your Telugu-Themed Art</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Posters, sketches, digital art, mandalas – share anything inspired by Telugu culture!</p>", unsafe_allow_html=True)
st.markdown("---")

# Art Form
with st.form("art_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Upload your artwork (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    title = st.text_input("Title of Artwork")
    author = st.text_input("Your Name (Optional)")
    submitted = st.form_submit_button("Submit Artwork 🎨")

# Save Art
if submitted:
    if uploaded_file is None or title.strip() == "":
        st.error("Please upload an artwork and give it a title.")
    else:
        os.makedirs("uploads/art", exist_ok=True)
        file_ext = uploaded_file.name.split(".")[-1]
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{title.replace(' ', '_')}.{file_ext}"
        file_path = os.path.join("uploads", "art", filename)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # 🎉 Reward the user
        reward = award_user("art")
        st.info(f"🏆 You earned a badge: **{reward['badge_name_tel']} {reward['badge_emoji']}** ({reward['points']} points)")

        st.success("✅ Artwork submitted successfully!")
        st.balloons()
