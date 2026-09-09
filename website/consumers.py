import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VisitorCountConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'portfolio_visitors'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send an increment event to everyone
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'visitor_update',
                'action': 'join'
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Send a decrement event to everyone
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'visitor_update',
                'action': 'leave'
            }
        )

    # Receive message from room group
    async def visitor_update(self, event):
        action = event['action']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'action': action
        }))
