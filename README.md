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
- Shows it in an online flipbook

## 🚀 Features
- AI-based text and image generation
- Clean web interface (Flask or Streamlit)
- Personalization based on user input

## 🛠️ Tech Stack
- OpenAI API (text/image)
- Flask / Streamlit
- Hugging Face datasets
- GitHub Pages (optional)

---

### ✅ 🔐 Environment Setup (Fixed)
```markdown
## 🔐 Environment Setup

Create a `.env` file in the project root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here

This is required to authenticate with the OpenAI API for story and image generation.


## 🧰 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/git clone https://github.com/laha-arindam/egr404.git
cd egr404
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

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
