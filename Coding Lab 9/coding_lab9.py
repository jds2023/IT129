class User: 
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0 
    
    def describe_user(self):
        print(f"\nUsername: {self.username}. Login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(f"\nLogin attempt from {self.username}, attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nLogin attempts for {self.username} have been reset to {self.login_attempts}")

user1 = User("JustinS", "Sun%4645!light")

user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts() 
