import { AuditResponse } from "@/src//types/audit";
import ReportCard from "./ReportCard";

export default function AuditResults({ data }: { data: AuditResponse }) {
  if (data.status !== "completed") {
    return (
      <div className="text-red-600">
        {data.error || "Audit failed"}
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {data.reports.map((report) => (
        <ReportCard key={report.url} report={report} />
      ))}
    </div>
  );
}
