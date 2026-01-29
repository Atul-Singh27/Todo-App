from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
from todos import todos, next_id
app = Flask(__name__)


CORS(app)

@app.route('/')
def index():
    # Show all todos
    return jsonify(todos)


@app.route('/add', methods=["POST"])
def add():
    global next_id

    title = request.form.get("title")
    if title:
        todos.append({
            "id": next_id,
            "title": title,
            "complete": False
        })
        next_id += 1

    return redirect(url_for("index"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    # Toggle complete status
    for todo in todos:
        if todo["id"] == todo_id:
            todo["complete"] = not todo["complete"]
            break

    return redirect(url_for("index"))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)