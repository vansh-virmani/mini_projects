from core.embedder import embed_text
from core.similarity import find_similar
from core.analyzer import detect_pattern
from core.classifier import classify_bug


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




if __name__=="__main__":
    text=input("Enter bug: ")

    #classification
    category=classify_bug(text)
    #embeddings
    embeddings=embed_text(text)
    #similarity
    similar=find_similar(embeddings,bug_database,category)
    #patern_detection
    pattern =detect_pattern(similar,category)
    print(f"\n category: {category}")


    print("\nSimilar Bugs:") 
    for item in similar: 
        print(f"{item['text']} → {item['similarity']:.2f}")
    
    print("\n Pattern Analysis:")

    print(pattern["message"])

    

