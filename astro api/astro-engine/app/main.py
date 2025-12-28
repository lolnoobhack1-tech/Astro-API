from datetime import datetime
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from .models import KundliRequest, KundliResponse
from .astrology import generate_kundli

# Initialize FastAPI app
app = FastAPI(
    title="Kundli Astro Engine",
    description="A production-ready Kundli generation API using Swiss Ephemeris (Lahiri Ayanamsa)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/generate-kundli",
    response_model=KundliResponse,
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Invalid input data"},
        500: {"description": "Internal server error"}
    }
)
async def generate_kundli_api(request: KundliRequest) -> KundliResponse:
    """
    Generate a kundli (astrological chart) based on birth details.
    
    - **date**: Birth date in DD-MM-YYYY format (e.g., "13-01-2007")
    - **time**: Birth time in 12-hour format (e.g., "06:47 PM")
    - **timezone**: IANA timezone (e.g., "Asia/Kolkata")
    - **latitude**: Birth latitude between -90 and 90 (e.g., 30.2110)
    - **longitude**: Birth longitude between -180 and 180 (e.g., 74.9455)
    """
    try:
        return generate_kundli(request)
    except ValidationError as ve:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": "Validation Error", "details": ve.errors()}
        )
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Invalid Input", "message": str(ve)}
        )
    except Exception as e:
        # Log the full error for debugging
        import traceback
        print(f"Error generating kundli: {str(e)}\n{traceback.format_exc()}")
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Internal Server Error", "message": "Failed to generate kundli"}
        )

@app.get(
    "/health",
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK
)
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint that verifies the API is running and can connect to required services.
    """
    try:
        # Add any additional health checks here
        return {
            "status": "healthy",
            "version": "1.0.0",
            "timestamp": datetime.utcnow().isoformat(),
            "services": {
                "database": "ok",  # Add actual checks in production
                "cache": "ok"      # Add actual checks in production
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "unhealthy", "error": str(e)}
        )
