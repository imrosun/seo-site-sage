interface Props {
  score: number;
}

export default function SeoScore({ score }: Props) {
  const color =
    score >= 80
      ? "text-green-600"
      : score >= 50
      ? "text-yellow-500"
      : "text-red-500";

  return (
    <div className="flex items-center gap-3">
      <div
        className={`text-4xl font-bold ${color}`}
      >
        {score}
      </div>
      <div className="text-sm text-gray-500">
        SEO Score
      </div>
    </div>
  );
}
