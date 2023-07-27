from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, render_template, session
)
import openai

bp = Blueprint('comparison', __name__)

model_engine_map = {
    "davinci": "davinci",
    "curie": "curie",
    "babbage": "babbage",
    "ada": "ada",
    "gpt3": "gpt-3.5-turbo",
    "gpt4": "gpt-4",
    # Add additional GPT models here
}

# Default
# api_model = model_engine_map.get("gpt3")

@bp.route("/comparison")
def comparison():
    # chat_log = session.get("chat_log", [])
    # chat_log = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."}]
    # session["chat_log"] = chat_log

    return render_template("comparison/comparison.html")


# Modify for sequential posts, to include timing
@bp.route("/comp", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data["user_input"]

    chat_log = session.get("chat_log", [])
    chat_log.append({"role": "user", "content": f"{user_input}"})

    chat_log_2 = session.get("chat_log", [])
    chat_log_2.append({"role": "user", "content": f"{user_input}"})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= chat_log,
        temperature=0.7,
        max_tokens=1024,
    )

    response2 = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat_log,
        temperature=0.7,
        max_tokens=1024,
    )

    message = response.choices[0].message.content.strip()
    message2 = response2.choices[0].message.content.strip()

    chat_log.append({"role": "assistant", "content": f"{message}"})
    chat_log_2.append({"role": "assistant", "content": f"{message2}"})

    session["chat_log"] = chat_log
    session["chat_log_2"] = chat_log_2

    return {"message": message, "message2": message2}