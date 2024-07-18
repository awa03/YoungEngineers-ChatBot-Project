from flask import Flask, request, render_template, redirect, url_for
from groq import Groq

# api key - GROQ
API_KEY = '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'
app = Flask(__name__)

client = Groq(api_key=API_KEY)

# chached history
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def main_app():
    # for previous messages (whole div needs to be rerendered)
    global chat_history
    if request.method == 'POST':
        # get the users question
        question = request.form.get('question_box')

        # if the question exists then we need to provide an answer
        if question:
            response = Ask_Question(question)
            chat_history.append({'role': 'user', 'content': question})
            chat_history.append({'role': 'bot', 'content': response})

        return redirect(url_for('main_app'))

    # render chat history
    return render_template('index.html', title='Home', chat_history=chat_history)

# From the without ai version
def Ask_Question(Content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": Content,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
