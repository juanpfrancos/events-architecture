import strawberry
from typing import List
from graphql_types import Event, Notification
from resolvers import (
    resolve_create_event,
    resolve_get_events,
    resolve_get_event_by_id,
    resolve_update_event,
    resolve_delete_event,
    resolve_send_message,
    resolve_full_text_search,
)

@strawberry.type
class Query:
    events: List[Event] = strawberry.field(resolver=resolve_get_events)
    event: Event = strawberry.field(resolver=resolve_get_event_by_id)
    full_text_search: List[Event] = strawberry.field(resolver=resolve_full_text_search)

@strawberry.type
class Mutation:
    create_event: Event = strawberry.field(resolver=resolve_create_event)
    update_event: Event = strawberry.field(resolver=resolve_update_event)
    delete_event: str = strawberry.field(resolver=resolve_delete_event)
    send_notification: str = strawberry.field(resolver=resolve_send_message)

schema = strawberry.Schema(query=Query, mutation=Mutation)
