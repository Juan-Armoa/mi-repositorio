import os
import json
from google import genai

client = genai.Client()

def summarize_text(text_to_analyze):
    prompt = f"Analyze the following text and return a short summary with the top 3 key points in English:\n\n{text_to_analyze}"
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
    return response.text

def load_history(filename="ai_summary.json"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            return []
    return []

def save_history(history, filename="ai_summary.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("=== TEXT SUMMARIZER BOT ===")
    print("Type 'exit' or 'quit' to close the program.\n")
    

    history = load_history()

    while True:
        user_input = input("Paste or type the text you want to summarize:\n> ")
        
        if user_input.strip().lower() in ["exit", "quit"]:
            print("\nExiting... See you next time!")
            break
            
        if not user_input.strip():
            print("You did not enter any text. Try again.\n")
            continue

        print("\nProcessing with Gemini...")
        summary = summarize_text(user_input)

        print("\n--- GENERATED SUMMARY ---")
        print(summary)
        print("-" * 25)

        entry = {
            "input": user_input,
            "summary": summary
        }
        history.append(entry)
        save_history(history)
        
        print("Done! History updated in ai_summary.json\n")