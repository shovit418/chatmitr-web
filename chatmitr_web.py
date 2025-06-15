# ChatMitr Web Version using Flask
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Knowledge database
knowledge = {
    "photosynthesis": "Photosynthesis is the process by which green plants make their own food using sunlight.",
    "gravity": "Gravity is the force that pulls everything towards the Earth.",
    "newton": "Newton's First Law: An object remains at rest or in motion unless acted upon by an external force.",
    "friction": "Friction is the force that resists motion between two surfaces in contact.",
    "acid": "Acids are substances that taste sour and turn blue litmus red.",
    "base": "Bases are substances that taste bitter and turn red litmus blue.",

    # Maths
    "area of circle": "Area of a circle = π × r² (pi = 3.14).",
    "pythagoras": "Pythagoras Theorem: a² + b² = c² in a right-angled triangle.",
    "speed formula": "Speed = Distance / Time",

    # Biology
    "mitochondria": "Mitochondria is the powerhouse of the cell.",
    "cell": "Cell is the basic unit of life.",

    # Hindi Concepts
    "जड़त्व": "जड़त्व वह गुण है जिससे कोई वस्तु अपनी गति या विश्राम की अवस्था बनाए रखती है।",
    "गुरुत्वाकर्षण": "गुरुत्वाकर्षण वह बल है जो हमें पृथ्वी की ओर खींचता है।",
    "प्रधानमंत्री": "भारत के प्रधानमंत्री श्री नरेंद्र मोदी हैं।",
    "संविधान": "भारत का संविधान 26 जनवरी 1950 को लागू हुआ।",

    # Festivals
    "diwali": "Diwali is the festival of lights celebrated to mark the return of Lord Ram to Ayodhya.",
    "holi": "Holi is the festival of colors celebrated to mark the victory of good over evil.",
    "eid": "Eid is a Muslim festival marking the end of Ramadan with prayers and feasting.",
    "christmas": "Christmas is celebrated on 25th December as the birth of Jesus Christ."
}

basic_convo = {
    "hi": "Hi there! How can I help you today?",
    "hello": "Hello! I'm ChatMitr – your study friend.",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "thank you": "You're welcome! 😊",
    "thanks": "Anytime, friend!",
    "what is your name": "My name is ChatMitr – your chatbot buddy."
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for phrase in basic_convo:
        if phrase in user_input:
            return basic_convo[phrase]
    for key in knowledge:
        if key in user_input:
            return knowledge[key]
    return "Hmm... I don't know that yet. Try something from school topics! ✏️"

# HTML Template with basic styling
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>ChatMitr - Web</title>
    <style>
        body { background: #1e1e2f; color: white; font-family: Arial; padding: 20px; }
        #chat-box { background: #2e2e3f; padding: 15px; border-radius: 10px; height: 400px; overflow-y: scroll; }
        #chat-box div { margin-bottom: 10px; }
        .user { color: lightgreen; }
        .bot { color: skyblue; }
        input[type=text] { width: 80%; padding: 10px; font-size: 16px; }
        input[type=submit] { padding: 10px 20px; font-size: 16px; background: #2e8b57; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🤖 ChatMitr – Your Study Buddy</h1>
    <div id="chat-box">
        {% for u, b in messages %}
            <div><span class="user">You:</span> {{ u }}</div>
            <div><span class="bot">ChatMitr:</span> {{ b }}</div>
        {% endfor %}
    </div>
    <form method="post">
        <input type="text" name="query" autofocus placeholder="Ask something...">
        <input type="submit" value="Send">
    </form>
</body>
</html>
'''

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['query']
        reply = get_response(user_input)
        chat_history.append((user_input, reply))
    return render_template_string(html_template, messages=chat_history)

if __name__ == '__main__':
    app.run(debug=True)

