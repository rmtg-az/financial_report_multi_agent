from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import logging


logger = logging.getLogger(__name__)


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FAISS_DIR = Path("faiss_index")


def create_vectorstore(pdf_path: Path) -> FAISS:
    """ Load a PDF, split it into chunks, generate embeddings,
    and save a FAISS vector store. """

    logger.info("Vector DB作成開始")

    try:

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        docs = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        vectorstore = FAISS.from_documents(
            docs,
            embeddings
        )

        vectorstore.save_local(FAISS_DIR)

        logger.info("Vector DB作成終了")

        return vectorstore

    except Exception as e:
        logger.exception("Vector DB作成に失敗しました")
        raise RuntimeError(
            f"Vector DB作成エラー: {e}"
        )


def load_vectorstore() -> FAISS:
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return FAISS.load_local(
        FAISS_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve_documents(question: str):
    vectorstore = load_vectorstore()

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    return docs