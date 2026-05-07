from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(message):

    message = message.lower()

    responses = {

        "hello": "Hello! Nice to meet you.",
        "hi": "Hi there!",
        "hey": "Hey! How are you?",

        "how are you": "I'm doing great. Thanks for asking!",

        "what is your name": "I am CloudBot, your AI assistant.",

        "who made you": "I was created as a cloud computing mini project.",

        "bye": "Goodbye! Have a wonderful day.",

        "thank you": "You're welcome!",

        "thanks": "Happy to help!",

        "what is cloud computing":
        "Cloud computing provides servers, storage and software services over the internet.",

        "advantages of cloud computing":
        "Cloud computing is scalable, cost effective and accessible from anywhere.",

        "what is ai":
        "Artificial Intelligence enables machines to mimic human intelligence.",

        "what is machine learning":
        "Machine learning allows systems to learn automatically from data.",

        "what is python":
        "Python is a popular programming language used in AI, web development and automation.",

        "what is flask":
        "Flask is a lightweight web framework written in Python.",

        "what is html":
        "HTML is used to structure webpages.",

        "what is css":
        "CSS is used for styling webpages beautifully.",

        "what is javascript":
        "JavaScript makes webpages interactive.",

        "tell me a joke":
        "Why do programmers prefer dark mode? Because light attracts bugs!",

        "help":
        "You can ask me about AI, cloud computing, Flask, Python, HTML, CSS and technology."

    }

    for key in responses:
        if key in message:
            return responses[key]

    return "Sorry, I don't understand that yet."

@app.route("/", methods=["GET", "POST"])
def home():

    user_message = ""
    bot_reply = ""

    if request.method == "POST":

        user_message = request.form["message"]

        bot_reply = chatbot_response(user_message)

    return render_template(
        "index.html",
        user_message=user_message,
        bot_reply=bot_reply
    )

if __name__ == "__main__":
    app.run(debug=True)