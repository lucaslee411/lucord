from sqlalchemy.orm import Session
import models

def create_user(db: Session, username: str, password: str):
    user = models.User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_server(db: Session, name: str, owner_id: int):
    server = models.Server(name=name, owner_id=owner_id)
    db.add(server)
    db.commit()
    db.refresh(server)
    return server

def create_channel(db: Session, name: str, server_id: int):
    channel = models.Channel(name=name, server_id=server_id)
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel

def create_message(db: Session, content: str, user_id: int, channel_id: int):
    message = models.Message(content=content, user_id=user_id, channel_id=channel_id)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
