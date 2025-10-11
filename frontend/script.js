async function send() {
  const msgInput = document.getElementById("msg");
  const chatbox = document.getElementById("chatbox");
  const message = msgInput.value.trim();
  if (!message) return;

  // Display message
  chatbox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;
  msgInput.value = "";

  // Send to backend
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message })
  });

  // Display chatbot message
  const data = await res.json();
  chatbox.innerHTML += `<div class="bot"><b>Bot:</b> ${data.reply}</div>`;
  chatbox.scrollTop = chatbox.scrollHeight;
}
