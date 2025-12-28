from pydantic import BaseModel, Field

class KundliRequest(BaseModel):
    date: str = Field(..., example="13-01-2007")
    time: str = Field(..., example="06:47 PM")
    timezone: str = Field(..., example="Asia/Kolkata")
    latitude: float = Field(..., example=30.2110)
    longitude: float = Field(..., example=74.9455)

class KundliResponse(BaseModel):
    sun_sign: str
    moon_sign: str
    ascendant: str
    nakshatra: str
    nakshatra_pada: int
    ayanamsa: str
    planetary_longitudes: dict
    confidence: int
