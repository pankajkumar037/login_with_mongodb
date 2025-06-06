from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    school: str
    email: EmailStr
    phone_number: str
    password: str
    class_name:str

class UserLogin(BaseModel):
    login: str  # Can be either email or phone number
    password: str
