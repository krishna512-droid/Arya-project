class PlannerAgent:
    name = "Planner Agent"

    def plan(self, goal: str) -> dict:
        # Lightweight autonomous planner. It intentionally avoids a paid LLM
        # dependency so the hackathon demo works immediately.
        keywords = [
            word.strip(".,!?").lower()
            for word in goal.split()
            if len(word.strip(".,!?")) > 3
        ]

        topic = " ".join(keywords[:6]) or "technology"

        return {
            "goal": goal,
            "topic": topic,
            "tasks": [
                "Find a reliable overview of the topic on Wikipedia.",
                "Inspect related public GitHub repositories.",
                "Extract useful evidence from both sources.",
                "Combine the evidence into a concise report."
            ]
        }
