from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, render_template, session
)
import openai

bp = Blueprint('chat', __name__)

model_engine_map = {
    "davinci": "davinci",
    "curie": "curie",
    "babbage": "babbage",
    "ada": "ada",
    "gpt": "gpt-3.5-turbo"
    # Add your other GPT models here
}
api_model = model_engine_map.get("gpt")

@bp.route("/")
def index():
    # chat_log = session.get("chat_log", [])
    chat_log = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."}]
    session["chat_log"] = chat_log

    print(chat_log)

    return render_template("index.html")

@bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data["user_input"]
    chat_log = session.get("chat_log", [])
    chat_log.append({"role": "user", "content": f"{user_input}"})

    response = openai.ChatCompletion.create(
        model=api_model,
        messages= chat_log,
        temperature=0.7,
        max_tokens=1024,
    )

    message = response.choices[0].message.content.strip()

    chat_log.append({"role": "assistant", "content": f"{message}"})

    session["chat_log"] = chat_log

    return {"message": message}