from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.schemas import knowledge as knowledge_schema
from app.workers import kb_ingestion_worker
import io

router = APIRouter()

@router.post("/ingest-url", response_model=knowledge_schema.IngestResponse)
def ingest_url(
    ingest_request: knowledge_schema.IngestURLRequest
):
    """
    Ingest knowledge from a URL.
    In a real system, this would be an async task.
    """
    try:
        # This is a blocking call for simplicity.
        # In production, you'd add this to a job queue (e.g., Celery, RQ).
        kb_ingestion_worker.ingest_from_url(
            url=ingest_request.url,
            tenant_id=ingest_request.tenant_id
        )
        return {"status": "success", "message": "URL ingestion started."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to start ingestion: {e}"}


@router.post("/ingest-file", response_model=knowledge_schema.IngestResponse)
async def ingest_file(
    tenant_id: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Ingest knowledge from a file (PDF).
    In a real system, this would be an async task.
    """
    if not file.filename.lower().endswith('.pdf'):
        return {"status": "error", "message": "Only PDF files are supported."}
        
    try:
        file_stream = io.BytesIO(await file.read())
        # This is a blocking call for simplicity.
        kb_ingestion_worker.ingest_from_pdf(
            file_stream=file_stream,
            filename=file.filename,
            tenant_id=tenant_id
        )
        return {"status": "success", "message": "File ingestion started."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to start ingestion: {e}"}
