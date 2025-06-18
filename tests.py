import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestCalculator(unittest.TestCase):
    def test_file_content_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)
    def test_file_content_pkg_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
    def test_file_content_bin_cat(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertIn("Error", result)
        print(result)

if __name__ == "__main__":
    unittest.main()