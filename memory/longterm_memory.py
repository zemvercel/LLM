import json
import os

class LongTermMemory:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump({}, file)

    def save(self, user_id, message):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        
        if user_id not in data:
            data[user_id] = []
        
        data[user_id].append(message)
        
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def retrieve(self, user_id):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        
        return data.get(user_id, [])
