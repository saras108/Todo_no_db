from app import app

from flask import render_template, request, redirect

tasks =[]

@app.route('/')
def index():
    return render_template("todo_crud.html",len = len(tasks), task = tasks)


@app.route("/todotask", methods=["POST"])
def todotask():

     if request.method == "POST":     
        req = request.form
        task = req.get("task")

        tasks.append(task)

        return redirect("/")

@app.route("/removetodotask/<id>")
def removetodotask(id):
    id = int(id)

    tasks.pop(id)

    return redirect("/")


@app.route("/updatetodotask/<id>", methods=["POST"])
def updatetodotask(id):
    if request.method == "POST":
        id = int(id)
        req = request.form
        task = req.get("task")

        tasks[id] = task

        return redirect("/")