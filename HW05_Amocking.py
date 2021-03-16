import unittest
from unittest.mock import Mock, MagicMock
from HW04a import Commits

class Mocktest(unittest.TestCase):
    @Mock('requests.get')
    def test_Commits(self, mockedReq):
        mockedReq.return_value = MagicMock('MockSuccess')
        commits = Commits(self.username, self.repo_name)
        self.assertEqual(commits, 'MockSuccess')

if __name__ == '__main__':
    unittest.main()