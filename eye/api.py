from flask import Flask

app = Flask(__name__)

notes = []

@app.route("/view_notes")
def send_messages():
    return {"messages": messages}

@app.route("/remove_note/<note>")
def remove(note):
    messages.append(message)
    return {"message": message}


app.run(host="0.0.0.0", port=5000, debug=True)
