from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from summarizer.main import main as summarizer_main
from config.configuration import summary_length as default_summary_length
import uvicorn

app = FastAPI()

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...), summary_length: int = Form(default_summary_length)):
    try:
        # Save the uploaded file
        file_path = r"D:\placements2025\document_summary_app\backend\temp{file.filename}"

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Run the summarization process
        summary = summarizer_main(file_path, summary_length)

        # Remove the temporary file
        import os
        os.remove(file_path)

        return JSONResponse(content={"summary": summary}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    # Start the FastAPI server
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000)
