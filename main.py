from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from todos import todos, next_id

app = FastAPI()

# CORS (equivalent to Flask-CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    # Show all todos
    return todos


@app.post("/add")
def add(title: str = Form(...)):
    global next_id

    todos.append({
        "id": next_id,
        "title": title,
        "complete": False
    })
    next_id += 1

    return RedirectResponse(url="/", status_code=303)


@app.get("/update/{todo_id}")
def update(todo_id: int):
    # Toggle complete status
    for todo in todos:
        if todo["id"] == todo_id:
            todo["complete"] = not todo["complete"]
            break

    return RedirectResponse(url="/", status_code=303)


@app.get("/delete/{todo_id}")
def delete(todo_id: int):
    global todos
    todos[:] = [todo for todo in todos if todo["id"] != todo_id]

    return RedirectResponse(url="/", status_code=303)
