import datetime
from fastapi import FastAPI, Response, status
from pydantic import BaseModel


app = FastAPI()
@app.get("/")
def root():
    return {'start': '1970-01-01'}

@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

days = {1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday", 7:"sunday"}


@app.get("/day", status_code=200)
def get_day(name: str, number: int, response: Response):
        if days.get(number) == name:
                return days[number] 
        else:
            response.status_code = 400
            return {"Day or number": "not viable"}

class Event(BaseModel):
	date: str
	event: str

events = []

@app.put("/events", status_code = 200)
def put_event(event: Event, response: Response):
    out = {
        "id": len(events),
        "date": event.date,
        "name": event.event,
        "date_added": str(datetime.date.today())
    }
    events.append(out)

    return out



@app.get("/events/{date}", status_code=200)
def get_event(date: str, response: Response):
    event_date=[]
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
        for event in events:
            if event["date"] == date:
                event_date.append(event)

        return event_date



    except status.HTTP_400_BAD_REQUEST as exception:
        pass
