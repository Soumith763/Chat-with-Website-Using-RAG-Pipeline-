import faiss
from sentence_transformers import SentenceTransformer
import openai

# Load the model and index
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("my_index.index")

def handle_query(query):
    # 1. Encode Query
    query_embedding = model.encode([query])

    # 2. Similarity Search
    distances, indices = index.search(query_embedding, k=5)

    # 3. Retrieve Relevant Information
    # Assuming you have a mapping between indices and original text
    relevant_text = [original_text[i] for i in indices[0]]

    # 4. Construct Prompt for LLM
    prompt = f"Here is some relevant information: {relevant_text}\n\nGiven this information, please answer the query: {query}"

    return prompt

# Example Usage
query = "What is the capital of France?"
prompt = handle_query(query)
print(prompt)