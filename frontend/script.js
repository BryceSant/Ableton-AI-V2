async function send() {
  const msgInput = document.getElementById("msg");
  const chatbox = document.getElementById("chatbox");
  const message = msgInput.value.trim();
  if (!message) return;

  // Display message
  chatbox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;
  msgInput.value = "";

  //Temp message to be shown while it renders
  const tempText = '<div class="bot" id="tempBot">Assistant is typing...</div>'
  chatbox.innerHTML += tempText

  // Send to backend
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message })
  });

  // Display chatbot message
  const data = await res.json();

  //Delete temp
  const tempDel = document.getElementById('tempBot')
  if (tempDel) {
    tempDel.remove()
  }
  //

  //Add chatbot message to chatbot
  chatbox.innerHTML += `
  <div class="bot">
    <b>Bot:</b>
    <pre style="display:inline; white-space:pre-wrap;">${data.reply}</pre>
  </div>`;
  chatbox.scrollTop = chatbox.scrollHeight;
}
