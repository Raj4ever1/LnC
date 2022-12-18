class UserData:
    def __init__(self, email = None, first_name = None, last_name = None, token = None, role = 4):
        self.email = email if email else None
        self.first_name = first_name if first_name else None
        self.last_name = last_name if last_name else None
        self.token = token if token else None
        self.role = role if role else None
