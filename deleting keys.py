user = {
    "user_name": "my_user",
    "password": "123456",
    "address": "ahmedabad",
    "e-mail": "mallik@gmail.com",
    "country": "India"
}
sensitive_info = ["password", "address"]

for i in sensitive_info:
    user.pop(i)

print(user)