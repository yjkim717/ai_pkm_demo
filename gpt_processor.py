import openai

def summarize_and_extract(text: str) -> str:
    prompt = f"""
You are an AI assistant summarizing meeting transcripts.
Summarize the text below and extract key action items.

### Transcript:
{text}

### Output Format:
Summary:
- ...

Action Items:
- ...
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response['choices'][0]['message']['content']
