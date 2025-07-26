import streamlit as st
import os
from datetime import datetime

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Add Recipe", page_icon="🧑‍🍳")

st.markdown("## 🧑‍🍳 Share a Traditional Telugu Recipe")

# Recipe title input
recipe_title = st.text_input("🍲 Recipe Name")

# Ingredients input
ingredients = st.text_area("📝 Ingredients (list them line by line)")

# Preparation steps input
steps = st.text_area("🔥 Preparation Steps")

# Image upload
recipe_image = st.file_uploader("📸 Upload a photo of the dish", type=["jpg", "jpeg", "png"])

# Submit button
if st.button("Submit Recipe"):
    if recipe_title and ingredients and steps:
        # Create recipes directory if not exists
        os.makedirs("data/recipes", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_title = recipe_title.replace(" ", "_").lower()

        # Save text data
        with open(f"data/recipes/{safe_title}_{timestamp}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {recipe_title}\n")
            f.write(f"Ingredients:\n{ingredients}\n\n")
            f.write(f"Preparation Steps:\n{steps}\n")

        # Save image
        if recipe_image:
            img_path = f"data/recipes/{safe_title}_{timestamp}.jpg"
            with open(img_path, "wb") as img_file:
                img_file.write(recipe_image.read())

        st.success("✅ Recipe submitted successfully!")
    else:
        st.warning("⚠️ Please fill all the fields before submitting.")
