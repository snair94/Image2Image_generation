Brief 1 – AI challenge – Plus Also Studios
________________________________________
Image-to-Image Product Generator

This project is a submission for Brief 1 of the AI Challenge 2025.  
It allows users to generate a product marketing image by uploading a reference image, writing a prompt, and selecting a desired aspect ratio.  
It uses the Stable Diffusion Img2Img model from Hugging Face, and the entire application is built using Gradio

 Features
- Upload any product image (e.g., shoes, furniture, electronics).
- Provide a text prompt to guide generation (e.g. "make this product look futuristic and neon-lit").
- Choose an output aspect ratio (1:1, 16:9, 4:5, 9:16).
- View and download the generated image.

Tech Stack
- [Python 3.10+](https://www.python.org/)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion)
- [Gradio](https://gradio.app/)
- [PyTorch](https://pytorch.org/)
- [Pillow (PIL)](https://python-pillow.org/)

Setup Instructions - locally

1. Clone the Repository
2. Create and Activate a Virtual Environment 
3. Install Dependencies
pip install -r requirements.txt
GPU and faster inference:
Ensure that torch is installed with CUDA support:
________________________________________Run this on hugging-face -
Open the displayed URL in your browser.
This will start a local Gradio interface.
Upload an image, write a prompt, and select the aspect ratio.
View and download your AI-generated image.
________________________________________
Testing Procedure
Upload a test image (e.g., a cup, a can of beer).
Using a basic prompt like:
make it look like a mug with Christmas/Halloween decorations
make it look like a can of coke
Choosing "16:9" aspect ratio and clicking Submit.
The output image reflects the prompt.
A preview is shown.
Download the image file with the down arrow key button on the top right corner of the preview
________________________________________
Dependencies
Here's what the requirements.txt should contain:
gradio
torch
diffusers
transformers
safetensors
accelerate
Pillow
Install with:
pip install -r requirements.txt
________________________________________
File Structure
├── app.py                  # Main application file
├── requirements.txt        # List of Python dependencies
├── README.md               # Documentation file (this file)
└── generated images        # Temporarily stored for download
________________________________________
Notes
Aspect ratio is applied first and then resized to 512x512.
The model runs faster and better on GPU.
Pictures used are either in .png or .jpeg format
This model takes comparatively a little longer as it is running on cpu space of hugging -face
________________________________________
Links
Snair94
GitHub: snair94/Image2Image_generation: This project takes an input image and with the given aspect ratio, generates another image based on the prompt given and lets you download this new image
Email: sn94.ecb@gmail.com
________________________________________

Hugging-Face Stage-link
Image-to-Image Product Generator


