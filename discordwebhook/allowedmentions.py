

class AllowedMentions():
    def __init__(self, users : bool = True, roles : bool = True, everyone : bool = True):
        self.users = users 
        self.roles = roles 
        self.everyone = everyone

        self.user_ids = []
    
    def to_dict(self):
        self.raw = {}

        self.raw["parse"] = []
        
        if self.users:
            self.raw["parse"].append("users")
        if self.roles:
            self.raw["parse"].append("roles")
        if self.everyone:
            self.raw["parse"].append("everyone")
        if self.user_ids != []:
            self.raw["users"] = self.user_ids
        
        return self.raw
    
    def add_user_id(self, user_id : int):
        self.user_ids.append(user_id)