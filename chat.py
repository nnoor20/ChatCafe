from flask import Flask, request, render_template, session, redirect, url_for
from flask_socketio import SocketIO
from flask_socketio import join_room, leave_room, send
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key123'
socketio = SocketIO(app)

rooms = {}

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        join = request.form.get("join", False)
            
        if join != False:
            room = 1234
            rooms[room] = {"members": 0, "messages": []}
            session["room"] = room
            session["name"] = name
        return redirect(url_for("room"))

    return render_template("home.html")

@app.route("/chat")
def room():
    room = session.get("room")

    return render_template("chat.html", code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "(has entered the room)"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
    
    send({"name": name, "message": "(has left the room)"}, to=room)
    print(f"{name} has left the room {room}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
