from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Server is running!"}

@app.post("/users/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    return crud.create_user(db=db, username=username, password=password)

@app.post("/servers/")
def create_server(name: str, owner_id: int, db: Session = Depends(get_db)):
    return crud.create_server(db=db, name=name, owner_id=owner_id)

@app.post("/channels/")
def create_channel(name: str, server_id: int, db: Session = Depends(get_db)):
    return crud.create_channel(db=db, name=name, server_id=server_id)

@app.post("/messages/")
def create_message(content: str, user_id: int, channel_id: int, db: Session = Depends(get_db)):
    return crud.create_message(db=db, content=content, user_id=user_id, channel_id=channel_id)
