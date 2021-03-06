from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String

from app import db


class User(db.Model):
    __tablename__ = 'tbl_users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    role = Column(Integer(), default=0)
    full_name = Column(String(64), nullable=True)
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_admin(self):
        return self.role == 1