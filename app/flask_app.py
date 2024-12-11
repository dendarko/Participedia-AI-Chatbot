from flask import Flask, request, jsonify, render_template
from pipeline.backend_integration import process_query
import logging

app = Flask(__name__, template_folder="templates", static_folder="static")

# Logger setup
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["GET"])
def index():
    app.logger.info("Serving index.html")
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def process():
    app.logger.info("Chat endpoint hit")
    query = request.json.get("query", "").strip()
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        app.logger.info(f"Processing query: {query}")
        result = process_query(query)

        # Prepare formatted response
        formatted_response = result["response"].strip().capitalize()
        examples = result.get("examples", [])
        
        # Format examples for better readability
        formatted_examples = [
            {
                "title": ex["title"].capitalize(),
                "description": ex["description"].strip().capitalize(),
                "url": ex["url"]
            }
            for ex in examples
        ]

        return jsonify({"response": formatted_response, "examples": formatted_examples})
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}", exc_info=True)
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
