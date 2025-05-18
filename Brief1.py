import gradio as gr
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline, DDIMScheduler
import torch

# Detect device
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# Load the model with appropriate dtype
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=dtype,
    use_safetensors=True
).to(device)

pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)

# Resize uploaded image to selected aspect ratio
def resize_to_aspect(image, aspect_ratio):
    width, height = image.size
    aspect_map = {
        "1:1": (min(width, height), min(width, height)),
        "16:9": (width, int(width * 9 / 16)),
        "4:5": (width, int(width * 5 / 4)),
        "9:16": (int(height * 9 / 16), height)
    }
    target_w, target_h = aspect_map.get(aspect_ratio, (width, height))
    image = image.resize((target_w, target_h))
    return image

def resize_to_512(image):
    return image.resize((768, 768))


#
# Generate new image from prompt and reference image
def generate_img(product_img, prompt, aspect_ratio):
    resized_img = resize_to_aspect(product_img, aspect_ratio).convert("RGB")
    resized_img = resize_to_512(resized_img)  # Required by the model
    output = pipe(prompt=prompt,  negative_prompt="cartoon, anime, painting, blurry, unrealistic, low quality", image=resized_img, strength=0.75, guidance_scale=7.5)
    return output.images[0]

# Gradio UI
gr.Interface(
    fn=generate_img,
    inputs=[
        gr.Image(type="pil", label="Upload Product Image"),
        gr.Textbox(label="Prompt", placeholder="Describe what you want to generate"),
        gr.Dropdown(["1:1", "16:9", "4:5", "9:16"], label="Aspect Ratio", value="1:1")
    ],
    # outputs=gr.Image(label="Generated Image", type="pil"),
    outputs=gr.Image(label='Download Image'),
    title="Image-to-Image Product Generator",
    description="upload a product image, describe your idea, and select the output aspect ratio."

).launch(share=True, ssr_mode=False)
