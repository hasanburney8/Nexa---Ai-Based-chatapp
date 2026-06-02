from typing import List  # Type hints
from sentence_transformers import SentenceTransformer  # NLP model for embeddings
import numpy as np  # NumPy for similarity calculations

class SortSourceService:
    """Sorts search results based on relevance using semantic similarity."""

    def __init__(self):
        # Load a pre-trained sentence embedding model
        self.embedding_model = SentenceTransformer("all-miniLM-L6-v2")

    def sort_sources(self, query: str, search_results: List[dict]):
        """Sort search results based on their similarity to the query."""
        try:
            relevant_docs = []
            query_embedding = self.embedding_model.encode(query)  # Convert query to vector

            for res in search_results:
                res_embedding = self.embedding_model.encode(res["content"])  # Convert text to vector

                # Compute cosine similarity
                similarity = float(
                    np.dot(query_embedding, res_embedding)
                    / (np.linalg.norm(query_embedding) * np.linalg.norm(res_embedding))
                )

                res["relevance_score"] = similarity  # Store similarity score

                # Filter results with a relevance score above 0.3
                if similarity > 0.3:
                    relevant_docs.append(res)

            # Sort results from highest to lowest relevance
            return sorted(relevant_docs, key=lambda x: x["relevance_score"], reverse=True)
        except Exception as e:
            print(f"Error during sorting: {e}")
