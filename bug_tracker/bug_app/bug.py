
from bug_tracker.config import bug_tracker_db
class Bug:


    def __init__(self) -> None:
        self.bug_tracker_collection =bug_tracker_db["bug"]

    def create_bug(self,bug):
        self.bug_tracker_collection.insert_one(bug)
        return bug

    def close_bug(self,bug,updated_bug)->None:
        pass
        return True

    def open_bug(self)->None:
        pass 

    def assign_bug_to_user(self)->None:
        pass

    def list_bug(self)->None:
        return self.bug_tracker_collection.find()


    def get_bug(self,):
        return {"bug_id":"1","bug_name":"demo_bug"}

    

