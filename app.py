from pathlib import Path

import gradio as gr


BASE_FOLDER = Path("D:/AI/ComfyUI_windows_portable/ComfyUI")
MODELS_FOLDER = BASE_FOLDER / "models/checkpoints"

def checkpoint_list():
    models = []
    for model in MODELS_FOLDER.glob("*.safetensors"):
        models.append(model.name)
    return models


with gr.Blocks() as demo:
    models = checkpoint_list()
    checkpoint = gr.Dropdown(
        choices=models,
    )

demo.launch()
