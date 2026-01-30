import { useState } from "react";
import { login } from "../services/api";

export default function LoginForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await login(username, password);
            if(data.error) {
                setError(data.error);
            } else {
                onLogin(data);
            }
        } catch (err) {
            setError("Login failed");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 border rounded shadow-md w-96 mx-auto mt-20">
            <h2 className="text-2xl font-bold mb-4">Login</h2>
            {error && <div className="text-red-500 mb-2">{error}</div>}
            <input className="border p-2 mb-2 w-full" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
            <input className="border p-2 mb-2 w-full" type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
            <button type="submit" className="bg-blue-500 text-white p-2 w-full">Login</button>
        </form>
    );
}
