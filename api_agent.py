import requests

class APIAgent:
    name = "API Agent"

    def run(self, plan: dict) -> list:
        topic = plan["topic"]
        query = topic[:80]

        url = "https://api.github.com/search/repositories"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 5
        }

        try:
            r = requests.get(
                url,
                params=params,
                timeout=10,
                headers={
                    "Accept": "application/vnd.github+json",
                    "User-Agent": "PS10-Hackathon-Demo/1.0"
                }
            )

            if not r.ok:
                return [{
                    "source": "GitHub API",
                    "error": f"HTTP {r.status_code}: {r.text[:300]}"
                }]

            data = r.json()
            repos = []

            for item in data.get("items", []):
                repos.append({
                    "name": item.get("full_name"),
                    "description": item.get("description"),
                    "stars": item.get("stargazers_count"),
                    "language": item.get("language"),
                    "url": item.get("html_url")
                })

            return [{
                "source": "GitHub API",
                "query": query,
                "repositories": repos
            }]

        except Exception as exc:
            return [{
                "source": "GitHub API",
                "error": str(exc)
            }]
