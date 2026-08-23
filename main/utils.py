# utils/wa_api.py
import requests
from urllib.parse import quote

WAWP_BASE_URL = "https://wawp.net/wp-json/awp/v1/send"
INSTANCE_ID = "307CFB8A7EC9"      # replace with your Wawp instance_id
ACCESS_TOKEN = "Fu6JHEUkSsMq8j"    # replace with your Wawp access token

def send_wa_message(chat_id: str, message: str) -> dict:
    """
    Send a WhatsApp message via Wawp API.

    Args:
        chat_id (str): WhatsApp chat ID, e.g., "447441429009"
        message (str): Message text to send

    Returns:
        dict: API response as JSON
    """
    # URL encode the message
    encoded_message = quote(message)

    # Construct the request URL with query parameters
    url = f"{WAWP_BASE_URL}?instance_id={INSTANCE_ID}&access_token={ACCESS_TOKEN}&chatId={chat_id}&message={encoded_message}"

    try:
        response = requests.post(url)
        response.raise_for_status()
        return response.json()  # return JSON response
    except requests.exceptions.RequestException as e:
        # Return error details
        return {"success": False, "error": str(e)}
