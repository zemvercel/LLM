# memory/memory_manager.py
import json
import os

class MemoryManager:
    def __init__(self, file_path='memory/storage.json'):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump({}, f)

    def load_memory(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_memory(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def add_conversation(self, instance_id, message):
        data = self.load_memory()
        if instance_id not in data:
            data[instance_id] = []
        data[instance_id].append(message)
        self.save_memory(data)

    def get_conversation(self, instance_id):
        data = self.load_memory()
        return data.get(instance_id, [])
