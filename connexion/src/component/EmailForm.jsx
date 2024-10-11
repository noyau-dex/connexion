// EmailForm.js
import React, { useState } from 'react';

function EmailForm({ sendOTP }) {
    const [email, setEmail] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        sendOTP(email);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Email:</label>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
            <button type="submit">Send OTP</button>
        </form>
    );
}

export default EmailForm;
