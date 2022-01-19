from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import user_model as model
from schemas import user_schema
from utilities import database

router = APIRouter(prefix="/user", tags=["User"],)


@router.get("/", response_model=List[user_schema.UserResponse])
def get_create(db:  Session = Depends(database.get_db)):
    try:
        users = db.query(model.UserModel).all()
        return users
    except Exception as e:
        print(e)


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_user(request: user_schema.UserRequest,
                db:  Session = Depends(database.get_db)):
    try:
        new_user = model.UserModel(**request.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print(e)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED,)
def update_user(id: int, request: user_schema.UserRequest,
                db: Session = Depends(database.get_db)):
    try:
        user = db.query(model.UserModel).filter(model.UserModel.id == id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"user with id {id} not found")
        user.update(request.dict())
        db.commit()
        return {"message": "User updated successfully"}

    except Exception as e:
        print(e)
