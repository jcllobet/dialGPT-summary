from fastapi import Response
import os
import vocode
from vocode.streaming.telephony.inbound_call_server import InboundCallServer
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.telephony import TwilioConfig
from vocode.streaming.models.agent import ChatGPTAgentConfig

vocode.api_key = os.getenv("VOCODE_API_KEY")

REPLIT_URL = f"https://{os.getenv('REPL_SLUG')}.{os.getenv('REPL_OWNER')}.repl.co"

if __name__ == "__main__":
  server = InboundCallServer(
    agent_config=ChatGPTAgentConfig(
      initial_message=BaseMessage(text="Hello! What can I help you with?"),
      prompt_preamble=
      "You are a helpful AI assistant. You respond in 10 words or less.",
    ),
    twilio_config=TwilioConfig(
      account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
      auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    ),
  )
  server.app.get("/")(lambda: Response(
    content=
    f"<div>Paste the following URL into your Twilio config: {REPLIT_URL}/vocode",
    media_type="text/html"))
  server.run(host="0.0.0.0", port=3000)

