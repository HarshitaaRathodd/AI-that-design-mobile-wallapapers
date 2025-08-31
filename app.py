# app.py
import os
from huggingface_hub import InferenceClient
import gradio as gr
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN not set. Create a .env file or set HF_TOKEN environment variable.")

# Choose a model — change if you prefer another
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"

client = InferenceClient(MODEL_ID, token=HF_TOKEN)

def generate_image(prompt, style, width, height):
    # build a richer prompt
    styled = f"{prompt}, {style} style, high quality, wallpaper, cinematic lighting"
    # call the HF InferenceClient (returns PIL.Image)
    image = client.text_to_image(styled, width=width, height=height)
    return image

styles = [
    "Realistic",
    "Anime",
    "Cyberpunk",
    "Fantasy Art",
    "Minimalist",
    "Nature Photography",
    "Surreal"
]

with gr.Blocks() as demo:
    gr.Markdown("# 🌌 AI Wallpaper Generator")
    with gr.Row():
        with gr.Column(scale=1):
            prompt = gr.Textbox(label="Enter your wallpaper idea", placeholder="e.g. Misty mountains at sunrise")
            style = gr.Dropdown(choices=styles, value="Realistic", label="Choose style")
            width = gr.Slider(256, 1024, value=512, step=64, label="Width")
            height = gr.Slider(256, 1024, value=512, step=64, label="Height")
            btn = gr.Button("🎨 Generate Wallpaper")
        with gr.Column(scale=1):
            out_img = gr.Image(label="Generated Wallpaper")

    btn.click(generate_image, inputs=[prompt, style, width, height], outputs=out_img)

if __name__ == "__main__":
    # share=False if you don't want a public link; set True to get public gradio.live link
    demo.launch(share=True)
