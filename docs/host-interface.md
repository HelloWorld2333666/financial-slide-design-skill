# Host interface

The Skill holds design knowledge and the planning procedure. Producing slides needs a host application that implements
the capabilities below. The reference host is **financial-research-to-report (FRR)**; the second column says where FRR
implements each one, as a model for other hosts.

| Capability the Skill relies on | Contract | FRR implementation |
|---|---|---|
| Evidence store | Datasets (entity, geo, metric, unit, periods, observations each bound to an evidence record) and sourced facts | Project bundle; `app/server/imf.py`, Eurostat fetchers, `deck.py fact` |
| Evidence profile | List what the evidence supports, for planning | `deck.py profile <project>` |
| Figure tokens | Resolve `{{num …}}`, `{{change …}}`, `{{gap …}}`, `{{spread …}}`, `{{ev …}}` from evidence; refuse typed figures | `app/web/src/core/design/plans.ts` (`resolvePlan`), `insight.ts` (`Writer`) |
| Chart requests | Turn `{intent, family, datasets, periods}` into a valid chart spec or refuse with a reason | `app/web/src/core/recommend.ts` |
| Validation | No unsourced or stale figure; valid charts; words only on maps and diagram edges | `app/web/src/core/design/spec.ts` (`validateDesign`) |
| Layout and drawing | Compositions (`columns`, `cover`, `statement`, `wide`, `bands`, …), designed charts, maps, icons, pictures as editable objects | `app/web/src/core/design/compose.ts`, `build.ts`, `charts.ts`, `assets.ts` |
| Identity | One identity per deck from a primary colour and type pairing; every chart family follows it | `language.ts` (`registerIdentity`), `deck.py identity` |
| Assets | Flags, icons, map geometry, photographs and logos from allowlisted, licence-checked sources, cached outside version control with a provenance manifest, credited on the slide | `app/server/assets.py`, `/api/assets` |
| Render and inspect | Render each planned slide to an image; layout QA; deck checks; contact sheet | `deck.py build <project>`, `app/server/render_slides.py` |
| Deliver | Apply the slides to the live deck as editable, evidence-bound objects | `deck.py apply <project>` |
| In-app AI (optional) | Give the host's model selective card retrieval and a plan-submission tool | `app/server/skill_knowledge.py` (a copy of `tools/skill_knowledge.py`), `design_guidance` and `plan_slide` in `app/server/agent.py` |

## Keeping a host in sync

FRR reads the Skill from `.claude/skills/financial-slide-design/` in its own repository. After changing the Skill here,
copy `SKILL.md`, `cards/` and `docs/plan-format.md` (as `PLANS.md`) into that folder; FRR's `skill_knowledge.py` reads the
cards from there. The catalogue and these docs are not needed at runtime.

## Without a host

The knowledge works on its own for planning and critique: retrieve cards with `tools/skill_knowledge.py`, write plans in
`docs/plan-format.md`, and review rendered slides from any tool against `cards/R-refinement.md`. Rendering, evidence
binding and asset preparation are the host's.
