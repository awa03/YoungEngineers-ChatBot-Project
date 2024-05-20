from groq import Groq
import flask

# for api access
API_KEY = ''

# initialize the api
client = Groq(
    api_key=API_KEY,
)

# Ask the ai a question
def Question(Content):
    # Create a new question, and response
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # Content represents the question being asked
                "content": Content,
            }
        ],
        # Model for the api -- Dont need to worry about
        model="llama3-8b-8192",
    )
    # The ai will return a bunch of responses, so lets just use the first because
    # there will always be at least 1 response
    return chat_completion.choices[0].message.content;

# Where the code starts
if __name__ == '__main__':
    # loop so we can unlimitedly ask questions
    while True:
        # get the users questions
        user_input = input("You: ")

        # if the user wants to exit
        if(user_input == 'q'):
            break

        # print the chatbots reponse -- Will print the first response
        print ("Chatbot: ", Question(user_input))

