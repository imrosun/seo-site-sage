import { Metrics } from "@/src/types/audit";

export default function MetricsGrid({ metrics }: { metrics: Metrics }) {
  const items = [
    { label: "Title", value: metrics.title || "Missing" },
    { label: "H1 Tags", value: metrics.h1_count },
    { label: "H2 Tags", value: metrics.h2_count },
    { label: "Images Missing Alt", value: metrics.images_missing_alt },
    { label: "Load Time (ms)", value: metrics.load_time_ms },
  ];

  return (
    <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-4 mt-4">
      {items.map((item) => (
        <div
          key={item.label}
          className="rounded-lg border p-4 bg-transparent shadow-sm"
        >
          <div className="text-xs text-gray-500">{item.label}</div>
          <div className="text-lg font-semibold">{item.value}</div>
        </div>
      ))}
    </div>
  );
}
