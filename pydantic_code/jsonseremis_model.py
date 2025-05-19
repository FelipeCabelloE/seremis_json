from typing import List, Optional
from pydantic import BaseModel


class Seremi(BaseModel):
    Region: str
    Address: str
    Phones: List[str]
    Email: str
    Hours: str
    # Additional_Hours is optional, as it only appears in the last entry
    Additional_Hours: Optional[str] = None
