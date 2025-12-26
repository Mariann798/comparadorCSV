import unittest
import os
import pandas as pd
from main import compare_files

class TestCompareFiles(unittest.TestCase):

    def setUp(self):
        """Set up test files."""
        self.file1_path = 'test_file1.csv'
        self.file2_path = 'test_file2.csv'
        self.column = 'Emails'

        data1 = {self.column: ['a@a.com', 'b@b.com', 'c@c.com']}
        df1 = pd.DataFrame(data1)
        df1.to_csv(self.file1_path, index=False, sep=';')

        data2 = {self.column: ['b@b.com', 'c@c.com', 'd@d.com']}
        df2 = pd.DataFrame(data2)
        df2.to_csv(self.file2_path, index=False, sep=';')

    def tearDown(self):
        """Tear down test files."""
        os.remove(self.file1_path)
        os.remove(self.file2_path)

    def test_compare_files(self):
        """Test the compare_files function."""
        result = compare_files(self.file1_path, self.file2_path, self.column)
        self.assertEqual(sorted(result), sorted(['a@a.com']))

if __name__ == '__main__':
    unittest.main()
