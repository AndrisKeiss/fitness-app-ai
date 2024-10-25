# Fitness AI - Streamlit Application

## App Description

Fitness AI is a Streamlit-based web application that allows users to interact with an AI assistant. The application integrates with Astra DB for data storage and uses an external AI service for generating responses.

## File Descriptions

- `main.py`: The entry point of the Streamlit application. It sets up the main UI and coordinates between different modules.
- `db.py`: Handles all database operations, including connections to Astra DB and data queries.
- `form_submit.py`: Manages the form submission functionality, processing user inputs and storing them in the database.
- `ai.py`: Integrates with the external AI service, sending requests and processing responses.
- `profiles.py`: Handles user profile management, including creation, updating, and retrieval of user information.
- `__init__.py`: Python package initializer, may contain package-level configurations or imports.
- `requirements.txt`: Lists all Python dependencies required for the project.
- `sample.env`: Provides a template for the required environment variables.
- `langflows>>*.json`: Langflow JSON files containing workflow schemas used in astra.datastax.com. These files define the AI processing workflows for the application.

You will also need to create a vector database in the Astra DB UI and supply the necessary credentials to the `.env` file.

## Acknowledgements

- [Tech with Tim](https://www.youtube.com/@TechWithTim)
