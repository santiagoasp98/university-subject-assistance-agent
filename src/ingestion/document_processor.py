from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


class DocumentProcessor:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.temp_dir = Path('temp')
        self.temp_dir.mkdir(exist_ok=True)

        embed_model = HuggingFaceEmbedding(
            model_name='BAAI/bge-small-en-v1.5')
        Settings.embed_model = embed_model

    def process_documents(self, pdf_paths: list[str]) -> VectorStoreIndex:
        try:
            # Copy PDFs to temp directory
            for pdf_path in pdf_paths:
                source = Path(pdf_path)
                dest = self.temp_dir / source.name
                with open(source, 'rb') as src, open(dest, 'wb') as dst:
                    dst.write(src.read())

            # Load documents
            documents = SimpleDirectoryReader(
                input_dir=str(self.temp_dir),
                filename_as_id=True
            ).load_data()

            # Create a node parser
            node_parser = SimpleNodeParser.from_defaults()

            # Parse documents into nodes
            nodes = []
            for doc in documents:
                parsed_nodes = node_parser.get_nodes_from_documents([doc])
                nodes.extend(parsed_nodes)

            # Create index from nodes
            index = VectorStoreIndex(nodes)
            return index

        except Exception as e:
            raise Exception(f'Error processing documents: {str(e)}')

    def cleanup(self):
        '''Remove all temporary files'''
        for file in self.temp_dir.glob('*.pdf'):
            file.unlink()
