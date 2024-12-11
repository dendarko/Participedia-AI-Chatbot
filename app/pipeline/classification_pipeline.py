from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load classification model
classification_model_path = "/Users/dennisdarko/Documents/Participedia_project/models/case_classification_model"
classification_model = AutoModelForSequenceClassification.from_pretrained(classification_model_path)
classification_tokenizer = AutoTokenizer.from_pretrained(classification_model_path)

def classify_query(query):
    """
    Classifies the user query or returns a fallback category.
    """
    try:
        inputs = classification_tokenizer(query, return_tensors="pt", truncation=True, padding=True)
        outputs = classification_model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()

        class_map = {0: "cases", 1: "methods", 2: "organizations", 3: "general"}
        return class_map.get(predicted_class, "general")
    except Exception as e:
        logger.error(f"Error classifying query: {str(e)}")
        return "general"
