from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schema import EventCreate, EventUpdate, EventResponse, EventStatus
from model import Event
from session import SessionLocal
from elasticsearch import Elasticsearch

es_client = Elasticsearch("http://elasticsearch:9200")

router = APIRouter()

NOT_FOUND = HTTPException(status_code=404, detail="Event not found")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    event_dict = event.dict()
    event_dict["id"] = new_event.id
    es_client.index(index="events", id=new_event.id, document=event_dict)
    return new_event

@router.get("/", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise NOT_FOUND
    return event

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise NOT_FOUND
    for key, value in event.model_dump(exclude_unset=True).items():
        if key == "status" and isinstance(value, EventStatus):
            value = value.value.upper()
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)

    es_client.update(index="events", id=event_id, doc=event.dict(exclude_unset=True))
    return db_event



@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise NOT_FOUND
    db.delete(db_event)
    db.commit()

    es_client.delete(index="events", id=event_id, ignore=[404])
    return None