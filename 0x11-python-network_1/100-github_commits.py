import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[1], sys.argv[2])
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        try:
            for i in range(min(10, len(commits))):
                commit = commits[i]
                commit_data = commit.get("commit")
                author_name = commit_data.get("author").get("name")
                sha = commit.get("sha")
                print("{}: {}".format(sha, author_name))
        except IndexError:
            print("Not enough commits found.")
    else:
        print("Error: Status code:", response.status_code)
