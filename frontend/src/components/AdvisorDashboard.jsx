import { useState, useEffect } from "react";
import { getTrades } from "../services/api";
import TradeRow from "./TradeRow";
import { connectWebSocket } from "../services/websocket";

export default function AdvisorDashboard({ advisorId }) {
    const [trades, setTrades] = useState([]);

    useEffect(() => {
        async function fetchTrades() {
            const allTrades = await getTrades("advisor");
            const myTrades = allTrades.filter(t => t.advisor_id === advisorId);
            setTrades(myTrades);
        }
        fetchTrades();

        const ws = connectWebSocket((msg) => {
            if(msg.advisor_id === advisorId) {
                setTrades(prev => [msg, ...prev]);
            }
        });

        return () => ws.close();
    }, [advisorId]);

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Advisor Dashboard</h2>
            <table className="w-full border">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Sender</th>
                        <th>Receiver</th>
                        <th>Amount</th>
                        <th>Flagged</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {trades.map(trade => <TradeRow key={trade.id} trade={trade} />)}
                </tbody>
            </table>
        </div>
    );
}
