import streamlit as st
import os
import pandas as pd
from datetime import datetime
from utils.rewards import award_user  # 👈 Import reward system

st.markdown("<h2 style='text-align: center; color: #D84315;'>🍛 Share a Telugu Recipe</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Grandma’s secret? Dad’s signature dish? Share your family’s favorite Telugu recipe!</p>", unsafe_allow_html=True)
st.markdown("---")

# Recipe Form
with st.form("recipe_form"):
    title = st.text_input("Recipe Title")
    ingredients = st.text_area("Ingredients (one per line)")
    instructions = st.text_area("Instructions / Steps", height=200)
    author = st.text_input("Your Name (Optional)")
    submitted = st.form_submit_button("Submit Recipe 🍲")

# Handle Submit
if submitted:
    if title.strip() == "" or ingredients.strip() == "" or instructions.strip() == "":
        st.error("Please fill in the title, ingredients, and instructions.")
    else:
        os.makedirs("data", exist_ok=True)
        file_path = "data/recipes.csv"

        new_entry = {
            "title": title.strip(),
            "ingredients": ingredients.strip(),
            "instructions": instructions.strip(),
            "author": author.strip() or "Anonymous",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([new_entry])
        
        df.to_csv(file_path, index=False)

        # 🎉 Reward before success
        reward = award_user("recipe")
        st.info(f"🏆 You earned a badge: **{reward['badge_name_tel']} {reward['badge_emoji']}** ({reward['points']} points)")

        st.success("✅ Recipe submitted successfully! Thank you for preserving Telugu food culture.")
        st.balloons()
