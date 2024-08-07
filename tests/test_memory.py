import unittest
import os
import json
from memory.longterm_memory import LongTermMemory

class TestLongTermMemory(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_chat_history.json"
        self.memory = LongTermMemory(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_and_retrieve(self):
        user_id = "test_user"
        message = "Hello, this is a test message."
        
        self.memory.save(user_id, message)
        retrieved_messages = self.memory.retrieve(user_id)
        
        self.assertIn(message, retrieved_messages)

if __name__ == "__main__":
    unittest.main()
