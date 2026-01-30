import axios from "axios";

const API_URL = "http://localhost:8000";

export async function login(username, password) {
    const res = await axios.post(`${API_URL}/login`, { username, password });
    return res.data;
}

export async function getTrades(role) {
    const res = await axios.get(`${API_URL}/trades`, { params: { role } });
    return res.data;
}

export async function reviewTrade(trade_id, status) {
    const res = await axios.post(`${API_URL}/review_trade`, { trade_id, status });
    return res.data;
}
