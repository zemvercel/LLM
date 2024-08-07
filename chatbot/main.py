# main.py
from conversation.conversation_manager import ConversationManager
from conversation.instance_manager import InstanceManager
from utils.api_keys import get_api_key

def main():
    instance_manager = InstanceManager()
    conversation_manager = ConversationManager()

    # Create a new conversation instance
    instance_id = instance_manager.create_instance()
    print(f"New conversation instance created with ID: {instance_id}")

    # Simulate a conversation
    conversation_manager.add_message(instance_id, "Hello, how can I help you today?")
    conversation_manager.add_message(instance_id, "I need information about modular programming.")

    # Retrieve conversation history
    history = conversation_manager.get_conversation(instance_id)
    for message in history:
        print(message)

if __name__ == "__main__":
    main()
