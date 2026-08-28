from datetime import datetime
from pydantic import BaseModel

class MissionCreate(BaseModel):
    id: str
    ticket_id: str
    team_id: str
    vehicle_id: str
    priority: str
    status: str
    latitude: float
    longitude: float
    personnel_required: int
    medical_personnel: int
    vehicle_required: int

class MissionResponse(BaseModel):
    id: str
    ticket_id: str
    team_id: str
    vehicle_id: str
    prioprity: str
    status: str
    latitude: str
    longitude: str
    personnel_required: int
    medical_personnel: int
    vehicle_required: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

class MissionUpdate(BaseModel):
    priority: str | None = None
    status: str | None = None
    team_id: str | None = None
    vehicle_id: str | None = None
    personnel_required: int | None = None
    medical_personnel: int | None = None
    vehicle_required: int | None = None
    