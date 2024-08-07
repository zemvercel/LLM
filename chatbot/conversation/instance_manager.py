# conversation/instance_manager.py
import uuid

class InstanceManager:
    def __init__(self):
        self.instances = {}

    def create_instance(self):
        instance_id = str(uuid.uuid4())
        self.instances[instance_id] = []
        return instance_id

    def get_instance(self, instance_id):
        return self.instances.get(instance_id)
