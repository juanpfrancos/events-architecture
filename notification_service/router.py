from fastapi import APIRouter, HTTPException
from model import MessageRequest
from message import send_message

router = APIRouter()


"""
Endpoint to receive whatsapp number and message to send
"""
@router.post("/send_message/")
async def send_message_endpoint(request: MessageRequest):
    try:
        result = send_message(request.phone, request.message)
        return {"message": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
