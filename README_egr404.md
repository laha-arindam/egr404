
# 📖 Once Upon AI: Intelligent Storybook Generator for Children

A creative, user-driven AI tool that transforms imagination into beautifully written and illustrated children’s stories.

---

## 👨‍👩‍👧‍👦 Team Members
- Huifang Li  
- Arindam Laha  
- Nausad Miyan  

---

## 📘 Project Description

This tool allows users to input:
- Character names
- Themes and settings
- Genre or tone
- Moral lessons

The system then:
- ✍️ Generates a personalized children's story using **GPT**
- 🎨 Creates matching illustrations using **DALL·E** or **Stable Diffusion**
- 📖 Displays the result in an online flipbook or PDF format

---

## 🚀 Features

- AI-powered story generation and illustration
- Clean web interface (built with Flask or Streamlit)
- Personalization based on user input
- Optional PDF export and flipbook viewing

---

## 🛠️ Tech Stack

- 🤖 OpenAI API (GPT-4 and DALL·E for text and image generation)
- 🌐 Flask / Streamlit (web interface)
- 🧠 Hugging Face datasets (for prompt training or tone modeling)
- 🗂️ GitHub Pages (optional for hosting)

---

## 📂 Project Structure

```plaintext
egr404/
├── app.py               # Main web interface (Streamlit or Flask)
├── story_generator.py   # GPT-based story creation
├── image_generator.py   # DALL·E / Stable Diffusion illustration generation
├── templates/           # HTML templates (for Flask version)
├── static/              # CSS, images, or assets
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and instructions
└── .gitignore           # Files/directories to exclude from version control
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

This is required to authenticate with the OpenAI API for story and image generation.

---

## 🧰 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/laha-arindam/egr404.git
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

---

## 📝 License

This project is for academic and educational use. For external or commercial applications, please contact the authors.
