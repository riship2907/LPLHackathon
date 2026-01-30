export function connectWebSocket(onMessage) {
    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = (event) => {
        onMessage(JSON.parse(event.data));
    };
    return ws;
}
