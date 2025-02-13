from llama_index.core import VectorStoreIndex
from llama_index.core.schema import QueryBundle

class AgentWorkflow:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def get_response(self, question: str, knowledge_base: VectorStoreIndex):
        try:
            # Create a query engine
            query_engine = knowledge_base.as_query_engine()

            # Get the response
            response = query_engine.query(QueryBundle(question))

            return str(response)
        except Exception as e:
            return f'Sorry, I encountered an error while processing your question: {str(e)}'
