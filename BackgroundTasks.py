from fastapi import FastAPI,BackgroundTasks


app = FastAPI()

def write_notification(email:str,message:""):
    with open("log.txt",mode="w") as email_file:
        content = f"notification for {email}:{message}"
        email_file.write(content)
def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q

@app.post("/send-notification/{email}")
async def send_notification(email:str,background_tasks:BackgroundTasks):
    background_tasks.add_task(write_notification,email,message="hello,")
    return {"message": "Notification sent in the background"}
