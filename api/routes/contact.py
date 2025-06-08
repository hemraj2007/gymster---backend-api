from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.contact import ContactCreate, ContactResponse
from api.crud import contact as crud_contact

router = APIRouter()

@router.post("/create", response_model=ContactResponse)
def create_contact(form: ContactCreate, db: Session = Depends(get_db)):
    """
    Create a new contact entry and send email notification.
    """
    return crud_contact.create_contact(db, form)

@router.get("/all", response_model=list[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    """
    Get all contact entries.
    """
    return crud_contact.get_all_contacts(db)

@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    Get a single contact by ID.
    """
    contact = crud_contact.get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/delete/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    Delete a contact by ID.
    """
    deleted = crud_contact.delete_contact(db, contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}
