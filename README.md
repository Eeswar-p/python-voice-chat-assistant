# 🎙️ Python Voice Chat Assistant

A simple real-time **voice chat assistant built with Python** that allows users to communicate with an AI using their voice.

The application captures speech through the microphone, converts it into text using **OpenAI Whisper**, sends the text to **OpenAI GPT-4o-mini** for generating a response, converts the response into natural-sounding speech using **Murf AI**, and plays the generated audio back to the user.

## ✨ Features

* 🎤 **Voice Input** — Records audio directly from the microphone.
* 📝 **Speech-to-Text** — Uses OpenAI Whisper to transcribe spoken input.
* 🤖 **AI Responses** — Uses OpenAI GPT-4o-mini to generate responses.
* 🔊 **Text-to-Speech** — Uses Murf AI to convert AI responses into speech.
* ▶️ **Audio Playback** — Automatically plays the generated response.
* 💬 **Interactive Voice Chat** — Continuously listens and responds until the application is stopped.
* ⚡ **Local Audio Processing** — Uses SoundDevice and NumPy for microphone recording.
* 🔐 **Environment-Based API Keys** — API credentials are loaded from an environment file rather than being hardcoded.

---

## 🏗️ Architecture

```text
                    ┌───────────────────┐
                    │       User        │
                    │   Speaks into     │
                    │    Microphone     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   SoundDevice     │
                    │   + NumPy         │
                    │  Audio Recording  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  OpenAI Whisper   │
                    │  Speech-to-Text   │
                    └─────────┬─────────┘
                              │
                         Text Input
                              │
                              ▼
                    ┌───────────────────┐
                    │  OpenAI GPT-4o-   │
                    │       mini        │
                    │   AI Response     │
                    └─────────┬─────────┘
                              │
                         Response Text
                              │
                              ▼
                    ┌───────────────────┐
                    │      Murf AI      │
                    │  Text-to-Speech   │
                    └─────────┬─────────┘
                              │
                         audio.mp3
                              │
                              ▼
                    ┌───────────────────┐
                    │   Audio Playback  │
                    │    playsound      │
                    └─────────┬─────────┘
                              │
                              ▼
                           🔊 User
```

---

## 🛠️ Tech Stack

| Technology             | Purpose                         |
| ---------------------- | ------------------------------- |
| **Python**             | Main programming language       |
| **OpenAI Whisper**     | Speech-to-text transcription    |
| **OpenAI GPT-4o-mini** | AI response generation          |
| **Murf AI**            | Text-to-speech generation       |
| **SoundDevice**        | Microphone audio recording      |
| **NumPy**              | Audio data processing           |
| **playsound**          | Audio playback                  |
| **python-dotenv**      | Environment variable management |

---

## 📁 Project Structure

```text
python-voice-chat-assistant/
│
├── main.py             # Main voice assistant application
├── requirements.txt    # Python dependencies
├── audio.mp3           # Generated audio response
└── README.md           # Project documentation
```

---

## 🔄 How It Works

The application follows a simple voice-to-voice pipeline.

### 1. Capture Voice

The application records audio from the default microphone using SoundDevice.

The current implementation records:

```text
Sample Rate: 16000 Hz
Channels: 1
Duration: 5 seconds
Audio Type: float32
```

The recorded NumPy audio array is then passed to Whisper.

### 2. Speech-to-Text

OpenAI Whisper processes the recorded audio and converts the speech into text.

```text
Voice
  ↓
Whisper
  ↓
Text
```

For example:

```text
User: What is artificial intelligence?
```

Whisper produces:

```text
"What is artificial intelligence?"
```

### 3. Generate AI Response

The transcribed text is sent to OpenAI using the Chat Completions API.

The current application uses:

```text
Model: gpt-4o-mini
```

The assistant is configured with a system instruction that asks it to provide short, sarcastic responses.

### 4. Convert Response to Speech

The generated AI response is sent to Murf AI's text-to-speech service.

The current implementation uses the Murf voice:

```text
en-US-ariana
```

and the conversational style.

The resulting audio is saved as:

```text
audio.mp3
```

### 5. Play the Response

The generated MP3 file is played using `playsound`.

The complete pipeline is therefore:

```text
🎤 Voice
   ↓
Whisper
   ↓
Text
   ↓
OpenAI GPT-4o-mini
   ↓
AI Response
   ↓
Murf AI
   ↓
audio.mp3
   ↓
🔊 Voice Response
```

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x
* A working microphone
* Speakers/headphones
* OpenAI API key
* Murf API key
* Internet connection

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Eeswar-p/python-voice-chat-assistant.git
```

Navigate into the project:

```bash
cd python-voice-chat-assistant
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The project requires the packages used for:

* OpenAI API
* Murf API
* Whisper
* SoundDevice
* NumPy
* Environment variables

---

## 🔑 API Configuration

The application loads API credentials from:

```text
api_keys.env
```

Create a file named:

```text
api_keys.env
```

in the project root.

Add:

```env
OPENAI_API_KEY=your_openai_api_key
MURF_API_KEY=your_murf_api_key
```

Replace the placeholder values with your actual API keys.

### Important

Do **not** commit your API keys to GitHub.

Add the following to `.gitignore`:

```gitignore
api_keys.env
.env
venv/
__pycache__/
```

---

## ▶️ Running the Application

After configuring the API keys, run:

```bash
python main.py
```

You should see:

```text
Voice chat - just speak!
==================================================
```

The application will then start listening.

Speak into the microphone when you see:

```text
Listening... (speak now)
```

The assistant will:

1. Record your voice.
2. Transcribe the audio.
3. Send the text to OpenAI.
4. Generate an AI response.
5. Convert the response to speech.
6. Play the generated audio.

---

## 💬 Example

```text
Voice Chat - just speak!

Listening... (speak now)

Heard: What is machine learning?

AI: Machine learning is basically teaching computers
to learn from data instead of making them follow every
instruction like a very obedient toaster.
```

The AI response is then converted into speech and played automatically.

---

## 🧩 Main Components

### `record_audio()`

Responsible for microphone input.

```python
audio_data = sd.rec(
    int(sample_rate * duration),
    samplerate=sample_rate,
    channels=1,
    dtype=np.float32
)
```

The audio is recorded at a 16 kHz sample rate and passed to Whisper.

### `get_openai_response()`

Sends the transcribed text to OpenAI.

```python
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": user_input}
    ]
)
```

### `stream_text_to_speech()`

Uses Murf AI to generate speech from the AI response.

```text
AI Response
     ↓
Murf Text-to-Speech
     ↓
MP3 Audio
```

### `play_audio()`

Plays the generated MP3 file through the system's audio output.

---

## 🔐 Security

API credentials should always be stored outside the source code.

Recommended configuration:

```text
api_keys.env
```

Never upload this file to a public repository.

Use:

```gitignore
api_keys.env
```

to prevent accidental commits.

If an API key has already been pushed to GitHub, revoke it and generate a new key.

---

## ⚠️ Current Limitations

The current version is intentionally simple and has a few limitations:

* Audio recording is fixed to **5 seconds**.
* It does not use a wake word.
* It does not provide continuous streaming microphone input.
* The interface is command-line based.
* Generated audio is temporarily stored as `audio.mp3`.
* Internet connectivity is required for the cloud AI services.
* The `chat_history` list stores messages locally during execution, but the current OpenAI request sends only the latest user input, so previous messages are not currently supplied to the model.
* Error handling is basic and can be improved for production use.

---

## 🔮 Future Improvements

Possible improvements include:

* 🎙️ Continuous real-time voice recognition
* 🗣️ Wake-word detection
* 💬 Proper multi-turn conversation memory
* 🌐 Web-based user interface
* ⚡ Streaming AI responses
* 🔊 Streaming text-to-speech
* 🎚️ Configurable voice and speech settings
* 🌍 Multi-language support
* 🧠 Long-term conversation memory
* 📝 Conversation transcript saving
* 🪟 Desktop application interface
* 🔐 Improved API-key management
* 🧪 Automated testing
* 🐳 Docker support
* 📊 Usage and performance monitoring

---

## 📊 System Flow

```text
┌─────────────────┐
│     Microphone  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   SoundDevice   │
│     + NumPy     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Whisper     │
│ Speech-to-Text  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ OpenAI GPT-4o   │
│      -mini      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Murf AI     │
│  Text-to-Speech │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    audio.mp3    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Speaker     │
└─────────────────┘
```

---

## 🎯 Project Objective

The goal of this project is to demonstrate how multiple AI and audio technologies can be combined to build a simple **voice-based conversational assistant**.

It demonstrates the integration of:

```text
Speech Recognition
       +
Natural Language Processing
       +
Large Language Model
       +
Text-to-Speech
       =
Voice AI Assistant
```

---

## 👨‍💻 Author

**Eeswar**

GitHub: [Eeswar-p](https://github.com/Eeswar-p)

Project: [Python Voice Chat Assistant](https://github.com/Eeswar-p/python-voice-chat-assistant)

---

## 📄 License

This project is available for educational and personal use. Add an appropriate open-source license to the repository if you intend to distribute or modify the project publicly.
