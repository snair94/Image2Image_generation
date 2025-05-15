import gradio as gr
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

# Load the pre-trained model from Hugging Face
model = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
model.to("cuda" if torch.cuda.is_available() else "cpu")

# Function to handle the image generation
def generate_image(image, prompt, aspect_ratio):
    # Resize the image according to the aspect ratio
    width, height = image.size
    if aspect_ratio == "1:1":
        size = (min(width, height), min(width, height))
    elif aspect_ratio == "16:9":
        size = (int(width * 1.78), height)  # Approximation for 16:9
    elif aspect_ratio == "4:3":
        size = (int(width * 1.33), height)  # Approximation for 4:3
    else:
        size = (width, height)  # Default (no change)

    # Resize the image
    image_resized = image.resize(size)

    # Generate a new image from the prompt
    generated_image = model(prompt).images[0]

    # Combine the resized image with the generated one (for demonstration)
    # You can enhance this by doing more advanced operations
    combined_image = Image.blend(image_resized, generated_image, alpha=0.5)

    return combined_image

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Image(type="pil", label="Upload an Image"),
        gr.Textbox(label="Enter Prompt", placeholder="e.g., a futuristic cityscape"),
        gr.Dropdown(label="Select Aspect Ratio", choices=["1:1", "16:9", "4:3"], default="1:1")
    ],
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="AI Image Generation",
    description="Upload an image, enter a text prompt, select an aspect ratio, and generate a referenced image.",
)

# Launch the interface
iface.launch()
