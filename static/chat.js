const box = document.getElementById("chat-box");

function addMessage(text, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.innerText = text;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

async function send() {
  const thread = document.getElementById("thread").value;
  const input = document.getElementById("msg");
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      thread_id: thread,
      message: text
    })
  });

  const data = await res.json();
  addMessage(data.response, "ai");
}

async function loadHistory() {
  const thread = document.getElementById("thread").value;
  const res = await fetch(`/history/${thread}`);
  const data = await res.json();

  box.innerHTML = "";
  data.history.forEach(m => {
    addMessage(m.content, m.type === "human" ? "user" : "ai");
  });
}


window.onload = loadHistory;

const input = document.getElementById("msg");

input.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();   // stop newline
    send();               // send message
  }
});

