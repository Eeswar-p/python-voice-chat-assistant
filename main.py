import whisper
import sounddevice as sd
import numpy as np
import os
from dotenv import load_dotenv # Load environment variables
from playsound import playsound
from openai import OpenAI
from murf import Murf
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="api_keys.env") # Loads variables from api_keys.env file

api_key = os.getenv("OPENAI_API_KEY")


# Get API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")

def create_openai_client(api_key):
    return OpenAI(api_key=api_key)

def create_murf_client(api_key):
    return Murf(api_key=api_key)


def get_openai_response(client, user_input, instructions, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def print_voices():
    voices = create_murf_client(MURF_API_KEY).text_to_speech.get_voices()
    for voice in voices:
        print(f'VOICE ID: {voice.voice_id}, Name:{voice.display_name}, MOODS:{voice.available_styles}')

def stream_text_to_speech(client, text, output_path):
    try:
        print(f"Streaming text: {text}")
        audio_stream = client.text_to_speech.stream(
            text=text,
            voice_id="en-US-ariana",
            format="MP3",
            style="Conversational",
            pitch=0
        )
        
        with open(output_path,"wb") as file:
            for chunk in audio_stream:
                file.write(chunk)
                
        print(f'Audio file created at: {output_path}')
        
    except Exception as e:
        print(f'ERROR:{e}')
        raise
        


class Message:
    def __init__(self, user_name:str, text:str, message_type:str):
        self.user_name = user_name
        self.text = text 
        self.message_type = message_type

def record_audio(model):
    try:
        sample_rate = 16000
        duration = 5  
        
        print("Listening... (speak now)")
        
        audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.float32)
        sd.wait()  
        
        audio_data = audio_data.flatten().astype(np.float32)
        
        result = model.transcribe(audio_data)
        text = result["text"].strip()
        
        if text:
            print(f"Heard: {text}")
            return text
        else:
            print("No speech detected")
            return None
            
    except Exception as e:
        print(f'Error with speech recognition: {e}')
        return None


def play_audio(file_path):
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Error playing audio: {e}")


def print_message(message: Message):
    if message.message_type == "system":
        print(f"\n {message.user_name}: {message.text}")
    elif message.message_type == "ai":
        print(f"\n{message.user_name}: {message.text}")
    else:
        print(f"\n{message.user_name}: {message.text}")

def main():
    print(" Voice chat - just speak!")
    print("=" * 50)
    
    openai_client = create_openai_client(OPENAI_API_KEY)
    murf_client = create_murf_client(MURF_API_KEY)
    whisper_model = whisper.load_model("base")
    
    chat_history = []
    
    while True:
        try:
            user_input = record_audio(whisper_model)
            
            if not user_input:
                print(" Speak again...")
                continue
            
            user_message = Message("You", user_input, "user")
            chat_history.append(user_message)
            print_message(user_message)
            
            instructions = "You are a helpful assistant. Provide short and overly sarcastic, slightly offensive responses."
            ai_response = get_openai_response(openai_client, user_input, instructions)
            
            ai_message = Message("AI", ai_response, "ai")
            chat_history.append(ai_message)
            print_message(ai_message)
            
            
            try:
                file_path = os.path.abspath("audio.mp3")
                
                if os.path.exists(file_path):
                    os.remove(file_path)

                stream_text_to_speech(murf_client, ai_response, file_path)
                play_audio(file_path)
                
            except Exception as e:
                print(f"Audio Error: {e}")
                
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()    
