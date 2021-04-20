from .user import User

users = [User(1, 'John', 'asdf')]

username_mapping = {u.username: u for u in users}
print(username_mapping.get('John'))
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identiy(payload):
    user_id = payload['identity']
    print(user_id)
    return userid_mapping.get(user_id, None)

# if __name__ == '__main__':
#     w=username_mapping.get('John', None)
# print(w.password)