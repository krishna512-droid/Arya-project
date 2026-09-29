import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

class WebAgent:
    name = "Web Agent"

    def run(self, plan: dict) -> list:
        topic = plan["topic"]
        results = []

        # Wikipedia REST API
        title = quote(topic.replace(" ", "_"))
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

        try:
            r = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "PS10-Hackathon-Demo/1.0"}
            )
            if r.ok:
                data = r.json()
                results.append({
                    "source": "Wikipedia",
                    "title": data.get("title", topic),
                    "url": data.get("content_urls", {})
                              .get("desktop", {})
                              .get("page", ""),
                    "summary": data.get("extract", "No summary available.")
                })
            else:
                results.append({
                    "source": "Wikipedia",
                    "error": f"HTTP {r.status_code}"
                })
        except Exception as exc:
            results.append({
                "source": "Wikipedia",
                "error": str(exc)
            })

        # A second trusted web source: Python.org search-style page
        # This is intentionally simple and read-only.
        if "python" in topic.lower():
            url = "https://www.python.org/"
            try:
                r = requests.get(
                    url,
                    timeout=10,
                    headers={"User-Agent": "PS10-Hackathon-Demo/1.0"}
                )
                soup = BeautifulSoup(r.text, "html.parser")
                text = soup.get_text(" ", strip=True)
                results.append({
                    "source": "Python.org",
                    "title": "Python.org",
                    "url": url,
                    "summary": text[:1000]
                })
            except Exception as exc:
                results.append({
                    "source": "Python.org",
                    "error": str(exc)
                })

        return results
