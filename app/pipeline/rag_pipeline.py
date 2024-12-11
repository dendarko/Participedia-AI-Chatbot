import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoModelForSeq2SeqLM

# Load QA model
qa_model_path = "/Users/dennisdarko/Documents/Participedia_project/models/qa_model_fine_tuned"
qa_model = AutoModelForQuestionAnswering.from_pretrained(qa_model_path)
qa_tokenizer = AutoTokenizer.from_pretrained(qa_model_path)

# Load generative model
generative_model_name = "t5-small"
generative_model = AutoModelForSeq2SeqLM.from_pretrained(generative_model_name)
generative_tokenizer = AutoTokenizer.from_pretrained(generative_model_name)

def extract_answers_with_qa_model(query, retrieved_docs):
    """
    Extracts answers for a query from the retrieved documents using the QA model.
    Filters out irrelevant contexts and ensures meaningful answers.
    """
    results = []
    for doc in retrieved_docs:
        context = str(doc.get("context", ""))
        if not context.strip():
            continue  # Skip if the context is empty

        try:
            inputs = qa_tokenizer.encode_plus(
                query,
                context,
                return_tensors="pt",
                truncation=True,
                max_length=384,
                padding="max_length"
            )
            outputs = qa_model(**inputs)
            answer_start = torch.argmax(outputs.start_logits)
            answer_end = torch.argmax(outputs.end_logits) + 1
            answer = qa_tokenizer.decode(
                inputs["input_ids"][0][answer_start:answer_end],
                skip_special_tokens=True
            )
            # Only append non-empty answers
            if answer.strip() and "error" not in answer.lower():
                results.append({"document": doc, "answer": answer})
        except Exception as e:
            results.append({"document": doc, "answer": f"Error processing document: {str(e)}"})
    return results


def generate_contextual_response(query, retrieved_docs):
    """
    Generates a contextual response to a query using the retrieved documents and a generative model.
    """
    try:
        # Extract answers from the QA model
        qa_results = extract_answers_with_qa_model(query, retrieved_docs)

        # Clean up and structure the answers
        unique_qa_results = []
        for res in qa_results:
            if res["answer"].strip() not in [r["answer"].strip() for r in unique_qa_results]:
                unique_qa_results.append(res)

        # Combine contexts and answers for generative input
        context = " ".join(
            [f"Document: {res['document'].get('title', 'N/A')}. Answer: {res['answer']}" for res in unique_qa_results]
        )
        input_text = f"question: {query} context: {context}"

        # Tokenize and generate response
        inputs = generative_tokenizer(
            input_text,
            return_tensors="pt",
            truncation=True,
            padding=True
        )
        outputs = generative_model.generate(
            inputs["input_ids"],
            max_length=200,
            num_beams=4,
            early_stopping=True
        )
        response = generative_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response, unique_qa_results
    except Exception as e:
        # Handle errors during response generation
        return f"Error generating response: {str(e)}", []
