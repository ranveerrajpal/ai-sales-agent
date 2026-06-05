import os
import time
import keyboard
import sounddevice as sd
import soundfile as sf

from stt import transcribe
from rag import build_catalog
from rag import search_catalog
from llm import ask_llm
from tts import speak

SAMPLE_RATE = 16000

os.makedirs("recordings", exist_ok=True)

if not os.path.exists("chroma_db"):
    print("Building catalog...")
    build_catalog("catalog/products.pdf")


def record_audio():

    print("\nHold SPACE and speak...")

    while not keyboard.is_pressed("space"):
        pass

    print("Recording...")

    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        callback=callback
    )

    stream.start()

    while keyboard.is_pressed("space"):
        time.sleep(0.05)

    stream.stop()
    stream.close()

    audio_file = "recordings/input.wav"

    import numpy as np

    audio = np.concatenate(recording, axis=0)

    sf.write(
        audio_file,
        audio,
        SAMPLE_RATE
    )

    return audio_file


print("\nSales Agent Ready\n")

while True:

    audio_path = record_audio()

    user_text = transcribe(audio_path)

    print(f"\nCustomer: {user_text}")

    context = search_catalog(user_text)

    response = ask_llm(
        user_text,
        context
    )

    print(f"\nAgent: {response}")

    speak(response)