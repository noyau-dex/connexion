from flask import Flask, request, jsonify
import mysql.connector
import bcrypt

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1:3306",
    user="u303152537_NoyauConnexion",
    password="Thenoyau@123",
    database="u303152537_connexion"
)
cursor = db.cursor()

# Route to handle user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password'].encode('utf-8')

    # Query the database to find the user
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        stored_password = user[2].encode('utf-8')  # Assumes the password is the 3rd field in users table
        if bcrypt.checkpw(password, stored_password):
            return jsonify({"message": "Login successful", "profile": {"name": user[1], "email": user[0]}}), 200
        else:
            return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "User not found"}), 404

# Route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
    db.commit()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
