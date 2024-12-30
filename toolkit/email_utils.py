import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_training_complete_email(recipient_email, model_name, training_folder):
    # Get email credentials from environment variables
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("NOTIFICATION_EMAIL")
    sender_password = os.getenv("NOTIFICATION_EMAIL_PASSWORD")
    
    if not sender_email or not sender_password:
        print("Warning: Email credentials not found in environment variables. Skipping notification.")
        return
        
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = f"Training Complete: {model_name}"
    
    body = f"""
    Your model training has completed!
    
    Model Name: {model_name}
    Training Folder: {training_folder}
    
    This is an automated notification.
    """
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Create server connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message)
        server.quit()
        print(f"Training completion notification sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email notification: {str(e)}") 