# Technique catalogue (T01–T84)

Eighty-four concrete presentation techniques in thirteen categories. Each entry gives what the technique is for, when it applies (hard constraints marked **Hard**; numbers are heuristics), and what it combines with. The cards in `cards/` group these techniques into families, modifiers, patterns, devices, anchors and assets and carry the decision logic; this catalogue is the vocabulary they cite (T-numbers).


## 1. Proportion and composition

**T01 · Donut with the central figure and grey remainder**· [S2]
- **Category:** proportion of a single share.
- **Purpose:** one share read instantly, without a legend.
- **When:** a true share of a defined total (penetration, completion, market share, probability). **Hard:** valid parts of a defined whole; not for ratios that are not shares (debt/GDP is not a share). *Heuristic:* one highlighted part, or a few parts.
- **Combinations:**
 - T02 (donut pair over a table);
 - T33 (intensity), T36 (outline on a key segment);
 - T38 (small titles above each donut).

**T02 · Donut pair over a supporting table**· [S2]
- **Category:** proportion and chart–table combination (a two-tier composition).
- **Purpose:** the visuals carry the headline proportions; the table substantiates them.
- **When:** two or three key shares, plus a breakdown or extra measures for the same entities.
- **Combinations:** T01, T30 (in-cell bars), T54 (two-tier page), T80 (finding-led headers).

**T03 · Segmented donut ring with icons on the segments and callouts around it**
- **Category:** composition with identity markers.
- **Purpose:** a composition of 4–8 parts, each identified by an icon rather than a legend.
- **When:** shares of a total where the categories have recognisable icons.
- **Combinations:** T70 (category icons), T43 (callout boxes).

**T04 · Treemap combining area, colour and white icons**· [S2]
- **Category:** composition with many parts.
- **Purpose:** relative size of 5–20 categories at a glance; icons replace the legend.
- **When:** composition with many parts. **Hard:** valid positive parts of a whole, with tile area proportional to value. **Fitness test:** parts differ enough to compare by area, and every tile that needs a label (and icon) can hold it at the rendered size. Otherwise group small parts into "Other" with a note, label outside, or use ranked or stacked bars. The number of categories alone does not decide it.
- **Combinations:** T33 (intensity), T70 (white icons), T40 (callout on the key tile).

**T05 · 100% stacked bars by entity, with flags, values inside the segments and the legend above in segment order**
- **Category:** composition compared across entities.
- **Purpose:** compare the mix across countries or companies.
- **When:** components that sum to 100% per entity. *Heuristic:* few enough segments for inside labels to fit; enough entities to make a comparison.
- **Combinations:** T67 (flags), T62 (explanation cards as the legend), T33.

**T06 · Stacked columns with totals above and segment values inside**
- **Category:** composition and level over categories or time.
- **Purpose:** show both the total and its mix.
- **When:** additive, non-negative components (hard). *Heuristic:* few enough segments to label.
- **Combinations:** T40 (a total in a callout circle), T27 (bracket to the detail table), T16 (small multiples).

**T07 · 100% stacked area along process stages, with in-area callouts and a range arrow**
- **Category:** composition across a process.
- **Purpose:** show how a mix shifts from step to step (e.g. channels by purchase stage).
- **When:** shares at each of 3–6 ordered stages.
- **Combinations:** T01 (in a multi-module page), T42 (range arrow).

**T08 · Nested circles** (a part within a whole, or two growth rates)
- **Category:** proportion as area.
- **Purpose:** a striking size comparison when the exact value matters less than the ratio.
- **When:** two values, or a part and its whole; often on statement slides. **Hard:** circle area, not radius, encodes the value.
- **Combinations:** T37 (ratio statement), T57 (dark statement page).

**T09 · Proportional squares**
- **Category:** proportion as area.
- **Purpose:** compare a few magnitudes compactly, often over a map or in a grid.
- **When:** a few values with large differences (heuristic). **Hard:** square area encodes the value.
- **Combinations:** T22 (map), T08.


## 2. Comparison and ranking

**T10 · Ranked bars, one highlight against neutral peers**· [S2]
- **Category:** ranking.
- **Purpose:** position among peers.
- **When:** a cross-section with one entity, or a defined group, in focus. Honest zero baseline (hard). *Heuristic:* 4–40 entities. A **dot plot** variant suits values far from zero; a **diverging** variant suits signed values (refinement §C, V5).
- **Combinations:** T67 (flags), T68 (logos), T11 (benchmark bar), T41 (gap bracket), T33.

**T11 · Benchmark bar** (average, OECD or peer group) **inside a ranking**
- **Category:** ranking with context.
- **Purpose:** show above or below the average without a separate figure.
- **When:** a benchmark whose source and derivation are known.
- **Combinations:** T10, T67.

**T12 · Ranked table:** rank, flag, name, in-cell bar, earlier value, change, with the focus row tinted
- **Category:** ranking with precision.
- **Purpose:** rank, level and change read across one row.
- **When:** a cross-section plus an earlier period; 5–15 entities.
- **Combinations:** T67, T35 (figures panel beside it).

**T13 · Two-period increment:** the later column drawn over the earlier level, with the increment highlighted and a large "+20%"
- **Category:** comparison between two dates.
- **Purpose:** make the change itself the visual subject.
- **When:** two periods, the change is the subject, **and** the increment is clearly perceptible on a zero-based column at the rendered size. That test depends on the objective, the level and scale, the size and significance of the change, the comparison entities, and whether the form could mislead. *Heuristic only:* a relative change around 10% or more usually passes. Otherwise state the change as a figure, use T12 with a change column, or use a dumbbell or slope on a labelled scale (refinement §C, V6).
- **Combinations:** T14 (peer list), T35 (KPI), T39 (arrow to the "+20%").

**T14 · Peer benchmark list with flags beside a chart**
- **Category:** comparison context.
- **Purpose:** add peers without crowding the main chart.
- **When:** the main chart shows the focus; peers need one or two values each.
- **Combinations:** T13, T67.

**T15 · Grouped columns with metric rows (pills) aligned under the groups**
- **Category:** chart and mini-table aligned.
- **Purpose:** add derived measures (change, intent) exactly under the groups they describe.
- **When:** two to five groups with one or two derived measures each.
- **Combinations:** T13, T81 (numbered footnotes), T68 (logo grid panel).

**T16 · Small multiples in labelled rows, with an enlarged focus panel**
- **Category:** comparison by repetition.
- **Purpose:** the same comparison across many entities or buckets, on one scale.
- **When:** the same comparison across many entities or buckets. **A shared scale is required when panels are compared directly.** Different scales are acceptable for different measures or objectives when clearly labelled and not misleading (R11). *Heuristic:* 4–20 panels.
- **Combinations:**
 - T33 (two highlight tones);
 - T65 (dashed group separators);
 - T53 (implications panel).

**T17 · Scorecard or scenario matrix:** numbered rows, letter badges, gauges in cells, summary row under a heavy rule
- **Category:** assessment.
- **Purpose:** parallel evidence for one verdict.
- **When:** measures × focus and reference; or scenarios × dimensions.
- **Combinations:** T19 (sparklines), T34 (conclusion hierarchy).


## 3. Change over time

**T18 · Line chart with direct end labels** (no legend)
- **Category:** trend.
- **Purpose:** paths, turning points, divergence.
- **When:** a time series whose message is the path (trend, turning point, divergence). *Heuristic:* up to about six series and at least three periods; beyond that, use small multiples or indexed lines.
- **Combinations:** T41 (gap brackets), T20 (shaded period), T39 (connectors to the commentary), T35.

**T19 · Sparklines in table cells**, one shared window stated in the header
- **Category:** trend inside a table.
- **Purpose:** show direction beside precise values.
- **When:** every row shares the same window.
- **Combinations:** T17, T12.

**T20 · Shaded period or forecast region inside a chart**
- **Category:** trend annotation.
- **Purpose:** separate history from projection, or mark a crisis.
- **When:** a defined period with a reason to single it out.
- **Combinations:** T18.

**T21 · Timeline of dated events**· [S2]
- **Category:** time sequence.
- **Purpose:** dated milestones, policy steps.
- **When:** real dates; three to eight events.
- **Combinations:** T18 (events marked on a trend line).


## 4. Geography

**T22 · Choropleth map in palette tones with a stepped legend**
- **Category:** geography.
- **Purpose:** a regional pattern.
- **When:** geo-coded values, and **geography is the message.** A time series across countries goes to T18 instead.
- **Combinations:** T24, T25, T10.

**T23 · Proportional bubbles on a map with "now (then)" labels**
- **Category:** geography and magnitude.
- **Purpose:** where things are and how big, then and now.
- **When:** counts or amounts by location, where location matters. **Hard:** bubble area, not radius, encodes the value. *Heuristic:* about 10 markers.
- **Combinations:** T38 ("now (then)" labels), T82 ("Not exhaustive" tag), T57 (dark page).

**T24 · Map callout boxes with leader lines and trend icons in circles**
- **Category:** geography with annotation.
- **Purpose:** attach figures and direction to specific regions.
- **When:** up to about eight regions with one or two figures each.
- **Combinations:** T22, T59 (title as a design element).

**T25 · Category tags or labels placed on regions of a world map**
- **Category:** geography with categories.
- **Purpose:** show which regions hold which entities or shares.
- **When:** regional shares or lists.
- **Combinations:** T22.

**T26 · Zoom sequence:** reasoning, then a national ranking, then a local map, with chained headers
- **Category:** geography in an argument.
- **Purpose:** move from the general to the specific on one page.
- **When:** a question that narrows from country to region or city.
- **Combinations:** T10, T22, T80.


## 5. Tables and chart–table combinations

**T27 · Summary chart bracketed to the detail tables**
- **Category:** chart–table combination.
- **Purpose:** the summary shows the mix; the bracket says "this segment is explained here".
- **When:** a composition whose segments have their own detail.
- **Combinations:** T06, T28, T30, T68 (logos as row identifiers).

**T28 · Two-level table headers:** a group header spanning its columns, rules at both levels
- **Category:** table structure, an **optional** option within the tables family (V9), not a reporting default.
- **Purpose:** group columns (e.g. "2024 | 2025", "Level | Change").
- **When:** six or more columns in natural groups.
- **Combinations:** T27, T30.

**T29 · Totals row and an assumptions box beside a table**
- **Category:** table conventions.
- **Purpose:** close the table with its total; state the assumptions next to it.
- **When:** **conditional:** a totals row only when the rows are additive; an assumptions box only when figures are modelled or estimated. Part of the tables family (V9), not an always-on convention.
- **Combinations:** T17, T80.

**T30 · In-cell bars with labels inside**
- **Category:** table with visuals.
- **Purpose:** exact values and their relative size in one cell.
- **When:** one measure per column to compare across rows.
- **Combinations:** T12, T27.

**T31 · Heatmap and indicator cells** (scored comparisons)
- **Category:** table with visuals.
- **Purpose:** a pattern across a grid of scores.
- **When:** entities × criteria with an ordered scale.
- **Combinations:** T17, T33.

**T32 · Tables with icon column headers and coloured pill cells**
- **Category:** table with identity markers.
- **Purpose:** columns recognisable by icon; categorical values as coloured pills.
- **When:** company lists by category or segment.
- **Combinations:** T70 (icons), T68 (logos).


## 6. Emphasis through colour and text hierarchy

**T33 · Colour-intensity hierarchy:** darkest for the most important, a medium tone for the second, grey for the rest· [S2]
- **Category:** emphasis.
- **Purpose:** rank importance inside a chart. **The objective decides** what is darkest: the highest value, the largest change, or the target entity.
- **When:** a chart with a stated objective. It can coexist with categorical colours if the encoding stays understandable, for example when the focus uses a distinct channel such as saturation, outline or label (refinement §D3).
- **Combinations:** T10, T04, T05, T16.

**T34 · Hierarchy among written conclusions**· [S2]
- **Category:** emphasis in text.
- **Purpose:**
 - one primary insight in the strongest treatment;
 - secondary observations smaller, quieter or lower;
 - key words in bold or the emphasis colour.
- **When:** any slide with two or more observations. Avoid presenting every observation in identical boxes with identical weight.
- **Combinations:** T39 (arrow into the primary insight), T53.

**T35 · Large KPI anchor figures** (serif in the references; the typeface is an identity choice)
- **Category:** **figure anchor** (L3). It carries the message as a single figure. Its visual styling is handled separately by refinement R6.
- **Purpose:** one decisive number as the focal point.
- **When:** one to three decisive figures. Several figures work when they are ranked by size or position; avoid equal "heroes" with no order.
- **Combinations:** T13, T56 (dark split panel), T01.

**T36 · Thin outline around a key segment or cell** (e.g. a red outline on one quarter)· [S2]
- **Category:** emphasis without recolouring.
- **Purpose:** mark the key part while the rest stays grey.
- **When:** one segment, period or cell matters most.
- **Combinations:** T01, T05, T17, T40.

**T37 · Big ratio statement as the anchor** ("~2x faster")
- **Category:** **figure anchor** (L3). It carries a relation as a single figure; styling is handled by R6.
- **Purpose:** state the comparison as one number.
- **When:** when the ratio itself is the message.
- **Combinations:** T08, T57.

**T38 · "Now (then)" compact labels and small titles above each exhibit**
- **Category:** emphasis by compression.
- **Purpose:** two periods in one label.
- **When:** two periods, many markers.
- **Combinations:** T23, T12.


## 7. Annotation and reading guidance

**T39 · Arrow or connector from a data point to its conclusion**· [S2]
- **Category:** reading guidance.
- **Purpose:** lead the eye from the evidence to its meaning.
- **When:** a specific mark has a specific implication. **Not on every slide.**
- **Combinations:** T34, T53, T33.

**T40 · Callout circle or bubble anchoring a total or key value**
- **Category:** annotation.
- **Purpose:** pin the headline number to its exhibit.
- **When:** one headline figure tied to a chart.
- **Combinations:** T06, T01.

**T41 · Gap brackets with pill labels**
- **Category:** annotation.
- **Purpose:** make a difference explicit.
- **When:** two values being compared.
- **Combinations:** T18, T10.

**T42 · Range arrow across a chart**
- **Category:** annotation.
- **Purpose:** show the span between two stages or values.
- **When:** a meaningful range or progression.
- **Combinations:** T07.

**T43 · Callout boxes with leader lines** (outside the plot)
- **Category:** annotation.
- **Purpose:** explain several points without cluttering the chart.
- **When:** at most four to eight points.
- **Combinations:** T24, T03.

**T44 · Benchmark line or band in a chart**
- **Category:** annotation.
- **Purpose:** context for every value.
- **When:** a sourced benchmark.
- **Combinations:** T18, T10.


## 8. Diagrams: process, relationship, framework

**T45 · Ecosystem or network diagram:** icon circles as nodes, arrows labelled with verbs
- **Category:** relationship.
- **Purpose:** who relates to whom, and how.
- **When:** three to six actors with named relationships.
- **Combinations:** T70 (icons in nodes), T64 (join symbols), T53.

**T46 · Causal chain with bound figures and a feedback edge**
- **Category:** causality.
- **Purpose:** transmission and loops, with numbers in the nodes.
- **When:** ordered causes with accounting or estimated links.
- **Combinations:** T35.

**T47 · Serpentine (S-curve) journey:** large serif numerals 01–04, illustrations in rings, text alternating sides
- **Category:** process.
- **Purpose:** a sequence with emphasis on each stage.
- **When:** three to six ordered stages with short text.
- **Combinations:** T75 (illustrations), T66 (numerals).

**T48 · Semicircular or curved-arrow process**· [S2 split]
- **Category:** process.
- **Purpose:** progression with a sense of movement or escalation.
- **When:** three to five ordered stages that build on each other.
- **Combinations:** T70, colour transition across the stages.

**T49 · Cycle diagram**· [S2]
- **Category:** cyclical process.
- **Purpose:** a loop that genuinely recurs (credit cycle, budget cycle).
- **When:** only for true cycles. A one-way process is not forced into a circle without justification (: the geometry must match the relationship).
- **Combinations:** T70, numbered stages.

**T50 · Hierarchy or ownership tree** with shares on the edges· [S2]
- **Category:** structure.
- **Purpose:** ownership, organisation, breakdown.
- **When:** parent–child data, at most three levels on one slide.
- **Combinations:** T35 (figure per node).

**T51 · Radial lever framework:** categories as arcs, levers as wedges, an axis of ambition, rotated labels, category icons
- **Category:** framework.
- **Purpose:** two dimensions at once (category × ambition).
- **When:** many levers (10–20) in three or four categories.
- **Combinations:** T52, T70, T58 (title field left).

**T52 · Side-by-side framework comparison:** highlighted outline overlay, ghosted context, chevron banner headers
- **Category:** framework comparison.
- **Purpose:** before against after, or plan A against plan B, on the same framework.
- **When:** two configurations of the same structure.
- **Combinations:** T51, T36.


## 9. Page composition and layering

**T53 · Dominant exhibit with a full-height implications panel** (asymmetric 8/4)
- **Category:** composition.
- **Purpose:** one proof, one meaning.
- **When:** single-claim slides. A valuable pattern, but **not the default for every slide.** The deck plan watches how often it is used and how long its runs are, and allows repetition when the content is analytically parallel (refinement §D4).
- **Combinations:** T10, T16, T45, T39, T34.

**T54 · Two-tier page: headline visuals over a supporting table**· [S2]
- **Category:** composition.
- **Purpose:** message first, substantiation second.
- **When:** two or three key figures plus detail.
- **Combinations:** T02, T30.

**T55 · Multi-module grid sized by weight**, each module with its own finding-led header
- **Category:** composition.
- **Purpose:** complementary evidence on one page.
- **When:** two to four sub-claims.
- **Combinations:** T26 (zoom chain), T64 (join symbols), T80.

**T56 · Dark split KPI panel with a gradient**
- **Category:** composition with a colour field.
- **Purpose:** set the decisive figures apart from the evidence.
- **When:** two or three KPIs that summarise the page.
- **Combinations:** T35, T13.

**T57 · Full-bleed dark statement page**
- **Category:** composition for statements.
- **Purpose:** a pause slide carrying one comparison or map.
- **When:** a statement or regional definition, not a dense evidence page.
- **Combinations:** T08, T37, T23.

**T58 · Title field beside content** (asymmetric split)
- **Category:** composition.
- **Purpose:** the title becomes a block; the content gets the rest.
- **When:** frameworks, summaries, levers.
- **Combinations:** T51, T66, T77.

**T59 · Title as a design element, placed lower-left over a map or image**
- **Category:** composition.
- **Purpose:** make the title part of the picture on statement slides.
- **When:** map- or image-led statement slides only.
- **Combinations:** T22, T24.

**T60 · Layered composition:** line pattern + cutout photograph + title, or a cutout blended into a gradient· [S2 split]
- **Category:** layering.
- **Purpose:** depth and refinement on covers, dividers and statements.
- **When:** navigation and statement slides; sparingly on content slides.
- **Combinations:** T76, T77, T78.


## 10. Grouping and separation

**T61 · Separation by whitespace and subtle background fields, not heavy rules**· [S2]
- **Category:** grouping.
- **Purpose:** clear grouping without visual noise.
- **When:** a recommended default. Subtle borders, rules and decorative linework remain allowed when they improve grouping or are intentional; avoid heavy or awkward borders between coloured regions (R3, R5).
- **Combinations:** everything.

**T62 · Rounded explanation cards coloured like the chart's segments** (the legend becomes the argument)· [S2]
- **Category:** grouping and legend.
- **Purpose:** each card explains one segment, so no separate legend is needed.
- **When:** two to four segments, each with something to say.
- **Combinations:** T05, T06.

**T63 · Rounded highlight cards for key messages; straight edges kept for tables and charts**· [S2 split]
- **Category:** grouping and shape language.
- **Purpose:** soften emphasis boxes without blurring structure.
- **When:** cards and highlights. Tables and analytical charts usually keep straight edges.
- **Combinations:** T34.

**T64 · Join symbols on the divider between modules** ("+" for "and", "»" for "therefore")
- **Category:** grouping and logic.
- **Purpose:** say how the modules relate.
- **When:** multi-module pages with a logical link.
- **Combinations:** T55, T45.

**T65 · Dashed separators between groups of panels**
- **Category:** grouping.
- **Purpose:** separate groups (advanced and emerging economies) without boxes.
- **When:** small multiples or rows in natural groups.
- **Combinations:** T16.

**T66 · Numbered circles or large serif numerals for sequences and levers**
- **Category:** grouping and order.
- **Purpose:** give lists an order and a visual rhythm.
- **When:** recommendations, stages, levers.
- **Combinations:** T47, T58.


## 11. Identity markers: flags, logos, icons

**T67 · Country flags beside categories**
- **Category:** identity marker, **data-label role**. The primary definition of all identity markers (T67–T72) is in the refinement document, Layer 4c; T69 and T72 are other placement roles of the same markers.
- **Purpose:** instant recognition; less reading.
- **When:** country categories only.
- **Combinations:** T10, T12, T05, T14, T22.

**T68 · Company logos:** as row identifiers, or as a logo grid in a panel
- **Category:** identity.
- **Purpose:** recognise brands.
- **When:** company categories; logos of consistent quality and size; usage rights checked.
- **Combinations:** T10, T27, T32.

**T69 · Context marker beside the title:** a country flag or a topic icon badge
- **Category:** identity marker, **page-context role** (see T67 for the primary definition).
- **Purpose:** signal the subject before the title is read.
- **When:** country or topic decks; one marker.
- **Combinations:** T79.

**T70 · Category and product icons from one consistent set** (white inside tiles, nodes, column headers)· [S2]
- **Category:** identity.
- **Purpose:** identify segments without a legend.
- **When:** product or category data; one icon style per deck.
- **Combinations:** T04, T03, T45, T32, T49.

**T71 · Real product imagery for product categories**· [S2 split]
- **Category:** identity and imagery.
- **Purpose:** show the actual products or equipment.
- **When:** company or product decks (e.g. medical equipment).
- **Combinations:** T73, T60.

**T72 · Topic icons along a slide edge**
- **Category:** identity marker, **module-topic role** (see T67 for the primary definition).
- **Purpose:** reinforce the subject of each module.
- **When:** multi-module pages with distinct topics.
- **Combinations:** T55.


## 12. Imagery and decoration

**T73 · Topic photograph cropped into a field** (half slide, or an edge)
- **Category:** imagery.
- **Purpose:** reinforce the subject: French architecture, ports, equipment.
- **When:** covers, dividers, closings; also on content slides where appropriate (cropped away from the data, or as a contained image card). Not behind dense evidence.
- **Combinations:** T58, T60.

**T74 · Duotone cutout anchored to a corner**
- **Category:** imagery.
- **Purpose:** an image tinted in the palette, integrated rather than boxed.
- **When:** covers, statement slides.
- **Combinations:** T76, T60.

**T75 · Illustrations in rings, or isometric illustrations as column headers**
- **Category:** imagery.
- **Purpose:** characterise stages or topics.
- **When:** journeys, multi-column overviews.
- **Combinations:** T47, T32.

**T76 · Fine line-pattern geometry** (fanning lines) as texture
- **Category:** decoration.
- **Purpose:** refined texture on covers.
- **When:** covers and dividers only.
- **Combinations:** T74, T60.

**T77 · Thematic line-art motif**
- **Category:** decoration.
- **Purpose:** a subject hint at a small size.
- **When:** usually small. Your guidance stands: crude, low-detail line art should not be enlarged excessively. The exact balance of scale, complexity and fidelity is a design judgement (R12).
- **Combinations:** T58.

**T78 · AI-generated decorative assets** (illustrations, custom icons, backgrounds)· [S2]
- **Category:** imagery production.
- **Purpose:** distinctive visuals where no licensed image exists.
- **When:** only after the visual approach is chosen; decorative only; never data.
- **Combinations:** T73–T75.


## 13. Reporting conventions

**T79 · Action title** (one conclusion sentence, 30–36 pt)
- **Category:** furniture.
- **Purpose:** the slide's message in one line.
- **When:** every content slide.
- **Combinations:** T80.

**T80 · Finding-led exhibit header with a unit line and a hairline**
- **Category:** furniture and hierarchy.
- **Purpose:** each exhibit states its sub-finding; the unit and date follow.
- **When:** every exhibit.
- **Combinations:** T55, T26.

**T81 · Numbered footnotes** (superscripts on labels, notes above the source)
- **Category:** furniture.
- **Purpose:** precise caveats without clutter.
- **When:** definitions, breaks in series, estimates.
- **Combinations:** T15.

**T82 · Caveat tags** ("Not exhaustive", "Illustrative") **beside the exhibit header**
- **Category:** furniture.
- **Purpose:** honest framing of partial or illustrative content.
- **When:** partial lists, examples, directional figures.
- **Combinations:** T23.

**T83 · Page numbers**
- **Category:** furniture.
- **Purpose:** a reporting convention.
- **When:** every slide except the cover.
- **Combinations:** —

**T84a · Source line**
- **Category:** reporting convention (L5), **always on** for data slides.
- **Purpose:** traceability.
- **When:** every slide that shows data.

**T84b · Legends and direct labels**
- **Category:** chart labelling **modifier** (L2).
- **Purpose:** readability.
- **When:**
 - direct labels where they fit;
 - a legend in data order where they don't.
 - Legend, direct labels and explanation cards may coexist when each has a distinct job.
- **Combinations:** T18, T05, T62.
