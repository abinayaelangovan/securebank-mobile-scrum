"""
SecureBank Mobile - Sprint Reporting Tool
Generates Burndown and Velocity charts from sprint data.
Built because the team's Jira tier did not include native burndown/velocity reports.

To add a new sprint: append a new entry to the SPRINTS list below with the
sprint's dates, committed points, and day-by-day remaining work, then re-run
this script. All charts regenerate automatically.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# ----------------------------
# SPRINT DATA (from Jira)
# ----------------------------
SPRINTS = [
    {
        "name": "Sprint 1",
        "start": datetime(2026, 7, 21),
        "end": datetime(2026, 8, 4),
        "committed": 26,
        "completed_stories": {
            "SCRUM-3 (Fingerprint login)": 5,
            "SCRUM-4 (Face ID login)": 3,
            "SCRUM-8 (Auto-logout)": 2,
            "SCRUM-9 (Audit logging)": 3,
        },
        "carried_over_stories": {
            "SCRUM-5 (MFA setup)": 5,
            "SCRUM-7 (Password reset)": 5,
            "SCRUM-30 (Fraud alert - unrecognized country)": 3,
        },
        # Simulated day-by-day actual remaining work (Jira tier had no native burndown).
        # Bump at day 6 reflects a mid-sprint scope change (+3 pts, SCRUM-30 added,
        # SCRUM-6 removed to hold total steady).
        "actual_remaining": [26, 26, 24, 24, 21, 21, 21, 24, 19, 16, 13],
        "scope_change": {
            "day_index": 6,
            "label": "Scope change:\n+3 pts (SCRUM-30 added,\nSCRUM-6 removed)",
        },
    },
    {
        "name": "Sprint 2",
        "start": datetime(2026, 8, 5),
        "end": datetime(2026, 8, 18),
        "committed": 13,
        "completed_stories": {
            "SCRUM-5 (MFA setup)": 5,
            "SCRUM-7 (Password reset)": 5,
            "SCRUM-30 (Fraud alert - unrecognized country)": 3,
        },
        "carried_over_stories": {},
        # Clean, steady completion - no scope change this sprint. Capacity was
        # recalibrated to Sprint 1's actual velocity (13 pts), and the team hit it.
        "actual_remaining": [13, 13, 11, 10, 8, 8, 6, 5, 3, 2, 0],
        "scope_change": None,
    },
    # To add Sprint 3, copy the block above, fill in real data, and re-run.
]


def total_points(stories: dict) -> int:
    return sum(stories.values())


def build_burndown_chart(sprint: dict):
    start, end = sprint["start"], sprint["end"]
    committed = sprint["committed"]
    actual = sprint["actual_remaining"]
    days = [start + timedelta(days=i) for i in range(len(actual))]

    ideal = [
        committed - (committed / (len(days) - 1)) * i
        for i in range(len(days))
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(days, ideal, linestyle="--", color="#8899A6", linewidth=2, label="Ideal Burndown")
    ax.plot(days, actual, marker="o", color="#2684FF", linewidth=2.5, label="Actual Remaining Work")

    if sprint["scope_change"]:
        idx = sprint["scope_change"]["day_index"]
        ax.annotate(
            sprint["scope_change"]["label"],
            xy=(days[idx], actual[idx]),
            xytext=(days[idx] + timedelta(days=0.3), actual[idx] + 4),
            arrowprops=dict(arrowstyle="->", color="#FF5630"),
            fontsize=9, color="#FF5630",
        )

    ax.set_title(f"{sprint['name']} Burndown Chart — SecureBank Mobile", fontsize=14, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Remaining Story Points")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.set_ylim(0, max(committed, max(actual)) + 4)
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()

    plt.tight_layout()
    filename = f"/home/claude/{sprint['name'].lower().replace(' ', '')}_burndown.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    return filename


def build_velocity_chart(sprints: list):
    names = [s["name"] for s in sprints]
    committed_vals = [s["committed"] for s in sprints]
    completed_vals = [total_points(s["completed_stories"]) for s in sprints]

    fig, ax = plt.subplots(figsize=(9, 6))
    x = range(len(names))
    bar_width = 0.35

    ax.bar([i - bar_width / 2 for i in x], committed_vals, width=bar_width,
           label="Committed Points", color="#8899A6")
    ax.bar([i + bar_width / 2 for i in x], completed_vals, width=bar_width,
           label="Completed Points", color="#36B37E")

    ax.set_xticks(list(x))
    ax.set_xticklabels(names)
    ax.set_ylabel("Story Points")
    ax.set_title("Sprint Velocity — SecureBank Mobile", fontsize=14, fontweight="bold")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)

    for i, v in enumerate(committed_vals):
        ax.text(i - bar_width / 2, v + 0.5, str(v), ha="center", fontsize=10)
    for i, v in enumerate(completed_vals):
        ax.text(i + bar_width / 2, v + 0.5, str(v), ha="center", fontsize=10)

    plt.tight_layout()
    filename = "/home/claude/sprint_velocity.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    return filename


def print_summary(sprint: dict):
    committed = sprint["committed"]
    completed = total_points(sprint["completed_stories"])
    carried = total_points(sprint["carried_over_stories"])
    print(f"\n{sprint['name']} Summary")
    print(f"Committed: {committed} points")
    print(f"Completed: {completed} points ({len(sprint['completed_stories'])} stories)")
    if carried:
        print(f"Carried over: {carried} points ({len(sprint['carried_over_stories'])} stories)")
    print(f"Completion rate: {completed / committed * 100:.0f}%")


if __name__ == "__main__":
    burndown_files = [build_burndown_chart(s) for s in SPRINTS]
    velocity_file = build_velocity_chart(SPRINTS)

    for s in SPRINTS:
        print_summary(s)

    print("\nCharts saved:")
    for f in burndown_files:
        print(f"- {f}")
    print(f"- {velocity_file}")
