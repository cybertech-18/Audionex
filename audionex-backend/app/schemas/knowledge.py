from pydantic import BaseModel, HttpUrl

class IngestURLRequest(BaseModel):
    url: HttpUrl
    tenant_id: str

class IngestResponse(BaseModel):
    status: str
    message: str
