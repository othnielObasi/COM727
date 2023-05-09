// Get the HTML elements
const chatForm = document.querySelector("#chat-form");
const chatInput = document.querySelector("#chat-input");
const chatMessages = document.querySelector(".chat-messages");

// Function to output message to the DOM
function outputMessage(message) {
  const div = document.createElement("div");
  div.classList.add("message");
  div.innerHTML = `<p class="meta">CooKGenie</p>
  <p class="text">${message}</p>`;
  chatMessages.appendChild(div);
}

// Event listener for form submission
chatForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const message = chatInput.value;
  outputMessage(message);
  chatInput.value = "";

  // Send message to the server
  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: message }),
  })
    .then((res) => res.json())
    .then((data) => outputMessage(data.message));
});
