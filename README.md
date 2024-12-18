# Participedia AI Chatbot

## Purpose
The Participedia AI Chatbot project was initiated to resolve critical usability challenges within the Participedia platform, a global repository for participatory democracy practices. Participedia offers vast datasets categorized into cases, methods, and organizations. However, users often faced difficulties accessing and navigating this extensive information, particularly when searching for specific insights.

The chatbot utilizes advanced Natural Language Processing (NLP) to enable intuitive, human-like interactions. By understanding and responding to user queries, the chatbot simplifies information retrieval, providing personalized, relevant results in real time. This enhancement aims to:
- **Increase User Engagement**: An intuitive, interactive chatbot interface promotes engagement by reducing friction in the data retrieval process.
- **Enhance Usability**: Simplifying the search for participatory democracy practices ensures that the platform becomes more user-friendly and accessible to a diverse audience.
- **Empower Stakeholders**: Researchers, educators, and practitioners gain quick and effortless access to critical insights, enabling them to make data-driven decisions or enhance their learning.

---

## Key Features
1. **Dynamic Query Processing**: The chatbot leverages NLP models to interpret user queries and retrieve the most contextually relevant information from Participedia's datasets. This feature supports a wide range of natural language inputs, from specific queries like “What are citizen juries?” to broader questions like “How does participatory budgeting work in Canada?”
2. **Real-World Examples**: Responses generated by the chatbot are enriched with real-world examples from Participedia’s datasets. 
    - **Cases**: Provide detailed narratives of actual participatory democracy implementations (e.g., participatory budgeting projects in Porto Alegre, Brazil).
    - **Methods**: Include descriptions of techniques like deliberative polling and citizen juries.
    - **Organizations**: Highlight profiles of advocacy groups or institutions promoting participatory practices.
3. **User Feedback Mechanism**: To ensure the chatbot evolves and improves over time, a feedback loop has been integrated.
    - Users can rate responses as helpful (thumbs-up) or unhelpful (thumbs-down).
4. **Accessible Interface**: A clean, minimalistic interface guides users with sample queries and placeholder text. Responses are clearly structured, featuring concise summaries with links to detailed resources.

---

## Target Audience
1. **Researchers**:
   - Problem: Researchers often need to sift through large datasets to find specific cases or methods related to participatory democracy.
   - Solution: The chatbot streamlines this process by interpreting queries and delivering tailored results, saving time and effort.
2. **Educators and Students**:
   - Problem: The platform's static structure can be overwhelming for students unfamiliar with participatory processes.
   - Solution: The chatbot acts as an educational aid, enabling students to ask questions and explore concepts interactively.
3. **Practitioners**:
   - Problem: Policymakers and activists require actionable insights to design participatory initiatives.
   - Solution: The chatbot provides tailored recommendations, linking practitioners to relevant resources.

---

## Why It Matters
The Participedia AI Chatbot transforms how users interact with participatory democracy data, making it:
- **Effortless**: Natural language processing eliminates the need for complex navigation or keyword searches.
- **Contextual**: Tailored responses ensure users find exactly what they need.
- **Engaging**: Features like sample queries and feedback mechanisms create a user-friendly experience.

---

## System Design

### Architecture Overview
1. **Query Classification Pipeline**: Categorizes user queries into predefined categories (cases, methods, organizations).
2. **FAISS-Based Retrieval System**: High-speed similarity search and clustering of embeddings.
3. **RAG-Based QA Pipeline**: Combines FAISS retrieval with a fine-tuned T5 model for generating contextual and accurate responses.
4. **Frontend**: Built using Streamlit and Flask for seamless user interaction.

### Workflow
1. **User Input**: The user types a question into the chatbot.
2. **Query Classification**: The query is classified into categories.
3. **Data Retrieval**: FAISS retrieves relevant embeddings.
4. **Response Generation**: The T5 model generates a concise response.
5. **User Feedback**: Users rate responses for refinement.

---

## Methodology

### Data Sources
The chatbot leverages three primary datasets from Participedia:
1. **Cases**:
   - Description: Real-world examples of participatory democracy implementations.
   - Examples: Participatory budgeting in Porto Alegre, Brazil; citizen juries in the UK.
2. **Methods**:
   - Description: Techniques and strategies for participatory engagement.
   - Examples: Deliberative polling, participatory mapping, citizen assemblies.
3. **Organizations**:
   - Description: Profiles of institutions and advocacy groups that support participatory democracy.
   - Examples: Nonprofit organizations promoting public engagement, think tanks focusing on governance innovation.

### Preprocessing
1. **Cleaning**:
   - Removed duplicates and irrelevant entries.
   - Standardized text formatting for consistency.
2. **Tokenization**:
   - Processed textual data using DistilBERT tokenizer to create semantic embeddings.
3. **Categorization**:
   - Grouped datasets into predefined categories (cases, methods, organizations).

### Model Training
1. **Query Classification**:
   - Model: Lightweight classification model.
   - Accuracy: Achieved 91%.
2. **QA Model**:
   - Model: Fine-tuned T5 (Text-to-Text Transfer Transformer) for generating concise answers.
   - Performance: F1 Score of 0.89.

---

## Implementation and Features

### Core Functionality
- Users can input natural language queries such as:
  - “What is participatory budgeting?”
  - “Which organizations support participatory governance?”
- The chatbot retrieves and synthesizes relevant data from Participedia.

### Enhanced Features
1. **Dynamic Suggestions**:
   - Clickable buttons guide first-time users with sample queries.
2. **Feedback Mechanism**:
   - Users can provide thumbs-up or thumbs-down feedback for responses.
3. **Structured Responses**:
   - Responses include concise summaries, examples, and clickable links.

---

## Results and Insights

### Performance Metrics
1. **Classification Model**:
   - Accuracy: 92%.
2. **QA Model**:
   - F1 Score: 0.89.

### User Feedback
1. **Strengths**:
   - Intuitive design and fast response times.
2. **Areas for Improvement**:
   - Expanded dataset coverage and deeper responses.

### Key Findings
1. Popular Topics:
   - Participatory budgeting and citizen deliberation.
2. Role of Real-World Examples:
   - Enriched responses with examples increased user satisfaction.

---

## Challenges and Solutions

### Challenges
1. **Large Datasets**:
   - Computational overhead in processing and retrieval.
2. **Ambiguous Queries**:
   - Vague inputs like “How does it work?” posed difficulties.

### Solutions
1. **Efficient Retrieval**:
   - Integrated FAISS for high-speed embedding searches.
2. **Context-Based Responses**:
   - QA model fine-tuned to handle ambiguity.

---

## Future Enhancements

### Scalability
1. **Multilingual Support**:
   - Expand chatbot to handle multiple languages using XLM-R or mT5 models.
2. **Real-Time Updates**:
   - Synchronize with Participedia’s API for dynamic updates.

### New Features
1. **Advanced Recommendations**:
   - Personalized content suggestions based on query history.
2. **Visual Dashboards**:
   - Dynamic charts summarizing key insights.

---

## Impact and Contributions

### Research Benefits
- Simplifies access to participatory democracy datasets.
- Enables interdisciplinary research applications.

### Educational Impact
- Acts as an interactive learning tool for students and educators.
- Encourages exploration of participatory governance concepts.

### Practical Applications
- Provides actionable insights for policymakers and community leaders.
- Supports decision-making with tailored recommendations.

---

## Conclusion
The Participedia AI Chatbot successfully bridges the gap between Participedia’s extensive datasets and its diverse global audience. By leveraging advanced NLP, it simplifies data access, enhances engagement, and empowers stakeholders to explore participatory democracy concepts. Future enhancements will continue to expand its reach and impact, making it a critical tool for researchers, educators, and practitioners worldwide.


## Project Structure

```plaintext
├── app/
│   ├── app.py                 # Streamlit frontend
│   ├── flask_app.py           # Flask backend for API handling
├── pipeline/
│   ├── backend_integration.py # Backend logic for processing queries
│   ├── classification_pipeline.py # Query classification module
│   ├── faiss_pipeline.py      # FAISS-based embedding retrieval
│   ├── rag_pipeline.py        # RAG-based QA pipeline
├── static/
│   ├── app.js                 # Frontend JavaScript
│   ├── style.css              # Frontend CSS
│   ├── chatboticon.png        # Chatbot icon
│   ├── usericon.png           # User icon
│   ├── logo.png               # Participedia logo
├── templates/
│   ├── index.html             # Frontend HTML template
├── clusters/                  # FAISS clustering data
├── data/
│   ├── cleaned_dataset/       # Cleaned datasets (cases, methods, organizations)
├── embeddings/                # Embedding files
├── models/                    # Pretrained ML models
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation

```
How to Run
Prerequisites

    Python 3.8+
    Docker (for deployment)
    Google Cloud SDK (for Vertex AI integration)

Steps

    1. Clone the repository:
    git clone https://github.com/dendarko/participedia-ai-chatbot.git
    cd participedia-ai-chatbot
    
    2.Install dependencies:
    pip install -r requirements.txt
    
    3. Run the Flask server:
    python app/flask_app.py
    
    4. Open the Streamlit frontend:
    streamlit run app/app.py

License

This project is licensed under the MIT License.
Contact

For questions or feedback, please contact:

    Name: Dennis Darko
    Email: dennisdarko0909@gmail.com
    LinkedIn: Dennis Darko- https://www.linkedin.com/in/dennis-darko/


   
