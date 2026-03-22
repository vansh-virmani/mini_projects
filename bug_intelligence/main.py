from core.embedder import embed_text

from core.similarity import find_similar


bug_database = [
    {
        "text": "cannot concatenate str and int",
        "embedding": embed_text("cannot concatenate str and int")
    },
    {
        "text": "list index out of range",
        "embedding": embed_text("list index out of range")
    },
]




if __name__=="__main__":
    text=input("Enter bug: ")

    embeddings=embed_text(text)
    similar=find_similar(embeddings,bug_database)

    print("\nSimilar Bugs:") 
    for item in similar: 
        print(f"{item['text']} → {item['similarity']:.2f}")

