# app/schemas.py 

from pydantic import BaseModel


"""
{
  "target_url": "https://realpython.com",
  "is_active": true,
  "clicks": 0,
  "url": "JNPGB",
  "admin_url": "MIZJZYVA"
}
"""


class URLBase(BaseModel):
    target_url: str 
    
class URL(URLBase):
    is_active: bool
    # count how many times a shortened URL has been visited. 
    clicks: int 
    
    class Config:
        # Object-Relational Mapping, and it provides the convenience of interacting with your database using an object-oriented approach. 
        orm_mode = True
        
class URLInfo(URL):
    url:str
    admin_url:str
    
    