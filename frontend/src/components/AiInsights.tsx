interface Props {
  summary: string;
  suggestions: string[];
}

export default function AiInsights({ summary, suggestions }: Props) {
  const aiUnavailable = summary.includes("could not be generated");

  return (
    <div className="mt-6 rounded-lg border bg-transparent p-5">
      <h3 className="font-semibold text-gray-800 dark:text-gray-400 mb-2">
        AI Insights
      </h3>

      <p className={`text-sm ${aiUnavailable ? "text-gray-400" : "text-gray-700"}`}>
        {summary}
      </p>

      <ul className="mt-3 list-disc pl-5 text-sm text-gray-700 dark:text-gray-600">
        {suggestions.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>

      {aiUnavailable && (
        <div className="mt-3 text-xs text-yellow-600">
          AI service unavailable. Showing fallback recommendations.
        </div>
      )}
    </div>
  );
}
