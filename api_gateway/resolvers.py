import requests
from typing import List
from graphql_types import Event

BASE_URL_EVENTS = "http://events_service:8008/events"
BASE_URL_NOTIFICATIONS = "http://notification_service:8007/send_message"

async def resolve_get_events() -> List[Event]:
    response = requests.get(BASE_URL_EVENTS)
    events = response.json()
    return [Event(**event) for event in events]

async def resolve_get_event_by_id(event_id: int) -> Event:
    response = requests.get(f"{BASE_URL_EVENTS}/{event_id}")
    event = response.json()
    return Event(**event)

async def resolve_create_event(title: str, description: str, location: str, start_time: str, end_time: str, capacity: int) -> Event:
    payload = {
        "title": title,
        "description": description,
        "location": location,
        "start_time": start_time,
        "end_time": end_time,
        "capacity": capacity,
    }
    response = requests.post(BASE_URL_EVENTS, json=payload)
    event = response.json()
    return Event(**event)

async def resolve_update_event(event_id: int, title: str, description: str, location: str, start_time: str, end_time: str, capacity: int, status: str) -> Event:
    payload = {
        "title": title,
        "description": description,
        "location": location,
        "start_time": start_time,
        "end_time": end_time,
        "capacity": capacity,
        "status": status,
    }
    response = requests.put(f"{BASE_URL_EVENTS}/{event_id}", json=payload)
    event = response.json()
    return Event(**event)

async def resolve_delete_event(event_id: int) -> str:
    response = requests.delete(f"{BASE_URL_EVENTS}/{event_id}")
    return "Event deleted successfully" if response.status_code == 204 else response.text

async def resolve_full_text_search(query: str) -> List[Event]:
    response = requests.get(f"{BASE_URL_EVENTS}/search/full-text", params={"query": query})
    events = response.json()
    return [Event(**event) for event in events]

async def resolve_send_message(phone: str, message: str) -> str:
    payload = {"phone": phone, "message": message}
    response = requests.post(BASE_URL_NOTIFICATIONS, json=payload)
    return "Notification sent successfully" if response.status_code == 200 else response.text
