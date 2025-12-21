import { Report } from "@/src/types/audit";
import SeoScore from "./SeoScore";
import MetricsGrid from "./MetricGrid";
import AiInsights from "./AiInsights";

export default function ReportCard({ report }: { report: Report }) {
  return (
    <div className="rounded-xl border bg-transparent p-6 shadow-md">
      <div className="flex flex-col md:flex-row justify-between text-left">
        <a
          href={report.url}
          target="_blank"
          className="font-medium text-blue-600 hover:underline text-left"
        >
         {report.url}
        </a>
        <SeoScore score={report.seo_score} />
      </div>

      <MetricsGrid metrics={report.metrics} />

      <AiInsights
        summary={report.ai_summary}
        suggestions={report.ai_suggestions}
      />
    </div>
  );
}
