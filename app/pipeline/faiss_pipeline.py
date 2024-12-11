import faiss
import numpy as np
import pandas as pd
import pickle

# Load FAISS indices
indices = {
    "cases": faiss.read_index("/Users/dennisdarko/Documents/Participedia_project/faiss/cases_faiss_index"),
    "methods": faiss.read_index("/Users/dennisdarko/Documents/Participedia_project/faiss/methods_faiss_index"),
    "organizations": faiss.read_index("/Users/dennisdarko/Documents/Participedia_project/faiss/organizations_faiss_index"),
}

# Load embeddings
with open("/Users/dennisdarko/Documents/Participedia_project/embeddings/cases_with_embeddings.pkl", "rb") as f:
    cases_embeddings = pickle.load(f)

with open("/Users/dennisdarko/Documents/Participedia_project/embeddings/methods_with_embeddings.pkl", "rb") as f:
    methods_embeddings = pickle.load(f)

with open("/Users/dennisdarko/Documents/Participedia_project/embeddings/organizations_with_embeddings.pkl", "rb") as f:
    organizations_embeddings = pickle.load(f)

# Load DataFrames
cases_df = pd.read_csv("/Users/dennisdarko/Documents/Participedia_project/data/data_cases.csv").reset_index()
methods_df = pd.read_csv("/Users/dennisdarko/Documents/Participedia_project/data/data_methods.csv").reset_index()
organizations_df = pd.read_csv("/Users/dennisdarko/Documents/Participedia_project/data/data_organizations.csv").reset_index()

# Create a mapping for DataFrames
data_map = {
    "cases": cases_df,
    "methods": methods_df,
    "organizations": organizations_df,
}

def retrieve_top_k(category, query_embedding, k=5):
    """
    Retrieves the top-k relevant documents using FAISS similarity search.
    """
    index = indices[category]
    distances, indices_list = index.search(query_embedding.reshape(1, -1), k)
    results = data_map[category].iloc[indices_list[0]].to_dict(orient="records")

    # Sort results by relevance score
    results = sorted(results, key=lambda x: distances[0][indices_list[0].tolist().index(x['index'])])

    for result in results:
        result["context"] = result.get("description", "No description available.")
    return results
