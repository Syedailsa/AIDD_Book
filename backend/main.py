from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from backend.agents.rag_agent import RoboticsProfessor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"status": "Physical AI Agent Ready"}

@app.websocket("/ws/v1/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    agent = RoboticsProfessor()
    chat_history = []
    try:
        while True:
            data = await websocket.receive_text()
            response_text = agent.chat(user_message=data, history=chat_history)
            chat_history.append({"role": "user", "content": data})
            chat_history.append({"role": "assistant", "content": response_text})
            await websocket.send_json({"response": response_text})
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
