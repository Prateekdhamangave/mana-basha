import streamlit as st
from PIL import Image
import os

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Logo (optional)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, use_container_width=True)

# Title
st.markdown("<h2 style='text-align: center; color: #FF5722;'>🤣 Share a Telugu Meme</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Make someone laugh today with your funny Telugu meme!</p>", unsafe_allow_html=True)

# Meme creator name
meme_creator = st.text_input("😎 Meme Creator Name (optional)")

# Meme Title
meme_title = st.text_input("🏷️ Meme Title")

# Upload Meme Image
uploaded_meme = st.file_uploader("📤 Upload your meme (JPG/PNG)", type=["jpg", "jpeg", "png"])

# Optional Caption
meme_caption = st.text_area("📝 Add a caption (optional)")

# Submit button
if st.button("Submit Meme"):
    if meme_title and uploaded_meme:
        st.success("✅ Meme submitted successfully!")
        st.markdown(f"### 🏷️ {meme_title} by {meme_creator if meme_creator else 'Anonymous'}")
        st.image(uploaded_meme, use_column_width=True)
        if meme_caption:
            st.markdown("#### 🗨️ Caption:")
            st.markdown(f"<pre>{meme_caption}</pre>", unsafe_allow_html=True)
    else:
        st.error("❌ Please provide at least a title and image.")
