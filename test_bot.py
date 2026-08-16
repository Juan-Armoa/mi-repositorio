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

if __name__ == "__main__":
    print("=== TEXT SUMMARIZER BOT ===")
    
    user_input = input("\nPaste or type the text you want to summarize and press Enter:\n> ")
    
    if not user_input.strip():
        print("You did not enter any text. Exiting...")
    else:
        print("\nProcessing with Gemini...")
        summary = summarize_text(user_input)
        
        print("\n--- GENERATED SUMMARY ---")
        print(summary)
        
        output_data = {
            "original_text": user_input.strip(),
            "ai_summary": summary
        }
        
        with open("ai_summary.json", "w", encoding="utf-8") as file:
            json.dump(output_data, file, indent=4, ensure_ascii=False)
            
        print("\nDone! The result was updated in ai_summary.json")