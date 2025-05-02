
import streamlit as st
from story_gen import generate_story
from image_gen import generate_image
from pdf_export import save_pdf

st.set_page_config(page_title="Once Upon AI: Storybook Generator", layout="wide")
st.title("📚 Once Upon AI - Storybook Generator for Children")

# Sidebar inputs
st.sidebar.header("Story Settings")
main_character = st.sidebar.text_input("Main Character", "Luna the Cat")
setting = st.sidebar.text_input("Setting", "a magical forest")
genre = st.sidebar.selectbox("Genre", ["Adventure", "Fairy Tale", "Comedy", "Mystery"])
moral = st.sidebar.text_input("Moral of the Story", "Be kind to others")

if st.sidebar.button("Generate Story"):
    with st.spinner("Creating your story and illustrations..."):
        prompt = f"Write a short, positive, imaginative children’s story about {main_character} in {setting}. Make it a {genre.lower()} with the moral: '{moral}'."
        story = generate_story(prompt)
        image_prompt = f"An illustration of {main_character} in {setting}, in a {genre.lower()} style, for a children's book."
        image_url = generate_image(image_prompt)

        st.subheader("📖 Your AI-Generated Story")
        st.write(story)

        st.subheader("🎨 Story Illustration")
        st.image(image_url, caption="AI-generated illustration")

        # if st.button("📄 Download PDF"):
        #     save_pdf(story, [image_url])
        #     with open("storybook.pdf", "rb") as f:
        #         st.download_button("Download Storybook", f, "storybook.pdf")
