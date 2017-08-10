#Python单元测试 unittest
#下面演示了一个非常简单的单元测试，测试2+2=4
import unittest
class TestAddition(unittest.TestCase):
    #这两个函数在每个测试的开始和结束都会运行一次，而不是把类中所有的测试都当做一个整体在开始或者结束的时候各运行一次
    def setUp(self):
        print("Setting up the test")
    
    def tearDown(self):
        print("Tearing down the test")
        
    def test_teoPlusTwo(self):
        total = 2+2
        self.assertEqual(4,total)
        
if __name__ == '__main__':
    unittest.main()
