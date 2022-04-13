current_users = ['Mariana','serik','Julia','SONIA','nastia']

lower_currentusers = []

for current_user in current_users:
    lower_currentusers.append(current_user.lower())

new_users = ['olena','Sonia','julia','katia']

for new_user in new_users:
    if new_user.lower() in lower_currentusers:
        print(f'The login {new_user} is not available. Please try another one')
    else:
        print(f'The login {new_user} is available')