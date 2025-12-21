import { APP_VERSION } from "@/src/lib/version";

export default function Footer() {
  return (
    <footer className="mt-10 border-t pt-4 text-center text-xs text-gray-400">
      SEO Site Sage • Version {APP_VERSION} • Roshan Sharma
    </footer>
  );
}
