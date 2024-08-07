import unittest
from rag.rag_retriever import RAGRetriever
from config import PDF_PATH

class TestRAGRetriever(unittest.TestCase):
    def test_retrieve(self):
        retriever = RAGRetriever(PDF_PATH)
        result = retriever.retrieve("What is the content of the PDF?")
        self.assertIn("expected content", result)  # Replace "expected content" with actual text from the PDF

if __name__ == "__main__":
    unittest.main()
