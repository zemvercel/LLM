# conversation/conversation_manager.py
from memory.memory_manager.py import MemoryManager

class ConversationManager:
    def __init__(self):
        self.memory_manager = MemoryManager()

    def add_message(self, instance_id, message):
        self.memory_manager.add_conversation(instance_id, message)

    def get_conversation(self, instance_id):
        return self.memory_manager.get_conversation(instance_id)
