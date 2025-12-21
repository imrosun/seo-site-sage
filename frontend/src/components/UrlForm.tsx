"use client";

import { useState } from "react";
import { submitUrls } from "@/src/lib/api";
import { AuditResponse } from "@/src/types/audit";

interface Props {
  onResult: (data: AuditResponse) => void;
}

export default function UrlForm({ onResult }: Props) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    setError(null);
    setLoading(true);

    const urls = input
      .split("\n")
      .map((u) => u.trim())
      .filter(Boolean);

    if (!urls.length) {
      setError("Please enter at least one valid URL");
      setLoading(false);
      return;
    }

    const result = await submitUrls(urls);

    setLoading(false);

    if (result.status === "failed") {
      setError(result.error || "Audit failed");
      return;
    }

    onResult(result);
  };

  return (
    <div className="rounded-lg border p-6 bg-transparent shadow">
      <textarea
        rows={4}
        className="w-full border rounded p-3 text-sm"
        placeholder="Enter one URL per line"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      {error && (
        <div className="mt-2 text-sm text-red-600">{error}</div>
      )}

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="mt-4 px-5 py-2 rounded bg-black text-white disabled:opacity-50 cursor-pointer hover:bg-yellow-600 dark:bg-gray-400 dark:text-black"
      >
        {loading ? "Analyzing…" : "Run Audit"}
      </button>
    </div>
  );
}
