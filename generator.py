import json
import os
from typing import List, Dict, Callable
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def generate_cards(
    num_cards: int,
    few_shot_examples: List[Dict],
    game_name: str,
    game_description: str,
    llm_generate_func: Callable,
) -> List[Dict]:
    """Generates cards using the LLM based on few-shot examples."""

    formatted_examples = "\n".join(
        [f"- {example}" for example in few_shot_examples]
    )

    prompt = f"""You are an expert in card games and love to create content for games.

    Your task is to generate {num_cards} unique new examples for the card game '{game_name}'.

    Game Description: {game_description}

    Follow the pattern from these examples:
    {formatted_examples}

    IMPORTANT INSTRUCTIONS:
    1. Output ONLY a valid JSON array of objects.
    2. Each object in the array should represent a single example.
    3. Do NOT include any markdown, code blocks (```json), explanations, or any other text before or after the JSON array.
    4. Ensure the JSON is valid and can be parsed directly by a JSON parser.
    5. Do not include any newlines or extra whitespace outside of the JSON array.
    """

    try:
        llm_response = llm_generate_func(prompt)
        cards = json.loads(llm_response)
        return cards
    except (json.JSONDecodeError, IndexError) as e:
        print(f"Error decoding json: {e}, LLM Response: {llm_response}")
        return []

def generate_with_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    return response.text