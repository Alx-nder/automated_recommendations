# virtualTourWebsite
This is a complete web app to demonstrate the automated recommendations.

This is a virtual tour app. Users can post real-estate listings so others can take a online tour of the space. 

FOLDERS:

    API's: 
    This folder contains scripts that implement a Zoom API. 
        2. The Zoom API is used to create a zoom meeting so that several persons can explore a space at once but more importantly, so realtors/tech support can communicate with users at any time.
    
    chatbot_module: 
    This folder contains the cource code for the chatbot used on the web app. the chatbot is powered using the chatterbot module. The chatbot is implemented with AJAX in the chatbot.js that sends requests and responses to and from the chatbot1.py script.

        N.B. speech_module.py is script that uses voice recognition to send a request to the chat bot. That is to say, the user can speak into a mic then speech_module.py turns the speech into text then that text is sent to the chatbot.
    
    database: 
    This folder contains the current MySQL database.

    validations:
    This folder contains the login, logout and validation codes that a user needs to sign-in and sign-out.

    web:
    This folder contains the full UI and frontend of the web app. PHP(HTML), CSS, and JavaScript and images/video content as well.
