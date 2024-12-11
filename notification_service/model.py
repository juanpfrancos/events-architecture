from pydantic import BaseModel

# Define the model for the request body (phone and message)
class MessageRequest(BaseModel):
    phone: str
    message: str
