from pathlib import Path

import gradio as gr


BASE_FOLDER = Path("D:/AI/ComfyUI_windows_portable/ComfyUI")
MODELS_FOLDER = BASE_FOLDER / "models/checkpoints"

KSAMPLER_NAMES = [
    "euler",
    "euler_ancestral",
    "dpmpp_sde",
    "dpmpp_2m",
    "dpmpp_2m_sde",
    "dpmpp_3m_sde",
    "ddpm",
    "lcm",
]


def checkpoint_list():
    models = []
    for model in MODELS_FOLDER.glob("*.safetensors"):
        models.append(model.name)
    return models


with gr.Blocks() as demo:
    models = checkpoint_list()
    
    with gr.Row():
        with gr.Column():
            base_checkpoint = gr.Dropdown(choices=models, label="Stable Diffusion Checkpoint")
        
        with gr.Column():
            refiner_checkpoint = gr.Dropdown(choices=models, label="SDXL Refiner Checkpoint")
            use_refiner = gr.Checkbox(label="Use Refiner")

    with gr.Tab("txt2img"):
        with gr.Row():
            with gr.Column(scale=3):
                positive = gr.Textbox(lines=4, placeholder="Positive prompt", container=False)
                negative = gr.Textbox(lines=4, placeholder="Negative prompt", container=False)

            with gr.Column(scale=1):
                with gr.Row():
                    gr.Button("Generate")

                with gr.Row():
                    gr.Dropdown(label="Style 1")
                    gr.Dropdown(label="Style 2")

        with gr.Row():
            with gr.Row():
                with gr.Column():
                    with gr.Row():
                        sampler = gr.Dropdown(choices=KSAMPLER_NAMES, label="Sampling Method")
                        steps = gr.Slider(minimum=5, maximum=50, step=1, label="Sampling Steps")
                    
                    with gr.Row():
                        with gr.Column():
                            width = gr.Slider(minimum=256, maximum=2048, step=64, label="Width")
                            height = gr.Slider(minimum=256, maximum=2048, step=64, label="Height")
                        with gr.Column():
                            cfg = gr.Slider(minimum=1.0, maximum=20.0, step=0.1, label="CFG Scale")
                    
                    with gr.Row():
                        seed = gr.Number(label="Seed")
                        random_seed = gr.Button("Random")
                        last_seed = gr.Button("Last Seed")

                with gr.Column():
                    gr.Image(label="Output", interactive=False)

    with gr.Tab("img2img"):
        pass

    with gr.Tab("Extras"):
        pass

    with gr.Tab("PNG Info"):
        pass

demo.launch()
