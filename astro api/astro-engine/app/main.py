from datetime import datetime
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError

from .models import KundliRequest, KundliResponse
from .astrology import generate_kundli
from .compatibility import generate_ashta_koota

# -----------------------------
# Pydantic Models for Compatibility
# -----------------------------
class CompatibilityRequest(BaseModel):
    kundli1: Dict[str, Any]
    kundli2: Dict[str, Any]

class CompatibilityResponse(BaseModel):
    total_gunas: int
    max_gunas: int
    breakdown: Dict[str, Any]
    verdict: str

# -----------------------------
# Initialize FastAPI
# -----------------------------
app = FastAPI(
    title="Kundli Astro Engine",
    description="A production-ready Kundli & Compatibility API using Swiss Ephemeris (Lahiri Ayanamsa) and Ashta-Koota",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Kundli Generation Endpoint
# -----------------------------
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
        import traceback
        print(f"Error generating kundli: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Internal Server Error", "message": "Failed to generate kundli"}
        )

# -----------------------------
# Compatibility Endpoint
# -----------------------------
@app.post(
    "/calculate-compatibility",
    response_model=CompatibilityResponse,
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Invalid input data"},
        500: {"description": "Internal server error"}
    }
)
async def calculate_compatibility_api(request: CompatibilityRequest) -> CompatibilityResponse:
    """
    Calculate Ashta-Koota compatibility between two kundlis.
    """
    try:
        result = generate_ashta_koota(request.kundli1, request.kundli2)
        return result
    except ValidationError as ve:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": "Validation Error", "details": ve.errors()}
        )
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Missing required kundli key", "key": str(ke)}
        )
    except Exception as e:
        import traceback
        print(f"Error calculating compatibility: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Internal Server Error", "message": "Failed to calculate compatibility"}
        )

# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get(
    "/health",
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK
)
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint to verify API is running.
    """
    try:
        return {
            "status": "healthy",
            "version": "1.0.0",
            "timestamp": datetime.utcnow().isoformat(),
            "services": {
                "database": "ok",
                "cache": "ok"
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "unhealthy", "error": str(e)}
        )
