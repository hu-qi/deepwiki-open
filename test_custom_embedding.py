
import os
import logging
from dotenv import load_dotenv
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def test_embedding():
    api_key = os.getenv("CUSTOM_OPENAI_API_KEY")
    base_url = os.getenv("CUSTOM_OPENAI_BASE_URL")
    model = os.getenv("CUSTOM_OPENAI_EMBEDDING_MODEL")

    logger.info(f"Testing embedding with:")
    logger.info(f"API Key: {api_key[:5]}...{api_key[-5:] if api_key else 'None'}")
    logger.info(f"Base URL: {base_url}")
    logger.info(f"Model: {model}")

    if not api_key or not base_url or not model:
        logger.error("Missing environment variables. Please check your .env file.")
        return

    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        logger.info("Sending embedding request...")
        response = client.embeddings.create(
            input="Hello, world!",
            model=model
        )
        
        logger.info("Response received!")
        logger.info(f"Object type: {type(response)}")
        logger.info(f"Raw response: {response}")
        
        if response.data and len(response.data) > 0:
            embedding = response.data[0].embedding
            logger.info(f"Embedding length: {len(embedding)}")
            logger.info(f"First 5 values: {embedding[:5]}")
        else:
            logger.error("No data in response")

    except Exception as e:
        logger.error(f"Error during embedding request: {e}")

if __name__ == "__main__":
    test_embedding()
