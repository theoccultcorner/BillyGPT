# Import necessary libraries
import openai
import speech_recognition as sr
import pyttsx3

# Assign OpenAI API key
openai.api_key = "Your API Key Goes Here"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Loop to listen for audio input
while True:
    # Create speech recognizer object
    r = sr.Recognizer()
    keywords = ["billy"]
    # Listen for input
    with sr.Microphone() as source:
        print("i'm listening:")
        audio = r.listen(source)
     
    # Try to recognize the audio
    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print("You said:", prompt)
        
        if "billy" in prompt.lower():
            # Use OpenAI to create a response
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.8,
                max_tokens=60
            )

            # Get the response text
            response_text = str(response['choices'][0]['text']).strip('\n\n')
            print(response_text)

            # Speak the response
            engine.say(response_text)
            engine.runAndWait()
            print()
        else:
            print("Keyword not found")
    
    
    
    # Catch if recognition fails
    except:
        response_text = "?"
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
        print()
