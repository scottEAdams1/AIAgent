import unittest
from functions.get_files_info import get_files_info

class TestCalculator(unittest.TestCase):
    def test_directory_dot(self):
        result = get_files_info("calculator", ".")
        print(result)
    def test_directory_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)
    def test_directory_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)
    def test_directory_outer(self):
        result = get_files_info("calculator", "../")
        print(result)

if __name__ == "__main__":
    unittest.main()