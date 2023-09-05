'''
Instagram bot for the account "influence.ai." This program will call an api to StableDiffusion
to generate a prompt based on keywords in keytrack.py.

Everything needed: 

Posting file: postmain.py
>Image generation file: imagen.py
Caption (and hashtag) generation file: capgen.py
Keyword score tracking file: keytrack.py

'''

import os # used to create / edit / delete files on our computer
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

SDV5_MODEL_PATH = os.getenv('SDV5_MODEL_PATH')
# Creates environement variable SDV5_MODEL_PATH from Windows
# Set in terminal with:      setx SDV5_MODEL_PATH C:\Users\Victo\stable-diffusion-v1-5

### SETTINGS FOR STABLE DIFFUSION ###

negative_prompt = "ugly, bad, bad lighting, poorly drawn, blury, morphed, disfigured, weird, odd, unfocused, illegal" # stuff to avoid
positive_prompt = "Cinematic, glorified, beautiful lighting:.7,\
        divine, Atmospheric:3,\
        Octane render, 8k, HD:3\
        Trending on Artstation, Greg Rutkowski:.7,\
        saturated:1,\
        dof:-.8"
num_inference_steps = 100 # number of steps to generate image
height = 1080
width = 1080
device_type = 'cuda'
low_vram = True # ALWAYS KEEP TRUE, IT SPEEDS IT UP BY SO MUCH

SAVE_PATH = r"c:/Users/Victo/OneDrive/Desktop/pythonCode/Influenceai/imgs"

def uniquify(path):
    '''
    function to prevent images being overrided with new generated images (WILL COMMENT OUT TO SAVE STORAGE LATER)
    '''
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + '(' + str(counter) + ')' + extension
        counter += 1

    return path

def generate_image(prompt):
    '''
    Generates image
    '''
    print("Prompt is : " + prompt)
    print(f"Characters in prompt: {len(prompt)}, limit: 200")

    if low_vram:
        pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH,
                                                       torch_dtype=torch.float16, # ignore error, pylint fault
                                                       revision="fp16")
    else:
        pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)

    pipe = pipe.to(device_type) # cuda is gpu as opposed to 'cpu'

    with autocast(device_type):
        image = pipe(prompt + positive_prompt,
                     negative_prompt=negative_prompt,
                     height=height,
                     width=width,
                     num_inference_steps=num_inference_steps).images[0]

    image_path = uniquify(os.path.join(SAVE_PATH, ("Image")) + '.jpeg')
    print(image_path)
    image.save(image_path)
    return(image_path)
