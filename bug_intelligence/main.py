from core.embedder import embed_text
from core.similarity import find_similar
from core.analyzer import detect_pattern
from core.classifier import classify_bug
from core.root_concept import find_root_concept

bug_database = [
    {
        "text": "cannot concatenate str and int",
        "embedding": embed_text("cannot concatenate str and int"),
        "category": "type_error"
    },
    {
        "text": "unsupported operand type int and str",
        "embedding": embed_text("unsupported operand type int and str"),
        "category": "type_error"
    },
    {
        "text": "coroutine was never awaited",
        "embedding": embed_text("coroutine was never awaited"),
        "category": "async_misuse"
    }
]

if __name__ == "__main__":
    text     = input("Enter bug: ")
    language = input("Language (python/c/cpp): ").strip() or "python"

    # stage 1 — classify
    classification = classify_bug(text)
    category       = classification["category"]
    method         = classification["method"]
    confidence     = classification["confidence"]

    # stage 2 — root concept
    concept = find_root_concept(text, category, language)

    # similarity + pattern
    embedding = embed_text(text)
    similar   = find_similar(embedding, bug_database, category)
    pattern   = detect_pattern(similar, category)

    # output
    print(f"\nCategory:    {category}")
    print(f"Detected by: {method} (confidence: {confidence})")
    print(f"\nRoot Concept: {concept['name']}")
    print(f"Explanation:  {concept['explanation']}")
    print(f"Found by:     {concept['layer_used']}")
    print(f"\nPattern: {pattern['message']}")