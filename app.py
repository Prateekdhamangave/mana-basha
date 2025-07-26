import streamlit as st

st.set_page_config(page_title="మన భాష", page_icon="🌾", layout="wide")

st.markdown(
    """
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: bold;
            color: #4B0082;
        }
        .sub-title {
            font-size: 1.5rem;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="main-title">మన భాష</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">A Celebration of Telugu Stories, Art & Culture 🌾</p>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("👋 **Welcome to Mana Basha!** Explore and contribute to Telugu culture by sharing stories, memes, recipes, and art.")

# Sidebar navigation info
st.sidebar.success("👈 Select a page from the left sidebar to begin!")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌟 Pages")
st.sidebar.markdown("- Home")
st.sidebar.markdown("- Add Story")
st.sidebar.markdown("- Add Meme")
st.sidebar.markdown("- Add Recipe")
st.sidebar.markdown("- Add Art")
st.sidebar.markdown("- View Submissions")
st.sidebar.markdown("---")
st.sidebar.markdown("🚀 Built with ❤️ by Team Mana Basha")
