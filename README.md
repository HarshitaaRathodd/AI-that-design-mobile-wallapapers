# AI Wallpaper Generator

Generate mobile wallpapers using Stable Diffusion (via Hugging Face Inference) with a simple Gradio frontend.

## Features
- Prompt-based wallpaper generation
- Style presets (Realistic, Anime, Cyberpunk, etc.)
- Choose width & height
- Single-file app (`app.py`) using Gradio

## Requirements
- Python 3.8+
- Hugging Face token with `read` access

## Setup (local)
1. Clone repo:
git clone https://github.com/<your-username>/ai-wallpaper-generator.git
cd ai-wallpaper-generator

2. Create virtual env & install:
python -m venv venv
source venv/bin/activate    # mac/linux
or: venv\Scripts\activate  # Windows
pip install -r requirements.txt

3. Add your Hugging Face token:
Copy .env.example to .env and paste your token:
HF_TOKEN=hf_xxx...

4. Run:
python app.py
