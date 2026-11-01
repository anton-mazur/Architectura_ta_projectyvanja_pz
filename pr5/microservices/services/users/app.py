from fastapi import FastAPI, HTTPException

app = FastAPI(title="Users service")
USERS = {1: {"id": 1, "email": "user@example.com"}}

@app.get("/health")
def health(): return {"status": "ok"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in USERS: raise HTTPException(404, "user not found")
    return USERS[user_id]
