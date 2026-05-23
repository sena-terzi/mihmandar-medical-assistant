"""
Simplified Retrieval-Augmented Generation (RAG) pipeline.

Used for hospital information retrieval.
"""

# Load hospital documents
documents = load_hospital_documents()

# Convert documents into embeddings
embeddings = embedding_model.encode(documents)

# Store embeddings in vector database
vector_db.add(embeddings)

# Retrieve relevant information
retrieved_docs = vector_db.search(user_query)

# Generate response using LLM
response = llm.generate(
    context=retrieved_docs,
    query=user_query
)

print(response)
