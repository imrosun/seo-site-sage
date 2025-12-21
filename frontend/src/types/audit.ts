export interface Metrics {
  title: string | null;
  h1_count: number;
  h2_count: number;
  images_missing_alt: number;
  load_time_ms: number;
}

export interface Report {
  url: string;
  seo_score: number;
  metrics: Metrics;
  ai_summary: string;
  ai_suggestions: string[];
}

export interface AuditResponse {
  status: "completed" | "failed";
  reports: Report[];
  error?: string;
}
