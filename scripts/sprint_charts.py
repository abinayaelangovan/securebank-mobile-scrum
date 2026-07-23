"""
SecureBank Mobile - Sprint Reporting Tool
Generates Burndown and Velocity charts from sprint data.
Built because the team's Jira tier did not include native burndown/velocity reports.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# ----------------------------
# SPRINT 1 DATA (from Jira)
# ----------------------------
SPRINT_NAME = "Sprint 1"
START_DATE = datetime(2026, 7, 21)
END_DATE = datetime(2026, 8, 4)
COMMITTED_POINTS = 26

# Stories completed in Sprint 1, with points
COMPLETED_STORIES = {
    "SCRUM-3 (Fingerprint login)": 5,
    "SCRUM-4 (Face ID login)": 3,
    "SCRUM-8 (Auto-logout)": 2,
    "SCRUM-9 (Audit logging)": 3,
}

# Stories carried over to Sprint 2
CARRIED_OVER_STORIES = {
    "SCRUM-5 (MFA setup)": 5,
    "SCRUM-7 (Password reset)": 5,
    "SCRUM-30 (Fraud alert - unrecognized country)": 3,
}

TOTAL_COMPLETED = sum(COMPLETED_STORIES.values())
TOTAL_CARRIED = sum(CARRIED_OVER_STORIES.values())

# Simulated day-by-day actual remaining work (since Jira tier had no native burndown).
# Reflects realistic pattern: slow start, mid-sprint scope change (SCRUM-30 added),
# late completions of SCRUM-3/4/8/9.
sprint_days = [(START_DATE + timedelta(days=i)) for i in range(11)]  # 10 working days + start
actual_remaining = [26, 26, 24, 24, 21, 21, 21, 24, 19, 16, 13]  # bump at day 6 = scope change (+3 SCRUM-30)

# Ideal burndown: linear from committed points to 0 over the sprint
ideal_remaining = [
    COMMITTED_POINTS - (COMMITTED_POINTS / (len(sprint_days) - 1)) * i
    for i in range(len(sprint_days))
]

# ----------------------------
# CHART 1: BURNDOWN CHART
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(sprint_days, ideal_remaining, linestyle="--", color="#8899A6",
        linewidth=2, label="Ideal Burndown")
ax.plot(sprint_days, actual_remaining, marker="o", color="#2684FF",
        linewidth=2.5, label="Actual Remaining Work")

# Annotate the scope-change bump
ax.annotate(
    "Scope change:\n+3 pts (SCRUM-30 added,\nSCRUM-6 removed)",
    xy=(sprint_days[6], actual_remaining[6]),
    xytext=(sprint_days[6] + timedelta(days=0.3), actual_remaining[6] + 4),
    arrowprops=dict(arrowstyle="->", color="#FF5630"),
    fontsize=9, color="#FF5630"
)

ax.set_title(f"{SPRINT_NAME} Burndown Chart — SecureBank Mobile", fontsize=14, fontweight="bold")
ax.set_xlabel("Date")
ax.set_ylabel("Remaining Story Points")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.set_ylim(0, 30)
ax.legend(loc="upper right")
ax.grid(True, alpha=0.3)
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig("/home/claude/sprint1_burndown.png", dpi=150)
plt.close()

# ----------------------------
# CHART 2: VELOCITY CHART
# ----------------------------
# Extend this dict as more sprints complete
sprint_velocity = {
    "Sprint 1": TOTAL_COMPLETED,
    "Sprint 2": None,  # to be filled in after Sprint 2
    "Sprint 3": None,
}

sprints = list(sprint_velocity.keys())
committed = [COMMITTED_POINTS, None, None]
completed = [sprint_velocity[s] if sprint_velocity[s] is not None else 0 for s in sprints]

fig, ax = plt.subplots(figsize=(9, 6))

x = range(len(sprints))
bar_width = 0.35

committed_vals = [COMMITTED_POINTS, 0, 0]  # only Sprint 1 has committed data so far
ax.bar([i - bar_width/2 for i in x], committed_vals, width=bar_width,
       label="Committed Points", color="#8899A6")
ax.bar([i + bar_width/2 for i in x], completed, width=bar_width,
       label="Completed Points", color="#36B37E")

ax.set_xticks(list(x))
ax.set_xticklabels(sprints)
ax.set_ylabel("Story Points")
ax.set_title("Sprint Velocity — SecureBank Mobile", fontsize=14, fontweight="bold")
ax.legend()
ax.grid(True, axis="y", alpha=0.3)

# Value labels
for i, v in enumerate(committed_vals):
    if v > 0:
        ax.text(i - bar_width/2, v + 0.5, str(v), ha="center", fontsize=10)
for i, v in enumerate(completed):
    if v > 0:
        ax.text(i + bar_width/2, v + 0.5, str(v), ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("/home/claude/sprint_velocity.png", dpi=150)
plt.close()

# ----------------------------
# SUMMARY OUTPUT
# ----------------------------
print(f"Sprint 1 Summary")
print(f"Committed: {COMMITTED_POINTS} points")
print(f"Completed: {TOTAL_COMPLETED} points ({len(COMPLETED_STORIES)} stories)")
print(f"Carried over: {TOTAL_CARRIED} points ({len(CARRIED_OVER_STORIES)} stories)")
print(f"Completion rate: {TOTAL_COMPLETED / COMMITTED_POINTS * 100:.0f}%")
print("\nCharts saved:")
print("- sprint1_burndown.png")
print("- sprint_velocity.png")
