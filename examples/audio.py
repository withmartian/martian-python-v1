#!/usr/bin/env python

from pathlib import Path

from openai import OpenAI

# gets MARTIAN_API_KEY from your environment variables
openai = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"


def main() -> None:
    # Create text-to-speech audio file
    response = openai.audio.speech.create(
        model="tts-1", voice="alloy", input="the quick brown fox jumped over the lazy dogs"
    )

    response.stream_to_file(speech_file_path)

    # Create transcription from audio file
    transcription = openai.audio.transcriptions.create(model="whisper-1", file=speech_file_path)
    print(transcription.text)

    # Create translation from audio file
    translation = openai.audio.translations.create(
        model="whisper-1",
        file=speech_file_path,
    )
    print(translation.text)


if __name__ == "__main__":
    main()
