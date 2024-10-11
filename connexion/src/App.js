import React, { useState } from 'react';
import EmailForm from'./component/EmailForm'
import OTPForm from'./component/OTPForm'

function App() {
  const [step, setStep] = useState('email');
  const [email, setEmail] = useState('');

  const sendOTP = (email) => {
      fetch('http://localhost:5000/send-otp', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email }),
      })
          .then(response => response.json())
          .then(data => {
              setEmail(email);
              setStep('otp');
          })
          .catch(error => console.error('Error:', error));
  };

  const verifyOTP = (otp) => {
      fetch('http://localhost:5000/verify-otp', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, otp }),
      })
          .then(response => response.json())
          .then(data => {
              if (data.message === 'OTP verified, login successful!') {
                  alert('Login successful!');
                  setStep('profile');
              } else {
                  alert('Invalid OTP');
              }
          })
          .catch(error => console.error('Error:', error));
  };

  return (
      <div>
          {step === 'email' && <EmailForm sendOTP={sendOTP} />}
          {step === 'otp' && <OTPForm verifyOTP={verifyOTP} />}
          {step === 'profile' && <h1>Welcome to your profile!</h1>}
      </div>
  );
}

export default App;
