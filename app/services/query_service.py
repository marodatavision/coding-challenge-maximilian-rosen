from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from services.embedding_service import embeddings_model
from services.retrieval_service import retrieve, build_store

llm = ChatOpenAI(model_name=settings.llm_model_name, openai_api_key=settings.openai_api_key)

def answer_query(chunks_with_emb, query: str):
    store = build_store(chunks_with_emb)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=store.as_retriever())
    return qa.run(query)
