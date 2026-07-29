# SecureBank Mobile — Scrum Master Simulation Project

A self-directed Agile simulation project built to demonstrate hands-on Scrum
Master skills using Jira, Confluence, and Python. The project simulates a
mobile banking application release across two completed sprints, covering
the full Scrum lifecycle: backlog creation, sprint planning, active sprint
facilitation, mid-sprint scope management, capacity recalibration using
real velocity data, sprint review, retrospective, and custom reporting.

## Why this project exists

I have a background in mainframe QA testing and recently completed a
Certified Scrum Master (CSM) course. This project was built to turn that
certification into demonstrable, hands-on evidence — a real backlog, real
sprints, a real scope-change decision, a real capacity recalibration, and
real reporting — rather than just a line on a resume.

## Project Structure

```
securebank-mobile-scrum/
├── README.md                              This file
├── docs/
│   └── SecureBank_Mobile_Portfolio_Case_Study.pdf   Full case study writeup
├── reports/
│   ├── sprint1_burndown.png               Sprint 1 burndown chart
│   ├── sprint2_burndown.png               Sprint 2 burndown chart
│   └── sprint_velocity.png                Sprint 1 vs. Sprint 2 velocity chart
└── scripts/
    ├── sprint_charts.py                   Python script that generates the charts
    └── requirements.txt                   Python dependencies
```

## Sprint Summary

| Metric | Sprint 1 | Sprint 2 |
|---|---|---|
| Sprint Length | 2 weeks | 2 weeks |
| Committed | 26 points (7 stories) | 13 points (3 stories) |
| Completed | 13 points (4 stories) | 13 points (3 stories) |
| Completion Rate | 50% | 100% |

**Sprint 1 Goal:** Deliver core secure login functionality (biometric
authentication and MFA) to establish a secure foundation before building
payment features.

**Sprint 2 Goal:** Complete the authentication and fraud-detection work
carried over from Sprint 1, using capacity recalibrated to Sprint 1's
actual velocity instead of the original untested estimate.

## Mid-Sprint Scope Change (Sprint 1)

Partway through Sprint 1, a critical fraud-detection requirement was
escalated by the Product Owner: flagging logins from unrecognized
countries. As Scrum Master, I facilitated a scope discussion to protect
the sprint goal without exceeding team capacity — a lower-priority,
overlapping-scope story (New Device Alert) was swapped out to make room,
keeping the sprint's committed points unchanged.

See `reports/sprint1_burndown.png` for the chart annotation showing this
scope change.

## Capacity Recalibration (Sprint 2)

Sprint 1 had no historical velocity, so capacity was estimated at 25–30
points — a guess that turned out to be too high (13 points were actually
completed). Sprint 2 capacity was recalibrated to 13 points based on that
real data, and the team delivered 100% of committed scope, validating the
adjustment.

See `reports/sprint_velocity.png` for the two-sprint comparison.

## Custom Sprint Reporting

The Jira plan used for this project did not include native burndown or
velocity reporting, so I built a lightweight Python tool (`matplotlib`) to
generate all charts directly from sprint data. The script is structured
around a `SPRINTS` list, so adding a new sprint is just appending one data
block and re-running — no rewriting required.

### Run it yourself

```bash
cd scripts
pip install -r requirements.txt
python sprint_charts.py
```

This regenerates `sprint1_burndown.png`, `sprint2_burndown.png`, and
`sprint_velocity.png`.

## Full Case Study

For the complete write-up — backlog structure, sprint planning rationale,
the scope-change decision, capacity recalibration, retrospectives, and
Jira screenshots — see
[`docs/SecureBank_Mobile_Portfolio_Case_Study.pdf`](docs/SecureBank_Mobile_Portfolio_Case_Study.pdf)
(renders directly in GitHub — no download required).

## Skills Demonstrated

- Sprint planning, backlog grooming, and story point estimation
- Facilitating mid-sprint scope trade-off decisions
- Recalibrating team capacity using real velocity data across sprints
- Sprint review and retrospective documentation
- Jira administration: epics, stories, sprints, and board management
- Confluence documentation for planning and review artifacts
- Python scripting for custom sprint metrics and reporting

---
Built by Abinaya Elangovan — Certified Scrum Master (CSM) | PSM I (in progress)
