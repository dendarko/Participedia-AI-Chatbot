from pipeline.classification_pipeline import classify_query
from pipeline.faiss_pipeline import retrieve_top_k
from pipeline.rag_pipeline import generate_contextual_response
from transformers import AutoTokenizer, AutoModel, pipeline
import numpy as np
import torch
import logging
import requests

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load embedding model
embedding_model_name = "/Users/dennisdarko/Documents/Participedia_project/models/embedding_model"
embedding_model = AutoModel.from_pretrained(embedding_model_name)
embedding_tokenizer = AutoTokenizer.from_pretrained(embedding_model_name)

# Load summarization model
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

# External data fetch configuration
API_KEY = "AIzaSyDIaeQ0gqJEDd2JOsbouRudIEYZlICcXHU"
SEARCH_ENGINE_ID = "e1893a7eeae4948ce"


def embed_query(query):
    """
    Generate embeddings for the input query using a pre-trained model.
    """
    try:
        inputs = embedding_tokenizer(query, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = embedding_model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).numpy()
    except Exception as e:
        logger.error(f"Error generating embeddings: {str(e)}", exc_info=True)
        raise RuntimeError("Failed to generate query embeddings.")


def fetch_external_data(query):
    """
    Fetch external data using Google Custom Search API.
    """
    try:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
        response = requests.get(url)
        response.raise_for_status()
        results = response.json().get("items", [])

        return [
            {
                "title": item.get("title", "No Title").capitalize(),
                "url": item.get("link", "#"),
                "description": item.get("snippet", "No description available.").capitalize(),
            }
            for item in results
        ]
    except Exception as e:
        logger.error(f"Error fetching external data: {str(e)}", exc_info=True)
        return []


def refine_response_with_summary_and_external(query, top_k_docs):
    """
    Refines the response with a short summary and integrates external data if available.
    """
    try:
        # Use retrieved documents for the summary
        if top_k_docs:
            response, qa_results = generate_contextual_response(query, top_k_docs)
            summary = summarizer(
                " ".join([doc["description"] for doc in top_k_docs]),
                max_length=150,
                min_length=30,
                do_sample=False
            )[0]["summary_text"]

            examples = [
                {
                    "title": doc.get("title", "No Title").capitalize(),
                    "url": doc.get("url", "#"),
                    "description": doc.get("description", "No description available.").capitalize(),
                }
                for doc in top_k_docs[:3]
            ]
        else:
            # Fallback to external data when no documents are retrieved
            summary = "I couldn't find specific information in our database but here are some relevant resources:"
            examples = fetch_external_data(query)

        return {"response": summary.capitalize(), "examples": examples}

    except Exception as e:
        logger.error(f"Error refining response: {str(e)}", exc_info=True)
        return {"response": "An error occurred while processing your query.", "examples": []}


def process_query(query):
    """
    Processes the user query by integrating classification, FAISS retrieval,
    and RAG pipeline with Google API for a contextual response.
    """
    try:
        # Classify the query
        category = classify_query(query)
        query_embedding = embed_query(query)

        # Retrieve relevant documents using FAISS
        top_k_docs = retrieve_top_k(category, query_embedding)

        # Refine the response with retrieved documents and external data
        refined_result = refine_response_with_summary_and_external(query, top_k_docs)
        return refined_result

    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return {"response": "An error occurred while processing your query.", "examples": []}
