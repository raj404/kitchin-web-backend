from fastapi import  Depends, APIRouter, status, HTTPException
from pydantic.schema import schema
from database import engine
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from models import models
from schemas import demo
import database
import logging
import constants
from datetime import datetime

router = APIRouter(
    tags = ['Authentication']
)

get_db = database.get_db


@router.post('/user')
def create_user(user_request: demo.User, db: Session = Depends(get_db)):
    user_check = db.query(models.User).filter(models.User.email_id == user_request.email).first()
    if not user_check:
        new_user = models.User(name=user_request.name,
                            email_id=user_request.email,
                            password=user_request.password,
                            contact_no = user_request.contact_no)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        common_msg = demo.ResponseCommonMessage(status=status.HTTP_200_OK, message= "SUCCESS")
        return {"message": common_msg,"result":new_user }
    raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail=f"User exist already!!")
    

@router.post('/login', response_model=demo.ShowUser)
def login(user_request: demo.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email_id == user_request.email, models.User.password == user_request.password).first()
    if user:
        return user.__dict__
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")