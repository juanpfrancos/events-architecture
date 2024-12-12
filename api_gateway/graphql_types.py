import strawberry

@strawberry.type
class Event:
    id: int
    title: str
    description: str
    location: str
    start_time: str
    end_time: str
    capacity: int
    attendees_registered: int
    status: str
    created_at: str
    updated_at: str

@strawberry.type
class Notification:
    phone: str
    message: str
