export default function TradeRow({ trade, onReview }) {
    return (
        <tr className="border-b">
            <td className="px-2">{trade.transaction_id}</td>
            <td className="px-2">{trade.sender_account}</td>
            <td className="px-2">{trade.receiver_account}</td>
            <td className="px-2">{trade.amount_ngn}</td>
            <td className="px-2">{trade.is_fraud ? "Yes" : "No"}</td>
            <td className="px-2">{trade.review_status}</td>
            {onReview && (
                <td className="px-2">
                    <button className="bg-green-500 text-white px-2 mr-1" onClick={() => onReview(trade.id, "confirmed_fraud")}>Fraud</button>
                    <button className="bg-gray-500 text-white px-2" onClick={() => onReview(trade.id, "false_positive")}>False</button>
                </td>
            )}
        </tr>
    );
}
