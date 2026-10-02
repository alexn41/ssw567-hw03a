import requests
import unittest
from unittest.mock import Mock
from unittest.mock import patch

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
    


class testAPI(unittest.TestCase):

    @patch('requests.get')
    def test_API(self, mock_get):

        mock_get.side_effect = [Mock(json=Mock(return_value=[{'name': 'test-repository'}])),Mock(json=Mock(return_value=[
                {'a': 'b'},
                {'a': 'c'},
                {'a': 'd'}
            ]))
        ]

        result = getGitHubInfo("test-user-92929")

        self.assertEqual(result,("Repo: test-repository, Number of commits: 3"))

        self.assertEqual(mock_get.call_count, 2)


if __name__ == '__main__':
    unittest.main()
