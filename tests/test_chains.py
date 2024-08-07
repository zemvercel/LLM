import unittest
from chains.chain_1 import Chain1
from chains.chain_2 import Chain2

class TestChains(unittest.TestCase):
    def test_chain1(self):
        chain = Chain1()
        self.assertEqual(chain.process("input"), "Chain1 processed: input")

    def test_chain2(self):
        chain = Chain2()
        self.assertEqual(chain.process("input"), "Chain2 processed: input")

if __name__ == "__main__":
    unittest.main()
