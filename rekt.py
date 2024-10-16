import requests
import time

def read_tokens(filename="query.txt"):
    """Read auth-token values from query.txt"""
    tokens = []
    try:
        with open(filename, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"{filename} not found.")
    return tokens

def fetch_tasks(auth_token):
    """Fetch tasks from the API"""
    url = "https://rekt-mini-app.vercel.app/api/quests/user"
    headers = {
        "accept": "application/json, text/plain, */*",
        "auth-token": auth_token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tasks = response.json().get('userQuests', [])
        return tasks
    else:
        print(f"Failed to fetch tasks: {response.status_code}, {response.text}")
        return []

def complete_task(auth_token, quest_id):
    """Complete the task by sending a POST request to complete the task"""
    url = f"https://rekt-mini-app.vercel.app/api/quests/complete/{quest_id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "auth-token": auth_token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        quest_status = data.get('questStatus', 'No quest status')
        print(f"Task completion status: {quest_status}")
        return quest_status == "COMPLETED"
    else:
        print("Join Grup: https://t.me/dasarpemulung")
        print(f"Failed to complete task: {response.status_code}, {response.text}")
        return False

def claim_task(auth_token, quest_id):
    """Claim the task reward by sending a POST request"""
    url = f"https://rekt-mini-app.vercel.app/api/quests/claim/{quest_id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "auth-token": auth_token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Join Grup: https://t.me/dasarpemulung")
        quest_status = data.get('questStatus', 'No quest status')
        print(f"Task claim status: {quest_status}")
    else:
        print("Join Grup: https://t.me/dasarpemulung")
        print(f"Failed to claim task: {response.status_code}, {response.text}")

def perform_task_workflow():
    """Perform task workflow for multiple auth-tokens"""
    display_banner()
    tokens = read_tokens()
    for token in tokens:
        tasks = fetch_tasks(token)
        for task in tasks:
            if task.get('questStatus') == "NOT_COMPLETED":
                quest_id = task['quest']['id']
                print(f"Completing task: {task['quest']['name']}")
                if complete_task(token, quest_id):
                    time.sleep(15)  # Wait for 15 seconds before claiming
                    claim_task(token, quest_id)

def display_banner():
    """Display the static banner header with strikethrough effect"""
    print("""
【Ｄａｓａｒ　Ｐｅｍｕｌｕｎｇ】
Youtube : Dasar Pemulung
Github  : https://github.com/dwisyafriadi2
Note    : Jangan edit nanti error ya jancok.
Join Grup: https://t.me/dasarpemulung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

if __name__ == "__main__":
    perform_task_workflow()