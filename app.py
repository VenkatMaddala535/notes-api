from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
notes = []
next_id = 1


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Notes API",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200


@app.route("/notes", methods=["POST"])
def create_note():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    title = data.get("title")
    description = data.get("description")

    if not title or not description:
        return jsonify({
            "error": "title and description are required"
        }), 400

    note = {
        "id": next_id,
        "title": title,
        "description": description
    }

    notes.append(note)
    next_id += 1

    return jsonify(note), 201


@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    for note in notes:
        if note["id"] == id:
            return jsonify(note)

    return jsonify({
        "error": "Note not found"
    }), 404


@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):

    data = request.get_json()

    for note in notes:
        if note["id"] == id:
            note["title"] = data.get("title", note["title"])
            note["description"] = data.get("description", note["description"])

            return jsonify(note)

    return jsonify({
        "error": "Note not found"
    }), 404


@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):

    for note in notes:
        if note["id"] == id:
            notes.remove(note)

            return jsonify({
                "message": "Deleted successfully"
            })

    return jsonify({
        "error": "Note not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
