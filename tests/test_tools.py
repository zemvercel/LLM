import unittest
from tools.tool_1 import Tool1
from tools.tool_2 import Tool2

class TestTools(unittest.TestCase):
    def test_tool1(self):
        tool = Tool1()
        self.assertEqual(tool.execute("test"), "Tool1 executed with query: test")

    def test_tool2(self):
        tool = Tool2()
        self.assertEqual(tool.execute("test"), "Tool2 executed with query: test")

if __name__ == "__main__":
    unittest.main()
