import streamlit as st 
from PIL import Image
import random

# ---------- Custom CSS Styling ---------- #
st.markdown("""
<style>
    .main {
        background-color: #fff8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #8B0000;
    }
    .hero {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        padding: 30px;
        background: linear-gradient(90deg, #ffd6d6, #ffe6b3);
        border-radius: 12px;
    }
    .feature-card {
        background-color: #fff;
        padding: 20px;
        margin: 10px;
        border-radius: 16px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    footer {
        text-align: center;
        font-size: 14px;
        padding: 10px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Hero Section ---------- #
st.markdown("""
<div class='hero'>
    Welcome to <span style='color:#d00000'>Mana Basha</span><br>
    Celebrating the soul of Telugu language through community stories & culture
</div>
""", unsafe_allow_html=True)

# ---------- About Section ---------- #
st.subheader("📜 About Mana Basha")
st.write("""
**Mana Basha** is a community-powered platform to collect and preserve the richness of Telugu through:
- 🌾 Village stories
- 🖼️ Memes & artwork
- 🍛 Family recipes
- 🎭 Local proverbs and dialects
- 🧠 Traditional riddles

Let’s keep our roots alive — one post at a time!
""")

# ---------- Proverb Rotator ---------- #
proverbs = [
    ("చెట్టు నీడ మరిచితే చీకటే.", "If you forget the tree's shade, only darkness remains."),
    ("అపుడు వచ్చిన తలుపు, ఇప్పుడు తీసుకోలేరు.", "The door that once came, cannot be opened now."),
    ("అమ్మ మాటలే అసలైన ఆణిముత్యాలు.", "A mother's words are the real pearls."),
    ("తినే నోరు ఉన్నంతవరకూ, మన పని మనమే.", "As long as we eat, our duty is ours."),
]
random_proverb = random.choice(proverbs)

st.markdown(f"""
### 🧠 Telugu Proverb of the Moment:
> "**{random_proverb[0]}**"  
_– {random_proverb[1]}_
""")

# ---------- Feature Buttons ---------- #
st.markdown("""---  
### 🎯 Explore Features
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Add_Story.py", label="📖 Add Story")
    st.page_link("pages/Add_Meme.py", label="🎭 Add Meme")

with col2:
    st.page_link("pages/Add_Art.py", label="🎨 Add Art")
    st.page_link("pages/Add_Recipe.py", label="🍲 Add Recipe")

with col3:
    st.page_link("pages/Add_Riddle.py", label="🧠 Add Riddle")
    st.page_link("pages/About.py", label="🎤 About Project")

# ---------- Footer ---------- #
st.markdown("""
---
<footer>
Made with ❤️ by Team Mana Basha <br>
Preserve, Celebrate, Share Telugu
</footer>
""", unsafe_allow_html=True)
