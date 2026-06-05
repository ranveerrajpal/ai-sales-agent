import asyncio
import edge_tts
import pygame

VOICE = "en-US-AriaNeural"

async def generate(text):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("reply.mp3")

def speak(text):

    asyncio.run(generate(text))

    pygame.mixer.init()
    pygame.mixer.music.load("reply.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue