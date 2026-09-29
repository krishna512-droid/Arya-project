class AnalystAgent:
    name = "Analyst Agent"

    def analyze(self, goal, plan, web_results, api_results):
        lines = [
            f"## Goal\n{goal}",
            "",
            "## Autonomous Findings",
        ]

        for result in web_results:
            if "error" in result:
                lines.append(f"- **{result.get('source')} error:** {result['error']}")
            else:
                lines.append(
                    f"- **{result.get('source')} — {result.get('title')}**: "
                    f"{result.get('summary', '')[:700]}"
                )

        for result in api_results:
            if "error" in result:
                lines.append(f"- **GitHub API error:** {result['error']}")
                continue

            repos = result.get("repositories", [])
            if repos:
                lines.append("")
                lines.append("### GitHub repositories discovered")
                for repo in repos:
                    lines.append(
                        f"- **{repo.get('name')}** — "
                        f"{repo.get('stars', 0):,} stars — "
                        f"{repo.get('language') or 'N/A'} — "
                        f"{repo.get('description') or 'No description'}"
                    )

        lines += [
            "",
            "## Agent Trace",
            "1. Planner converted the goal into executable research tasks.",
            "2. Web Agent retrieved information from trusted web endpoints.",
            "3. API Agent queried GitHub's public REST API.",
            "4. Analyst Agent merged the collected evidence into this report.",
            "",
            "> This demo is intentionally read-only and uses trusted/public endpoints."
        ]

        return "\n".join(lines)
