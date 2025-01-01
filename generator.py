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

    prompt = f"""Du er ekspert i kortspil og elsker at skabe indhold til spil.

        Din opgave er at generere {num_cards} unikke nye eksempler til kortspillet '{game_name}'.

        Spilbeskrivelse: {game_description}

        Følg mønsteret fra disse eksempler:
        {formatted_examples}
        Sørg for at dine eksempler er kreative, sjove og passer til spillet.
        Sørg for at der er variation i eksemplerne, så de ikke er for ens.
        
        VIGTIGE INSTRUKTIONER:
        1. Dit output må KUN være en gyldig JSON-array af objekter.
        2. Hvert objekt i arrayet skal repræsentere et enkelt eksempel.
        3. VIGTIGT: Dit svar må inden omstændigheder idneholde markdown, kodeblokke (```json), forklaringer eller nogen anden tekst før eller efter JSON-arrayet.
        4. Sørg for, at JSON er gyldig og kan parses direkte af en python JSON-parser fx json.loads().
        5. Medtag IKKE nye linjer eller ekstra mellemrum uden for JSON-arrayet.
    """

    try:
        llm_response = llm_generate_func(prompt)
        if llm_response.startswith("```json"):
            llm_response = llm_response.replace("```json", "")
            llm_response = llm_response.replace("```", "")
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