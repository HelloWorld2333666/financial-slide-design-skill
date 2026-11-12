---
name: financial-slide-design
description: Plan and design financial and economic research decks or slides to a consulting-report standard from verified evidence: storyboard, deck identity, chart and composition choice, photographs, maps, flags, icons and logos, then rendered-slide inspection and revision. Use when asked to create a presentation or deck on a topic, a new slide or section, to make slides look professional, or to redesign a slide. Do not use for text edits, number or data changes, small moves, or questions about the evidence.
---

# Financial slide design

You are the design model. You decide what each slide argues, which visual techniques carry it, what the deck looks
like and which pictures it needs. A **host application** does the mechanical work: holding verified evidence, resolving
every figure from it, sourcing licensed assets, laying out, drawing, checking and saving (`docs/host-interface.md`).
If a design needs something the host cannot draw, follow "Renderer limits" below; never hand-draw a slide or type a figure.

Treat any earlier deck as a **quality benchmark, not a template**: match its finish, not its layouts, palette, images
or slide count.

## The loop

1. **Evidence.** Find out what the evidence supports: datasets (entities, units, periods, parts of a whole) and sourced
   facts (rating actions, statements). Plan from this, not from memory. A fact the host could not confirm on its source
   page is "reported" and the slide says so.
2. **Storyboard and identity** (load `cards/DK-deck.md`). For each slide: role, objective, message, candidate families,
   pattern, density, focal figure, visual assets. The action titles in order must read as the executive summary.
   Choose one identity for **this** topic and reader: a primary colour (the structure ramp is derived from it) and a type
   pairing (serif or sans). Never reuse a previous deck's identity by default.
3. **Each slide** (load `cards/ROUTER.md` first, then only the cards in play): analyse the claim → shortlist families
   from the router table → decide with the family cards → compose with a pattern card (P1–P7) and the modifier, anchor
   and device cards → list the assets (S1, S2, V10) → write the plan.
   `python tools/skill_knowledge.py "<objective>" --intent <intent> --role <role>` returns the cards that apply.
4. **Plan** each slide in the format of `docs/plan-format.md`: figures only as evidence tokens, charts as requests,
   cards used and rejected alternatives in `rationale`. Technique ids (T01–T84) are defined in `catalog/techniques.md`.
5. **Build and inspect.** Have the host render every slide, then **look at every rendered image** and critique against
   `cards/R-refinement.md`: hard constraints first, then practice, then judgement. Typical defects: crowded columns, a
   title running to four lines, a map framed so the mechanism is cut off, labels over data, a card or legend over what
   matters, weak focal point, empty fields. Revise the plan, not the renderer; rebuild; at most two rounds per slide.
   Act on the host's deck checks (runs of one composition, too many commentary panels, covers without imagery, country
   tables without flags, identity drift) or record why not.
6. **Deliver** the slides as editable, evidence-bound objects in the host, with the sources listed.

## Visual assets (S1, S2, V10)

- **Covers, dividers, closings:** a photograph or a map of the subject. Only public domain, CC0, CC BY and CC BY-SA
  pictures; credit them in the source line.
- **Maps** when geography is part of the mechanism (routes, chokepoints, exposure by place, contagion), not because
  countries are mentioned. Figures on a map are bound text pinned to it; map labels carry names only.
- **Flags** beside countries in tables and rankings and on country figures; **logos** for companies and agencies
  (identification only); **icons** from one set for findings, process steps, lead-ins and watch items. One marker per
  row or block, none where it adds nothing.

## Renderer limits

When a technique a card recommends is not drawable: name the limit; solve it with asset sourcing, preparation, editable
shape composition or a small, reusable renderer addition; otherwise use the card's fallback **and record what it loses**.
An empty field, an omitted map or a plain table is never a silent fallback.

## Files

- `cards/`: the design knowledge (router, 16 families, 5 modifiers, 7 patterns, device, anchor, grouping, text hierarchy,
  2 asset cards, conventions, refinement R1–R14, deck).
- `catalog/techniques.md`: the 84 techniques the cards cite.
- `docs/plan-format.md`: the slide-plan format. `docs/host-interface.md`: what a host must provide.
- `tools/skill_knowledge.py`: selective card retrieval and a knowledge consistency check.
