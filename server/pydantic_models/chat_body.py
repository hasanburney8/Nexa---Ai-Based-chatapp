from pydantic import BaseModel  # Pydantic for data validation

# Data model for chat query input
class ChatBody(BaseModel):
    query: str  # The user's question/query
