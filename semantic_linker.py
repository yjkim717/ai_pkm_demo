import os
import openai

def get_existing_notes_texts(notes_folder: str) -> dict:
    notes = {}
    for filename in os.listdir(notes_folder):
        if filename.endswith(".md") or filename.endswith(".txt"):
            path = os.path.join(notes_folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                notes[filename] = f.read()
    return notes

def find_related_notes(new_note_text: str, notes_folder: str, top_k=3):
    existing_notes = get_existing_notes_texts(notes_folder)

    prompt = f"""
Below is a new meeting note. Recommend the top 3 most semantically related notes from the list based on content.

### New Note:
{new_note_text}

### Available Notes:
{list(existing_notes.keys())}

Return only the related filenames as a list.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    result = response['choices'][0]['message']['content']
    return [line.strip("-• \n") for line in result.splitlines() if line.strip()]
