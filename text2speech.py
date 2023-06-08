import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage
text_to_speak = """Hello 
Anil sir, how are you?
will do cheken party on saturday?
"""
speak_text(text_to_speak)
