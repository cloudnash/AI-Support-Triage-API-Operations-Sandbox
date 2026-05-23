import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

# Set up logging (Addresses the "logging & monitoring" requirement)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ai-triage-agent")

app = FastAPI(title="AI Support Triage API", version="1.0.0")

class Ticket(BaseModel):
    user_id: str
    issue_description: str

class TriageResponse(BaseModel):
    status: str
    category: str
    suggested_action: str
    processing_time_ms: float

def mock_ai_agent_analyze(text: str) -> dict:
    """Simulates an external LLM/AI Agent call analyzing a support ticket."""
    text_lower = text.lower()
    if "api" in text_lower or "endpoint" in text_lower:
        return {"category": "API Integration", "action": "Check API Keys and rate limits in Dashboard."}
    elif "deploy" in text_lower or "crash" in text_lower:
        return {"category": "DevOps / Infrastructure", "action": "Review container logs and CI/CD pipeline status."}
    else:
        return {"category": "General Usage", "action": "Route to L1 Customer Support."}

@app.post("/api/v1/triage", response_model=TriageResponse)
async def triage_ticket(ticket: Ticket):
    logger.info(f"Received ticket from user: {ticket.user_id}")
    start_time = time.time()
    
    try:
        # Simulate AI processing delay
        logger.info("Sending data to AI Agent for analysis...")
        analysis = mock_ai_agent_analyze(ticket.issue_description)
        
        process_time = round((time.time() - start_time) * 1000, 2)
        logger.info(f"AI Agent successfully categorized ticket as '{analysis['category']}' in {process_time}ms")
        
        return {
            "status": "success",
            "category": analysis["category"],
            "suggested_action": analysis["action"],
            "processing_time_ms": process_time
        }
        
    except Exception as e:
        logger.error(f"Failed to process ticket: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal AI Agent Error")

@app.get("/health")
async def health_check():
    """Endpoint for infrastructure monitoring tools."""
    return {"status": "healthy", "service": "ai-triage-api"}
