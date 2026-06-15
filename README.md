# 🚀 ROCm Bridge — AI-Powered CUDA to ROCm Code Converter

## What is ROCm Bridge?

ROCm Bridge is a web-based tool that automatically converts CUDA code (written for NVIDIA GPUs) into ROCm-compatible code (for AMD GPUs) using artificial intelligence.

**Problem:** Developers who want to switch from NVIDIA to AMD GPUs struggle because their existing CUDA code doesn't work on AMD hardware. Manual conversion is time-consuming and difficult.

**Solution:** ROCm Bridge automates this entire process using an LLM running on AMD's Instinct MI300X GPU.

---

## How It Works

1. User opens the web interface (`index.html`)
2. User pastes their CUDA code
3. The tool sends it to an LLM running on AMD Developer Cloud
4. The LLM converts it to ROCm-compatible code
5. User receives clean, ready-to-run ROCm code instantly

---

## Tech Stack

- **GPU:** AMD Instinct MI300X (AMD Developer Cloud)
- **Inference Server:** vLLM
- **LLM:** Llama or Qwen (open-source)
- **Backend:** Python (FastAPI)
- **Frontend:** HTML5 + CSS + JavaScript
- **Software:** ROCm stack

---

## Project Files

- **`backend.py`** — FastAPI server that handles code conversion
- **`index.html`** — Web interface where users paste CUDA code
- **`requirements.txt`** — Python dependencies

---

## How to Run Locally (Development)

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/rocm-bridge.git
   cd rocm-bridge
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the backend:**
   ```bash
   python backend.py
   ```
   You should see:
   ```
   Uvicorn running on http://0.0.0.0:8000
   ```

4. **Open the frontend:**
   - Open `index.html` in your web browser
   - Or go to `http://localhost:8000` if serving from backend

5. **Test it:**
   - Paste CUDA code in the left panel
   - Click "Convert to ROCm"
   - See the converted code appear on the right

---

## Current Status

- ✅ Project setup complete
- ✅ Frontend UI built
- ✅ Backend structure ready
- ⏳ **Next:** Deploy to AMD Developer Cloud with real LLM
- ⏳ **Next:** Integrate vLLM + Llama/Qwen on MI300X
- ⏳ **Next:** Submit to AMD Lemonade Developer Challenge

---

## Future Enhancements

- [ ] Real LLM integration on AMD MI300X
- [ ] Support for more CUDA features
- [ ] Code explanation panel
- [ ] Performance benchmarking
- [ ] Dark mode
- [ ] Multi-language support

---

## Roadmap

### Phase 1: Local Development ✅
- Build frontend UI
- Build FastAPI backend
- Mock LLM responses

### Phase 2: AMD GPU Deployment 🚧
- Get AMD Developer Cloud credits approved
- Set up vLLM on MI300X
- Deploy real LLM model
- Connect frontend to real backend

### Phase 3: Submission & Launch 📅
- Final testing and polishing
- Submit to AMD Lemonade Developer Challenge
- Deploy publicly

---

## About This Project

Built as part of the **AMD Lemonade Developer Challenge** to demonstrate the power of AMD's Instinct MI300X GPU for AI workloads.

**Goal:** Help developers transition from CUDA to ROCm with zero friction.

---

## License

MIT License — See LICENSE file for details

---

## Contact & Questions

For questions or feedback, please open an issue on GitHub.

---

**Happy Converting! 🚀**
