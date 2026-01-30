import { useState } from "react";
import Login from "./pages/Login";
import CompliancePage from "./pages/CompliancePage";
import AdvisorPage from "./pages/AdvisorPage";

export default function App() {
    const [user, setUser] = useState(null);

    const handleLogin = (data) => {
        setUser(data);
    };

    if(!user) return <Login onLogin={handleLogin} />;

    if(user.role === "compliance") return <CompliancePage />;
    if(user.role === "advisor") return <AdvisorPage advisorId={1} />; // demo: advisor1

    return <div>Unknown role</div>;
}
