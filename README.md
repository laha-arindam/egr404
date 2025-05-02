# Once Upon AI: Intelligent Storybook Generator for Children

A creative, user-driven AI tool that transforms imagination into beautifully written and illustrated children’s stories.

## 👨‍👩‍👧‍👦 Team Members
- Huifang Li
- Arindam Laha
- Nausad Miyan

## 📘 Project Description
This tool allows users to input character names, themes, genres, and moral lessons. The system then:
- Generates a personalized children's story using GPT
- Creates matching illustrations using DALL·E or Stable Diffusion
- Exports the story as a PDF or shows it in an online flipbook

## 🚀 Features
- AI-based text and image generation
- Clean web interface (Flask or Streamlit)
- Personalization based on user input

## 🛠️ Tech Stack
- OpenAI API (text/image)
- Flask / Streamlit
- FPDF or ReportLab (PDF export)
- Hugging Face datasets
- GitHub Pages (optional)

## 📂 Project Structure
```plaintext
once-upon-ai/
├── app.py               # Main web interface
├── story_generator.py   # GPT-based story creation
├── image_generator.py   # DALL·E / Stable Diffusion illustration generation
├── templates/           # HTML templates (for Flask)
├── static/              # CSS, images, or assets
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and instructions
└── .gitignore           # Files/directories to exclude from version control
