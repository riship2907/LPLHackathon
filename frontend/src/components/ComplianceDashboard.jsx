import { useState, useEffect } from "react";
import { getTrades, reviewTrade } from "../services/api";
import TradeRow from "./TradeRow";
import { connectWebSocket } from "../services/websocket";

export default function ComplianceDashboard() {
    const [trades, setTrades] = useState([]);

    useEffect(() => {
        async function fetchTrades() {
            const data = await getTrades("compliance");
            setTrades(data);
        }
        fetchTrades();

        const ws = connectWebSocket((msg) => {
            // new trades can be pushed here
            setTrades(prev => [msg, ...prev]);
        });

        return () => ws.close();
    }, []);

    const handleReview = async (trade_id, status) => {
        await reviewTrade(trade_id, status);
        setTrades(trades.map(t => t.id === trade_id ? {...t, review_status: status} : t));
    };

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Compliance Dashboard</h2>
            <table className="w-full border">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Sender</th>
                        <th>Receiver</th>
                        <th>Amount</th>
                        <th>Flagged</th>
                        <th>Status</th>
                        <th>Review</th>
                    </tr>
                </thead>
                <tbody>
                    {trades.map(trade => <TradeRow key={trade.id} trade={trade} onReview={handleReview} />)}
                </tbody>
            </table>
        </div>
    );
}
