import os
from datetime import datetime

def write_to_obsidian(markdown_text: str, related_notes: list, vault_path: str = "./vault/output/"):
    os.makedirs(vault_path, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{vault_path}MeetingNote_{now}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_text)
        if related_notes:
            f.write("\n\n---\n")
            f.write("Related Notes:\n")
            for note in related_notes:
                f.write(f"- [[{note}]]\n")

    print(f"[+] Markdown note created: {filename}")
