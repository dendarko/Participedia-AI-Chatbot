document.addEventListener("DOMContentLoaded", () => {
  const chatBox = document.getElementById("chat-box");
  const placeholderContainer = document.getElementById("placeholder-container");
  const userInput = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");
  const suggestions = document.getElementById("suggestions");

  const addMessage = (message, isUser, examples = []) => {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${isUser ? "user-message" : "bot-message"}`;

    const icon = document.createElement("img");
    icon.src = isUser ? "/static/usericon.png" : "/static/chatboticon.png"; // Replace with your icon paths
    icon.className = "message-icon";

    const textDiv = document.createElement("div");
    textDiv.innerHTML = message;

    messageDiv.appendChild(icon);
    messageDiv.appendChild(textDiv);

    chatBox.appendChild(messageDiv);

    // Add examples if provided
    if (!isUser && examples.length > 0) {
      examples.forEach((example) => {
        const exampleDiv = document.createElement("div");
        exampleDiv.className = "bot-example";
        exampleDiv.innerHTML = `
          <strong>${example.title}:</strong>
          <p>${example.description}</p>
          <a href="${example.url}" target="_blank" class="example-link">Learn More</a>
        `;
        chatBox.appendChild(exampleDiv);
      });
    }

    // Add feedback buttons for bot responses
    if (!isUser) {
      const feedbackDiv = document.createElement("div");
      feedbackDiv.className = "feedback-buttons";
      feedbackDiv.innerHTML = `
        <span>Was this helpful?</span>
        <button class="thumbs-up">👍</button>
        <button class="thumbs-down">👎</button>
      `;

      feedbackDiv.querySelector(".thumbs-up").onclick = () =>
        alert("Thank you for your feedback!");
      feedbackDiv.querySelector(".thumbs-down").onclick = () =>
        alert("Thank you for your feedback! We'll work on improving.");

      chatBox.appendChild(feedbackDiv);
    }

    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
  };

  const sendMessage = async (query) => {
    const input = query || userInput.value.trim();
    if (!input) return;

    placeholderContainer.style.display = "none"; // Hide placeholder
    suggestions.style.display = "none"; // Hide sample question buttons
    chatBox.style.display = "block"; // Show chat box

    addMessage(input, true); // User message
    userInput.value = "";

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: input }),
      });
      const data = await response.json();

      addMessage(data.response || "No detailed response available.", false, data.examples);
    } catch (error) {
      console.error("Error:", error);
      addMessage("Error connecting to the server.", false);
    }
  };

  sendBtn.addEventListener("click", () => sendMessage());
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  document.querySelectorAll("#suggestions button").forEach((button) => {
    button.addEventListener("click", () => sendMessage(button.textContent));
  });
});
