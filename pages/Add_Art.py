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
st.markdown("<h2 style='text-align: center; color: #9C27B0;'>🎨 Upload Your Telugu Art</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Share your drawings, rangoli, folk paintings, or modern creations!</p>", unsafe_allow_html=True)

# Artist Name
artist_name = st.text_input("👩‍🎨 Artist Name (optional)")

# Art Title
art_title = st.text_input("🖼️ Art Title")

# Description
description = st.text_area("📝 Describe your art")

# Upload Image
uploaded_art = st.file_uploader("📤 Upload your artwork (JPG/PNG)", type=["jpg", "jpeg", "png"])

# Submit button
if st.button("Submit Artwork"):
    if art_title and description and uploaded_art:
        st.success("✅ Artwork submitted successfully!")
        st.markdown(f"### 🖌️ {art_title} by {artist_name if artist_name else 'Anonymous'}")
        st.image(uploaded_art, use_column_width=True)
        st.markdown("#### 📝 Description:")
        st.markdown(f"<pre>{description}</pre>", unsafe_allow_html=True)
    else:
        st.error("❌ Please fill all required fields and upload an image.")
