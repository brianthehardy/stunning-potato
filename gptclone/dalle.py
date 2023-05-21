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


@bp.route("/generate_image", methods = ['POST'])
def generate_image():
    prompt = request.form["prompt"]

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return render_template("dalle/dalle.html", image_url=image_url, prompt=prompt)