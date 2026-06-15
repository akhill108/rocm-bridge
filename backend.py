from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS (allow frontend to talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock LLM response (we'll replace this with real vLLM later)
def convert_cuda_to_rocm(cuda_code):
    """
    This is a placeholder function.
    When AMD credits arrive, this will call the real LLM on MI300X.
    For now, it returns a mock ROCm conversion.
    """
    
    # Simple mock conversion (replace # with //)
    rocm_code = cuda_code.replace("//CUDA", "//ROCm")
    rocm_code = rocm_code.replace("cudaMalloc", "hipMalloc")
    rocm_code = rocm_code.replace("cudaMemcpy", "hipMemcpy")
    rocm_code = rocm_code.replace("cudaFree", "hipFree")
    rocm_code = rocm_code.replace("__global__", "__global__")
    
    return rocm_code

@app.get("/")
def read_root():
    return {"message": "ROCm Bridge Backend is running!"}

@app.post("/convert")
async def convert_code(cuda_code: str):
    """
    API endpoint to convert CUDA code to ROCm
    """
    try:
        rocm_code = convert_cuda_to_rocm(cuda_code)
        return {
            "success": True,
            "rocm_code": rocm_code,
            "message": "Conversion complete!"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Conversion failed"
        }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    # This runs the backend on http://localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
