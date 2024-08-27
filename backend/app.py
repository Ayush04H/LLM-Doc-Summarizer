from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from summarizer.main import main as summarizer_main
from config.configuration import summary_length as default_summary_length
import uvicorn
import os

app = FastAPI()

# Ensure the temp directory exists within the container
TEMP_DIR = "./temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...), summary_length: int = Form(default_summary_length)):
    try:
        # Save the uploaded file in the temp directory within the container
        file_path = os.path.join(TEMP_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())  # Use await to read file asynchronously

        # Run the summarization process
        summary = summarizer_main(file_path, summary_length)

        # Remove the temporary file
        os.remove(file_path)

        return JSONResponse(content={"summary": summary}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    # Start the FastAPI server
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
