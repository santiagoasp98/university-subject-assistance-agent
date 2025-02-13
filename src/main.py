# ----------------------------------- #
# Imports
# ----------------------------------- #

import os
from pathlib import Path
from agent.workflow import AgentWorkflow
from ingestion.document_processor import DocumentProcessor
from llm.ollama_client import OllamaClient

# ----------------------------------- #
# Main function
# ----------------------------------- #

def main():
    print('Welcome to the University Subject Assistant!')

    while True:
        print('\nWhat do you need help with? (Type \'exit\' to quit)')
        subject = input('Enter subject name: ').strip()

        if subject.lower() == 'exit':
            break

        print('Please provide the path to your PDF files (comma-separated if multiple):')
        pdf_paths = input('PDF paths: ').strip().split(',')
        pdf_paths = [path.strip() for path in pdf_paths]

        # Validate PDF paths
        valid_paths = []
        for path in pdf_paths:
            if os.path.exists(path) and path.lower().endswith('.pdf'):
                valid_paths.append(path)
            else:
                print(f'Warning: Invalid or non-existing PDF path: {path}')

        if not valid_paths:
            print('No valid PDF files provided. Please try again.')
            continue

        try:
            # Initialize components
            llm_client = OllamaClient()
            doc_processor = DocumentProcessor(llm_client)
            agent = AgentWorkflow(llm_client)

            # Process documents
            knowledge_base = doc_processor.process_documents(valid_paths)

            # Start Q&A session
            print('\nDocuments processed! You can now ask questions about the subject.')
            print('\nType \'quit\' to end this session.')

            while True:
                question = input('\nYour question: ').strip()

                if question.lower() == 'quit':
                    break

                response = agent.get_response(question, knowledge_base)
                print('\nAssistant:', response)

            # Cleanup
            doc_processor.cleanup()
            print('\nSession ended. Knowledge base cleared.')

        except Exception as e:
            print(f'An error occurred: {str(e)}')
            continue

if __name__ == '__main__':
    main()