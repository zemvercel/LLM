from langchain import LangChain
from config import API_KEYS, SYSTEM_PROMPT, PDF_PATH, CHAT_HISTORY_FILE
from memory.longterm_memory import LongTermMemory
from tools.tool_1 import Tool1
from tools.tool_2 import Tool2
from chains.chain_1 import Chain1
from chains.chain_2 import Chain2
from rag.rag_retriever import RAGRetriever

def main():
    # Initialize LangChain with the desired LLM and system prompt
    langchain = LangChain(api_key=API_KEYS["google_gemini"], system_prompt=SYSTEM_PROMPT)

    # Initialize components
    memory = LongTermMemory(CHAT_HISTORY_FILE)
    tool1 = Tool1()
    tool2 = Tool2()
    chain1 = Chain1()
    chain2 = Chain2()
    rag_retriever = RAGRetriever(PDF_PATH)

    # Example usage
    user_input = "Tell me about the weather."
    response = langchain.generate(user_input, memory=memory, tools=[tool1, tool2], chains=[chain1, chain2], retriever=rag_retriever)
    print(response)

if __name__ == "__main__":
    main()
