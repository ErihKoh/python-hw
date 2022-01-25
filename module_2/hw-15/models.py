from pydantic import BaseModel


class MeteoWeather(BaseModel):
    head: str
    current_temp: str
    desc: str


class MeteoprogWeather(BaseModel):
    head: str
    current_temp: str
    desc: str
