import axios from "axios";
import { AuditResponse } from "../types/audit";

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  timeout: 30000,
});

export async function submitUrls(urls: string[]): Promise<AuditResponse> {
  try {
    const res = await api.post("/audit", { urls });
    return res.data;
  } catch (err: any) {
    return {
      status: "failed",
      reports: [],
      error:
        err.response?.data?.message ||
        err.message ||
        "Network error while running audit",
    };
  }
}

export const fetchReports = async () => {
  const res = await api.get("/reports");
  return res.data;
};
