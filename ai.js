async function fakeAIResponse(prompt) {}
async function fakeAIResponse(prompt) {
    const r = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });
    const data = await r.json();
    return data.response;
}
