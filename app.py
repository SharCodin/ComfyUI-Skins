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
        label="Stable Diffusion Checkpoint"
    )

    with gr.Tab("txt2img"):
        positive = gr.Textbox(lines=4, placeholder="Positive prompt",container=False)
        negative = gr.Textbox(lines=4, placeholder="Negative prompt",container=False)
    
    with gr.Tab("img2img"):
        pass

demo.launch()
