from bug_tracker.config import bug_tracker_db

class User:

    def __init__(self) -> None:
        self.user_tracker_collection =bug_tracker_db["user"]

        


    def create_user(self)->None:
        pass 


    def delete_user(self)->None:
        pass 

    def get_user(self)->None:
        pass 


    def list_user(self)->None:
        pass

    def update_user(self)->None:
        pass 

