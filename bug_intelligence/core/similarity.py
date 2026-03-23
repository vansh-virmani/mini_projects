import numpy as np

def cosine_similarity(vec1,vec2):
    vec1=np.array(vec1)
    vec2=np.array(vec2)

    dot_product=np.dot(vec1,vec2)

    norm1=np.linalg.norm(vec1)
    norm2=np.linalg.norm(vec2)

    return dot_product /(norm1*norm2)

def find_similar(new_embeddings,database,category,threshold=0.6):
    results=[]

    for bug in database:
        if bug["category"] !=category:
            continue

        sim=cosine_similarity(new_embeddings,bug["embedding"])

        if sim>threshold:
            results.append({
                "text":bug["text"],
                "similarity":round(sim,2)

            })

    #sorting by similarity
    results.sort(key=lambda x: x["similarity"],reverse=True)

    return results
