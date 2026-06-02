import google.generativeai as genai  # Import Gemini AI
from config import Settings  # Import API settings

# Load API settings
settings = Settings()

class LLMService:
    """Handles interaction with Gemini AI to generate responses based on search results."""

    def __init__(self):
        # Configure Gemini API with API key
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")  # Load the AI model

    def generate_response(self, query: str, search_results: list[dict]):
        """Generates an AI response using search results as context."""

        # Combine search results into context text
        context_text = "\n\n".join(
            [
                f"Source {i+1} ({result['url']}):\n{result['content']}"
                for i, result in enumerate(search_results)
            ]
        )

        # Formulate the prompt
        full_prompt = f"""
        Context from web search:
        {context_text}

        Query: {query}

        Please provide a comprehensive, detailed, well-cited accurate response using the above context. 
        Think and reason deeply. Ensure it answers the query the user is asking. Do not use your knowledge until it is absolutely necessary.
        """

        # Stream the response from the AI model
        response = self.model.generate_content(full_prompt, stream=True)

        # Yield response chunks to handle streaming
        for chunk in response:
            yield chunk.text
