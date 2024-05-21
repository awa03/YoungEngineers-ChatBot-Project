# Tutorial
This application will teach you the basics of fullstack development. In this project you will:
- Create http requests
- Use Python to create a flask application
- Use Python to make api calls
- Use html to design a website
- Use css to design a website

## Installing Dependency's
To install dependencies please run the installation script specified in the `Install-Scripts` directory. <br><br>
The scripts are system dependent, for mac and linux users please run the following command
```sh
    ./Install-Scripts/linux-install.sh
```

For windows users use the powershell script:
```ps1
    ./Install-Scripts/windows-install.ps1
```

Now you should have all dependencys for the project installed. For further Documentation on the individual scripts please visit the [project documentation](Docs/dependency.md)

## Console Application

The first portion of this application will be created as a console application.

### Benefits of Console Applications
Console applications offer several advantages:

- **Simplicity**: Console applications are straightforward to develop and use, focusing on functionality without the overhead of graphical user interfaces.
- **Speed**: They typically run faster than GUI applications due to lower resource consumption.
- **Accessibility**: Easier to debug and run on various platforms, including remote servers and cloud environments.
- **Automation**: Ideal for automation tasks and scripting, enabling quick execution of commands and processes.

### Implementation Details

This section details the implementation of the console application using the Groq library.

**Importing the Groq Library**
```python
from groq import Groq
The Groq library is imported to enable API access for interacting with the chatbot.

**API Access Setup**

```python
# for API access
API_KEY = ''
An API key is required to authenticate requests to the Groq API.
```

**Initializing the API Client**
```python
# initialize the API
client = Groq(
    api_key=API_KEY,
)
```

The Groq client is initialized using the provided API key.

```python
# Ask the AI a question
def Question(Content):
    # Create a new question and response
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # Content represents the question being asked
                "content": Content,
            }
        ],
        # Model for the API -- No need to worry about this
        model="llama3-8b-8192",
    )
    # The AI will return a bunch of responses, so let's just use the first because
    # there will always be at least 1 response
    return chat_completion.choices[0].message.content
```
This function sends a question to the Groq API and returns the AI's response. The model used is llama3-8b-8192.

**Main Execution Loop**
```python
# Where the code starts
if __name__ == '__main__':
    # Loop to allow unlimited questions
    while True:
        # Get the user's question
        user_input = input("You: ")

        # If the user wants to exit
        if user_input == 'q':
            break

        # Print the chatbot's response -- Will print the first response
        print("Chatbot: ", Question(user_input))
```

The main execution loop allows the user to continuously ask questions to the chatbot. The loop breaks if the user inputs 'q', indicating they want to exit the application.
This console application demonstrates how to interact with the Groq chatbot API in a simple and efficient manner.

## Ui Portion

> [!NOTE]
> Still in development