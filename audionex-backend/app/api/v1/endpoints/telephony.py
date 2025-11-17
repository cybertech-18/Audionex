from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Start
from app.core.config import settings
from app.workers.telephony_worker import CallProcessor

router = APIRouter()

@router.post("/incoming-call")
async def handle_incoming_call(request: Request):
    """
    Handles incoming calls from Twilio.
    This webhook returns TwiML instructions to start a media stream.
    """
    twiml = VoiceResponse()
    
    # The <Start> verb tells Twilio to begin streaming the call's audio
    # to the WebSocket endpoint provided in the 'url'.
    start = Start()
    start.stream(url=f"wss://{settings.BASE_URL.replace('http://', '').replace('https://', '')}/api/v1/telephony/ws/{request.query_params.get('CallSid')}")
    twiml.append(start)

    # You can say something to the user while the WebSocket connects.
    twiml.say("Connecting you to the agent. Please wait a moment.")
    
    # The <Pause> verb is important to keep the call active while the
    # WebSocket connection is established.
    twiml.pause(length=20)

    return Response(content=str(twiml), media_type="application/xml")


@router.websocket("/ws/{call_sid}")
async def websocket_endpoint(websocket: WebSocket, call_sid: str):
    """
    WebSocket endpoint for Twilio Media Streams.
    """
    await websocket.accept()
    processor = CallProcessor(websocket, call_sid)
    
    try:
        while True:
            message = await websocket.receive_text()
            await processor.handle_message(message)
    except WebSocketDisconnect:
        print(f"WebSocket disconnected for call {call_sid}")
    except Exception as e:
        print(f"Error in WebSocket for call {call_sid}: {e}")
    finally:
        # Clean up resources if any
        print(f"Closing WebSocket for call {call_sid}")
