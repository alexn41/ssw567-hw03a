import requests
import unittest

def getGitHubInfo(user):
    profile = f'https://api.github.com/users/{user}/repos'
    x = requests.get(profile)
    y = x.json()
    for i in y:
        repo = f'https://api.github.com/repos/{user}/{i['name']}/commits'
        a = requests.get(repo)
        b = a.json()
        commits = 0
        for j in b:
            commits += 1
        repoInfo = (f'Repo: {i['name']}, Number of commits: {commits}')
    print(repoInfo)
    return repoInfo
    
getGitHubInfo("cat")    

class testAPI(unittest.TestCase):
    def test_API(self):
        self.assertEqual(getGitHubInfo("test-user-92929"),("Repo: test-repository, Number of commits: 3"))
        self.assertEqual(getGitHubInfo("cat"),("Repo: cat.github.io, Number of commits: 26"))


if __name__ == '__main__':
    unittest.main()