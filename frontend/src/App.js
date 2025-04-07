import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:5000/chat", { message });
    setResponse(res.data.response);
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>DevOps Chatbot</h1>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask a DevOps question..."
        style={{ width: "60%", padding: "10px", fontSize: "16px" }}
      />
      <button onClick={sendMessage} style={{ marginLeft: "10px", padding: "10px 20px" }}>
        Send
      </button>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
}

export default App;
