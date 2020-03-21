from ...src.numfinder.NumFinder import NumFinder
import unittest 
"""
MichaelShen@MichaelShen-UV9VAQ9I MINGW64 /d
$ python -m unittest mooc-software-testing.test.numfinder.test_numfinder -v
$ coverage run -m  mooc-software-testing.test.numfinder.test_numfinder
$ coverage report 
$ coverage html 
"""
class Test(unittest.TestCase):
    def test1(self):
        foo = NumFinder([2,5,9,1,100,20])
        self.assertEqual(foo.find(),(100,1))
       
        
if __name__ == '__main__':
    unittest.main()
    
"""
$ coverage report -m
Name                                                        Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------
D:\mooc-software-testing\__init__.py                            0      0   100%
D:\mooc-software-testing\src\__init__.py                        0      0   100%
D:\mooc-software-testing\src\numfinder\NumFinder.py            12      0   100%
D:\mooc-software-testing\src\numfinder\__init__.py              0      0   100%
D:\mooc-software-testing\test\__init__.py                       0      0   100%
D:\mooc-software-testing\test\numfinder\__init__.py             0      0   100%
D:\mooc-software-testing\test\numfinder\test_numfinder.py       8      0   100%
-----------------------------------------------------------------------------------------
TOTAL                                                          20      0   100%

"""