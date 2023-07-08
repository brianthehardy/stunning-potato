import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, render_template, session
)
import openai

bp = Blueprint('dalle', __name__)

@bp.route("/dalle")
def dalle():
    # prompt = request.form["prompt"]
    # Send the prompt to the DALL-E API for image generation
    # Retrieve the generated image URL from the DALL-E API response
    # Render the results in the dalle.html template
    return render_template("dalle/dalle.html")  #, image_url=image_url, prompt=prompt)

test_prompts = [
    'A giraffe wearing a tuxedo and holding a bouquet of flowers.',
    'A teapot made of ice and filled with fire.',
    'A pizza with toppings shaped like different countries on a world map',
    'A panda riding a unicycle on a tightrope.',
    'A helicopter made entirely of watermelon.',
    'A library made of clouds floating in the sky',
    'A dragon made of spaghetti and meatballs.',
    'A treehouse with a slide instead of stairs.'
    'A cityscape with buildings made of candy.',
    'A rocket ship powered by a giant hamster wheel.'
]

@bp.route("/generate_image", methods = ['POST'])
def generate_image():
    prompt = request.form["prompt"]

    # If they submit without
    if not prompt:
        prompt = test_prompts[ random.randints(9) ]

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    try:
        image_url = response['data'][0]['url']
    except openai.error.InvalidRequestError:
        return "Your request was rejected as a result of our safety system. Your prompt may contain text that is not allowed by our safety system."

    return render_template("dalle/dalle.html", image_url=image_url, prompt=prompt)