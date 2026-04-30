
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import json
from thefuzz import fuzz

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["["*"]"], 
)




app = FastAPI()

response = []

def respond(chat):
    best_match = None
    highest_score = 0
    
    for item in response:
        score = fuzz.ratio(item['question'], chat)
        if score > highest_score:
            highest_score = score
            best_match = item
            
    if highest_score > 75:
        return best_match['answer']
    
    return "Sorry, I don't understand that yet 😩"


def save_data():
    with open('response.json', 'w') as file:
        json.dump(response, file, indent=4)


def load_data():
    try:
        with open('response.json', 'r') as file:
            stored_data = json.load(file)
            response.extend(stored_data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

load_data()

@app.get("/")
def home():
    return {"message": "HiveBot API is running 🚀"}


@app.get("/chat")
def chat(message: str):
    reply = respond(message.strip().lower())
    return {"reply": reply}


@app.post("/teach")
def teach(question: str, answer: str):
    question = question.strip().lower()
    answer = answer.strip().lower()

    for item in response:
        if item['question'] == question:
            return {"message": "I already know that 😅"}

    response.append({
        "question": question,
        "answer": answer
    })

    save_data()
    return {"message": "Bot learned successfully 🎉"}
