# financial-slide-design-skill

A design Skill for financial and economic research presentations: how to turn verified evidence into slides of
consulting-report quality. It covers the storyboard, the deck's visual identity, chart and composition choice,
photographs, maps, flags, icons and logos, and the inspection and revision of rendered slides.

It is written for an AI design model (Claude Code loads it as a Skill from `SKILL.md`) and for people developing the
knowledge. Rendering and evidence handling belong to a host application; the reference host is
financial-research-to-report (FRR).

## Architecture

```
SKILL.md                  the planning loop the design model follows (entry point)
cards/                    the design knowledge, one decision card per object
  ROUTER.md               always loaded: objective → candidate families, hard rules, card index
  V01–V16                 visual families (rings, ranking, two-period, time series, tables, maps, diagrams, …)
  M1–M5                   modifiers (emphasis, difference and reference markers, callouts, labels)
  P1–P7                   page patterns (dominant exhibit, two-tier, multi-module, title-led, …)
  A1 D1 G1 H1             figure anchors, relationship devices, grouping, text hierarchy
  S1 S2                   identity markers (flags, logos, icons) and imagery
  C1 R-refinement DK-deck conventions and QA, refinement principles R1–R14, deck planning
catalog/techniques.md     the 84 techniques (T01–T84) the cards cite
docs/plan-format.md       the slide-plan format (figure tokens, chart requests, compositions, assets)
docs/host-interface.md    what a host must provide, and where FRR implements it
tools/skill_knowledge.py  selective card retrieval for one slide; knowledge consistency check
tests/                    smoke tests (standard library only)
```

Each card states purpose, when it applies and when not, hard constraints, execution, combinations, alternatives and a
status row describing the reference host's renderer. Knowledge is retrieved selectively: the router and at most five
cards per slide.

## Install

As a Claude Code Skill, put this repository (or a copy) at `.claude/skills/financial-slide-design/` in the host project,
or at `~/.claude/skills/financial-slide-design/` for every project. No package install is needed; the tool and tests use
the Python 3.10+ standard library.

## Use

```bash
# the cards for one slide
python tools/skill_knowledge.py "how shipping disruption through a strait reaches Gulf budgets" --intent causality --role evidence
python tools/skill_knowledge.py "inflation since 2019 in five countries, one highlighted" --intent trend --ids
# check that every card, technique and file reference resolves
python tools/skill_knowledge.py --check
# smoke tests
python -m unittest discover -s tests
```

In a host, the design model follows `SKILL.md`: storyboard, identity, per-slide plans from the cards, build, inspect,
revise. Hosts can give their own AI the same knowledge through `tools/skill_knowledge.py` (FRR does this with
`design_guidance` and `plan_slide` tools).

## Develop

- Change knowledge in the cards, in our own words. Add a card only when no existing one covers the lesson; register it
  in `cards/ROUTER.md` and, if it should be retrievable for an intent, role or wording, in `tools/skill_knowledge.py`.
- Keep `catalog/techniques.md` as the vocabulary: cite techniques by id in the cards.
- Run `python tools/skill_knowledge.py --check` and the tests before committing.
- Sync changes into a host as described in `docs/host-interface.md`.

## Not included

Reference decks, reference images and the private design library the knowledge was studied from; any purchased
template; fetched or generated pictures; host code, data and rendered decks. Pictures used by a host are fetched at
run time from licensed sources and are never committed here.

## Licence

To be chosen before the repository is made public.
