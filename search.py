import requests

def search_github_user(username):
    url = f"https://api.github.com/search/users?q={username}"
    response = requests.get(url)
    if response.status_code == 200:
        users = response.json().get('items', [])
        if users:
            for user in users:
                print(f"Login: {user['login']}, URL: {user['html_url']}")
        else:
            print("No users found.")
    else:
        print(f"Failed to search for user: {response.status_code}")

# Example usage:
search_github_user("Sayed Huzaifa Mumit")
