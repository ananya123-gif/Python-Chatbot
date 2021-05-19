# Python-Chatbot
Chatbots are nothing but an intelligent piece of software that can interact and communicate with people just like humans. In this project, we implemented a chatbot from scratch that will be able to understand what the user is talking about and give an appropriate response.

Steps are as follows:

Step1. Import Libraries 
Create a new python file and name it as main.py and then import all the required modules.

Step2. Load the Data
Data is provided to the Chatbot to respond accordingly. Firstly, it look for the correct match in the function, if not found the correct match, it searches in the wolframalpha module else search Wikipedia and responses.

Step3. Adding features
Adding various features to our chatbot to make it more interactive and more user friendly.
*Adding calculator which can perform calculations from basic to medium level like finding modulas, exponent and even factorial too.
* Adding calendar which can show a full year calendar of any year by just typing the year only.
* Adding voice recognition feature which makes our bot more familiar with the user.

Step4. Interacting with the Chatbot
Our model is ready to chat, so now let’s create a nice graphical user interface for our chatbot. 
In our GUI file, we will be using the Tkinter module to build the structure of the desktop application and then we will capture the user message and again perform some preprocessing before we input message into our trained model.
The model will then predict the tag of the user’s message, and respond randomly from the list provided else respond by searching it through the given library or through Wikipedia.

Step5. Running the Chatbot
Now our chatbot is ready to respond to your queries or requests, run the python file main.py to get the responses and start your conversation with the Chatbot.  

Example:
YOU: hello
BOT: Hello, human.
YOU: how are you
BOT: I am doing well, thank you.
YOU: 5!
BOT: 120
YOU: capital of Nepal
BOT: Kathmandu, Nepal
