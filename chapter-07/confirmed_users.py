# 首先创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户，知道没有未验证用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verify user: {current_user.title()}")
    confirmed_users.append(current_user)
# 显示所有的已验证用户
print("\nThe following users have been confirmed.")
for user in confirmed_users:
    print(user.title())