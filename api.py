from fastapi import FastAPI
  
app = FastAPI()
   
@app.get("/") 
async def health():     
  return { "status": 204, "message": "Server is running!"}