from flask import Flask, request
from ml.model import TextGenerationModel

app = Flask(__name__, static_folder="build", static_url_path="/")
trilogy_KS_model = TextGenerationModel(
    "./ml/trilogy_model/", "./ml/trilogy_tokenizer.pickle"
)
post_KS_model = TextGenerationModel("./ml/modern_model", "./ml/modern_tokenizer.pickle")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/generate", methods=["POST"])
def generate_text():
    request_body = request.get_json()
    response = {}
    try:
        seed_text = request_body["seedText"].lower()
        temperature = request_body["temperature"]
        word_count = request_body["wordCount"]
    except TypeError as e:
        return str(e), 400
    response["inputText"] = seed_text
    try:
        response["trilogyGeneratedText"] = trilogy_KS_model.generate_text(
            seed_text, word_count, temperature
        )
        response["modernGeneratedText"] = post_KS_model.generate_text(
            seed_text, word_count, temperature
        )
    except Exception as e:
        return str(e), 500
    return response
