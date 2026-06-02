import asyncio  # Asynchronous execution
from fastapi import FastAPI, WebSocket  # FastAPI for web APIs and WebSocket communication

# Import necessary services and data models
from pydantic_models.chat_body import ChatBody
from services.llm_service import LLMService
from services.sort_source_service import SortSourceService
from services.search_service import SearchService

# Initialize FastAPI app
app = FastAPI()

# Instantiate services
search_service = SearchService()
sort_source_service = SortSourceService()
llm_service = LLMService()

# WebSocket for real-time chat interaction
@app.websocket("/ws/chat")
async def websocket_chat_endpoint(websocket: WebSocket):
    await websocket.accept()  # Accept WebSocket connection

    try:
        await asyncio.sleep(0.1)  # Small delay for stability
        data = await websocket.receive_json()  # Receive JSON input
        query = data.get("query")  # Extract query from input

        # Perform web search and sort results
        search_results = search_service.web_search(query)
        sorted_results = sort_source_service.sort_sources(query, search_results)

        await asyncio.sleep(0.1)  # Delay before sending results
        await websocket.send_json({"type": "search_result", "data": sorted_results})  # Send sorted results

        # Stream AI response in chunks
        for chunk in llm_service.generate_response(query, sorted_results):
            await asyncio.sleep(0.1)
            await websocket.send_json({"type": "content", "data": chunk})

    except Exception as e:
        print(f"Unexpected error occurred: {e}")  # Handle errors
    finally:
        await websocket.close()  # Close connection

# REST API for chat
@app.post("/chat")
def chat_endpoint(body: ChatBody):
    """Handles chat via REST API (non-WebSocket)"""
    search_results = search_service.web_search(body.query)
    sorted_results = sort_source_service.sort_sources(body.query, search_results)
    response = llm_service.generate_response(body.query, sorted_results)
    return response  # Return AI response
