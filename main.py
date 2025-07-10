import os
from dotenv import load_dotenv
from datetime import datetime
import openai
from audio_to_text import transcribe_audio
from gpt_processor import summarize_and_extract
from semantic_linker import find_related_notes
from obsidian_writer import write_to_obsidian

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    audio_path = input("Enter path to audio file: ").strip()
    base_notes_path = "./vault/notes/"

    print("Transcribing audio...")
    text = transcribe_audio(audio_path)

    print("Summarizing and extracting tasks...")
    markdown = summarize_and_extract(text)

    print("Finding related notes...")
    related = find_related_notes(markdown, base_notes_path)

    print("Writing to Obsidian...")
    write_to_obsidian(markdown, related)

    print("Done!")

if __name__ == "__main__":
    main()
