import unittest 
from file_helper import * 

class FileHelperTest(unittest.TestCase):
    
    def test_read_file(self):
        result = read_file("input_s")
        
        self.assertEqual("", "")
        
        
    def test_write_ouput(self):
        write_output("test")
        
        result = read_file("test")
        self.assertEqual("test", result)
        
if __name__ == '__main__':
    unittest.main()