import asyncio
import websockets
from typing import Set
from websockets.protocol import State

class WebSocketObserver:
    def __init__(self):
        self.clients: Set[websockets.WebSocketServerProtocol] = set()
    
    def subscribe(self, client):
        """Add client to observers"""
        self.clients.add(client)
        print(f"Client subscribed. Total clients: {len(self.clients)}")
    
    def unsubscribe(self, client):
        """Remove client from observers"""
        self.clients.remove(client)
        print(f"Client unsubscribed. Total clients: {len(self.clients)}")
    
    async def notify(self, message: str, sender=None):
        """Notify all connected clients"""
        if self.clients:
            tasks = []
            for client in self.clients:
                if (client != sender) and client.state == websockets.protocol.State.OPEN:
                    tasks.append(client.send(message))
            await asyncio.gather(*tasks, return_exceptions=True)

