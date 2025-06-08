from sqlalchemy.orm import Session
from api.database.models.contact import Contact
from api.database.schemas.contact import ContactCreate
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  # .env file se environment variables load karega

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    # Email send karein
    send_email(db_contact)

    return db_contact

def send_email(contact: Contact):
    email_address = os.getenv("EMAIL_HOST_USER")
    email_password = os.getenv("EMAIL_HOST_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = f"New Contact Message: {contact.subject}"
    msg["From"] = email_address
    msg["To"] = email_address  # Apne aapko email bhejna
    msg.set_content(
        f"""
        👤 Name: {contact.name}
        📧 Email: {contact.email}
        📌 Subject: {contact.subject}
        📝 Message: {contact.message}
        """
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email sending failed:", str(e))


def get_all_contacts(db: Session):
    return db.query(Contact).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
