// OTPForm.js
import React, { useState } from 'react';

function OTPForm({ verifyOTP }) {
    const [otp, setOtp] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        verifyOTP(otp);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Enter OTP:</label>
            <input
                type="text"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
            />
            <button type="submit">Verify OTP</button>
        </form>
    );
}

export default OTPForm;
