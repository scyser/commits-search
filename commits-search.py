import requests

while True:
    try:
        repository = input("Enter repository link: ").split("/")
        owner = repository[-2]
        repo = repository[-1]
        break
    except Exception:
        print('Incorrect input!')


url = f"https://api.github.com/repos/{owner}/{repo}/commits"

search_query = input("Enter search query: ").lower()

def find_commits(url, search_query):

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        answer = []
        for commit in commits:
            if search_query in commit['commit']['message'].lower():
                answer.append(commit)

        return answer
    else:
        return f"Error! Status code: {response.status_code}"
    

print(find_commits(url, search_query))