from llama_index.core import VectorStoreIndex
from llama_index.core.schema import QueryBundle


class AgentWorkflow:
    def __init__(self, llm_client, knowledge_base: VectorStoreIndex):
        self.llm_client = llm_client
        # Create a query engine
        self.query_engine = knowledge_base.as_query_engine()

    def get_response(self, question: str):
        try:
            # Get the response
            response = self.query_engine.query(QueryBundle(question))

            return str(response)
        except Exception as e:
            return 'Sorry, I encountered an error while processing your '\
                   f'question: {str(e)}'
