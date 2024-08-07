import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGRetriever:
    def __init__(self, pdf_path):
        self.knowledge_base = self.load_pdf(pdf_path)
        self.vectorizer = TfidfVectorizer().fit_transform(self.knowledge_base)

    def load_pdf(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return [text]

    def retrieve(self, query):
        query_vec = TfidfVectorizer().fit_transform([query])
        similarities = cosine_similarity(query_vec, self.vectorizer).flatten()
        most_similar_idx = similarities.argmax()
        return self.knowledge_base[most_similar_idx]
