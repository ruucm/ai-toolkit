from toolkit.email_utils import send_training_complete_email
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_email_notification():
    # Get email credentials from environment
    sender_email = os.getenv("NOTIFICATION_EMAIL")
    sender_password = os.getenv("NOTIFICATION_EMAIL_PASSWORD")
    recipient_email = os.getenv("NOTIFICATION_RECIPIENT_EMAIL")
    
    if not sender_email or not sender_password:
        print("Error: Email credentials not found in .env file")
        return
        
    if not recipient_email:
        print("Error: Recipient email not found in .env file")
        return
        
    print(f"Using sender email: {sender_email}")
    print(f"Using recipient email: {recipient_email}")
    
    try:
        send_training_complete_email(
            recipient_email=recipient_email,
            model_name="TEST_MODEL",
            training_folder="TEST_FOLDER"
        )
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {str(e)}")

if __name__ == "__main__":
    test_email_notification() 