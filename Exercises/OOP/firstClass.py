class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 
        user.following += 1


user_1 = User("001", "james")
user_2 = User("002", "barbara")

print(user_1.id, ": ", user_1.username)
print(user_2.id, ": ", user_2.username)
