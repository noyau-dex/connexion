# app.py
from flask import Flask, request, jsonify
import random
import smtplib
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1:3306",
    user="u303152537_NoyauConnexion",
    password="Thenoyau@123",
    database="u303152537_connexion"
)
cursor = db.cursor()

# Send OTP via email
def send_otp_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    message = f'Subject: Your OTP\n\nYour OTP is {otp}'
    server.sendmail('your-email@gmail.com', email, message)
    server.quit()

# Route to send OTP
@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data['email']
    
    # Generate a random 6-digit OTP
    otp = random.randint(100000, 999999)

    # Save OTP and email to the database
    cursor.execute("INSERT INTO otps (email, otp) VALUES (%s, %s)", (email, otp))
    db.commit()

    # Send OTP to the user's email
    send_otp_email(email, otp)

    return jsonify({"message": "OTP sent successfully!"})

# Route to verify OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data['email']
    otp = data['otp']

    # Verify OTP from the database
    cursor.execute("SELECT otp FROM otps WHERE email=%s", (email,))
    result = cursor.fetchone()

    if result and str(result[0]) == otp:
        return jsonify({"message": "OTP verified, login successful!"})
    else:
        return jsonify({"message": "Invalid OTP"}), 401

if __name__ == '__main__':
    app.run(debug=True)
