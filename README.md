# SecureBank Mobile — Scrum Master Simulation Project

A self-directed Agile simulation project built to demonstrate hands-on Scrum
Master skills using Jira, Confluence, and Python. The project simulates a
mobile banking application release, covering the full Scrum lifecycle:
backlog creation, sprint planning, active sprint facilitation, mid-sprint
scope management, sprint review, retrospective, and custom sprint reporting.

## Why this project exists

I have a background in mainframe QA testing and recently completed a
Certified Scrum Master (CSM) course. This project was built to turn that
certification into demonstrable, hands-on evidence — a real backlog, a real
sprint, a real scope-change decision, and real reporting — rather than just
a line on a resume.

## Project Structure

```
securebank-mobile-scrum/
├── README.md                              This file
├── docs/
│   └── SecureBank_Mobile_Portfolio_Case_Study.docx   Full case study writeup
├── reports/
│   ├── sprint1_burndown.png               Sprint 1 burndown chart
│   └── sprint_velocity.png                Sprint velocity chart
└── scripts/
    ├── sprint_charts.py                   Python script that generates the charts
    └── requirements.txt                   Python dependencies
```

## Sprint 1 Summary

| Metric | Value |
|---|---|
| Sprint Length | 2 weeks (10 working days) |
| Team | 5 Developers, 2 QA, 1 Product Owner |
| Committed | 26 story points (7 stories) |
| Completed | 13 story points (4 stories) |
| Carried Over | 13 story points (3 stories) |
| Completion Rate | 50% |

**Sprint Goal:** Deliver core secure login functionality (biometric
authentication and MFA) to establish a secure foundation before building
payment features.

## Mid-Sprint Scope Change

Partway through Sprint 1, a critical fraud-detection requirement was
escalated by the Product Owner: flagging logins from unrecognized
countries. As Scrum Master, I facilitated a scope discussion to protect
the sprint goal without exceeding team capacity — a lower-priority,
overlapping-scope story (New Device Alert) was swapped out to make room,
keeping the sprint's committed points unchanged.

See `reports/sprint1_burndown.png` for the chart annotation showing this
scope change.

## Custom Sprint Reporting

The Jira plan used for this project did not include native burndown or
velocity reporting, so I built a lightweight Python tool (`matplotlib`) to
generate both charts directly from sprint data. The script is designed to
be extended sprint over sprint by updating a simple data dictionary.

### Run it yourself

```bash
cd scripts
pip install -r requirements.txt
python sprint_charts.py
```

This regenerates `sprint1_burndown.png` and `sprint_velocity.png`.

## Full Case Study

For the complete write-up — backlog structure, sprint planning rationale,
scope-change decision, retrospective, and Jira screenshots — see
[`docs/SecureBank_Mobile_Portfolio_Case_Study.docx`](docs/SecureBank_Mobile_Portfolio_Case_Study.docx).

## Skills Demonstrated

- Sprint planning, backlog grooming, and story point estimation
- Facilitating mid-sprint scope trade-off decisions
- Sprint review and retrospective documentation
- Jira administration: epics, stories, sprints, and board management
- Confluence documentation for planning and review artifacts
- Python scripting for custom sprint metrics and reporting

---
Built by [Your Name] — Certified Scrum Master (CSM) | PSM I (in progress)
