"use client"
import { useState } from "react";
import UrlForm from "@/src/components/UrlForm";
import Footer from "../components/Footer";
import { AuditResponse } from "../types/audit";
import AuditResults from "../components/AuditResult";

export default function Home() {
    const [result, setResult] = useState<AuditResponse | null>(null);
  return (
    <main className="p-10 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">SEO Analyzer</h1>

      <p className="text-gray-500 mb-6">
        Professional SEO & Performance Audits
      </p>

       <UrlForm onResult={setResult} />

        {result && <AuditResults data={result} />}

      <Footer />
    </main>
  );
}
