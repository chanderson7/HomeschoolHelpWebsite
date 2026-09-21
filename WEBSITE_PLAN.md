# HomeSchoolHelper website plan

## Purpose and source

Introduce HomeSchoolHelper to homeschooling parents, explain the proposed iOS experience, and help families explore the design. Start with a product-preview website; evolve it into an App Store marketing site when the app is available.

Reviewed [chanderson7/HomeschoolHelper](https://github.com/chanderson7/HomeschoolHelper) at commit `0c0209e7696b81c5d25e160955a1efe1cf89e1d5` on September 20, 2026. The repository contains documentation and a thirteen-screen interactive HTML prototype, not production iOS source. Features below are proposed capabilities, even where a prototype interaction exists.

Primary sources: [product baseline](https://github.com/chanderson7/HomeschoolHelper/blob/0c0209e7696b81c5d25e160955a1efe1cf89e1d5/docs/product-baseline.md), [screen specifications](https://github.com/chanderson7/HomeschoolHelper/blob/0c0209e7696b81c5d25e160955a1efe1cf89e1d5/docs/screens.md), and [roadmap](https://github.com/chanderson7/HomeschoolHelper/blob/0c0209e7696b81c5d25e160955a1efe1cf89e1d5/docs/roadmap.md).

## Audience and positioning

Primary audience: parents coordinating lessons and records for one or more children, including families who mix structured curriculum with flexible or unplanned learning.

Core promise: **Plan the week, adapt when life changes, and keep a reliable record of learning.**

Organize the story around the parent's workflow: **Plan → teach → adjust → record → export.** Explain useful outcomes before listing individual tools. Use a warm, practical voice without promising effortless homeschooling or guaranteed academic results.

## Recommended site structure

Begin with a focused homepage and a separate interactive preview. Avoid separate thin pages for every feature.

| Route | Purpose | Initial content |
|---|---|---|
| `/` | Explain the product and its benefits | Hero, feature groups, workflow, screen gallery, FAQ, final preview link |
| `/preview` | Let visitors explore the concept | Existing prototype with a clear demo notice and return navigation |
| `/privacy` | Explain website data practices | Actual hosting, analytics, and form practices once selected; distinguish website practices from future app plans |
| `/support` | Provide a contact route | Verified support address or working contact method, plus availability FAQ |

Homepage navigation: Features · How it works · Screens · FAQ. Primary action: **Explore the prototype**. Add **Get launch updates** only after a working email collection service, consent text, and privacy information exist. Do not display an App Store download badge before a verified listing is available.

## Homepage outline and suggested copy

### 1. Hero

- Status label: **An iOS app in development**.
- Heading: **A clearer plan for your homeschool day.**
- Supporting copy: “HomeSchoolHelper is being designed to bring lessons, flexible schedules, and learning records together—so you can see what's next for each child and keep track of the work along the way.”
- Primary action: **Explore the prototype** → `/preview`.
- Secondary action: **See planned features** → feature section.
- Visual: Today screen, with a smaller weekly-plan preview alongside it on desktop. Use one readable screen on mobile.
- Caption: “Design preview with fictional sample data. Features are still in development.”

### 2. Three core benefits

1. **See the day clearly.** A proposed daily checklist brings each child's next lessons into view.
2. **Make room for real life.** Flexible planning is intended to help you review unfinished work and proposed schedule changes.
3. **Keep learning records together.** Planned attendance, grades, and reports connect daily organization with longer-term recordkeeping.

### 3. Feature walkthrough

Use four alternating text-and-screen sections. Label the whole area “Planned features” and keep meaningful status distinctions visible in each section.

| Group | Parent-facing message | Features to explain | Prototype visuals |
|---|---|---|---|
| Daily learning | **Know what's next for every child.** | Child filters, daily assignments, completion history, household overview | Today; Family |
| Flexible planning | **Build a lesson sequence. Adjust as life happens.** | Courses, ordered lessons, eligible teaching days, weekly view; proposed missed-day changes reviewed before confirmation | Build lessons; Sequence preview; Weekly plan; Missed-day recovery |
| Learning records | **Give your family's learning a clear record.** | Explicit attendance and instructional time, grades, final course results, planned report and transcript exports | Attendance; Grades; Transcript preview |
| Learning beyond the plan | **Leave room for the learning you didn't schedule.** | Proposed retrospective entries and activities shared across children | Editorial illustration or simple workflow; no existing screen should be presented as this feature |

Keep reading logs and household spending in a smaller “Ideas for later” area, rather than giving them equal weight with the core experience.

### 4. How it is intended to work

Five short steps with a concrete family scenario:

1. **Plan:** Create a course, enter its lesson sequence, and choose teaching days.
2. **Teach:** Review each child's work and record what was completed.
3. **Adjust:** When a day changes, review proposed moves for unfinished lessons.
4. **Record:** Confirm attendance and time; enter grades separately where needed.
5. **Export:** Review and finalize records before producing a report, once exports are implemented.

Do not suggest that checking off a lesson automatically awards attendance, grades, or credits.

### 5. Screen gallery

Show six selected screens: Today, Weekly plan, Build lessons, Missed-day recovery, Attendance, and Transcript preview. Each needs a short benefit caption and a visible “Design preview” label. Let visitors open larger images or the interactive preview. Keep body copy outside screenshots so it remains readable and accessible.

The full thirteen-screen gallery belongs on `/preview`. Explain there that edits reset on reload, schedules and reports use sample data, and PDF export is not implemented.

### 6. Product direction

Heading: **Built around the way families actually learn.**

Discuss intended principles: support multiple children, allow ordered work without mandatory dates, explicitly confirm records, and provide family-controlled exports. Describe local storage and recovery as implementation goals, not verified privacy, security, or backup guarantees.

### 7. FAQ

| Question | Draft answer |
|---|---|
| Can I download the app today? | HomeSchoolHelper is currently a design prototype and development plan. There is no released app linked from this site yet. |
| Can I plan for more than one child? | Multi-child planning is part of the proposed core experience. The prototype illustrates child filters and a household overview. |
| What if our schedule changes? | The planned workflow lets parents review proposed moves for unfinished lessons before applying them. The prototype demonstrates the flow using sample data. |
| Can I record learning after it happens? | Retrospective and shared learning entries are included in the proposed release scope; their screens have not yet been designed. |
| Will it track attendance and grades? | Both are planned. Attendance, grades, and lesson completion will be recorded explicitly rather than treated as interchangeable. |
| Can I export a transcript? | Transcript previews are in the design. Actual report generation and PDF/CSV exports still require implementation. |
| What will it cost? | Pricing is being evaluated and has not been finalized. |
| Which devices will it support? | The product is being planned for iOS. Minimum iOS version and device support are still being decided. |

### 8. Closing action and footer

Heading: **See how a homeschool day could come together.**

Action: **Explore the prototype**. Once launch updates are operational, use that as the secondary action. Footer: HomeSchoolHelper, development status, Privacy, Support, and copyright information verified with the owner.

## Feature accuracy checklist

| Capability | Repository evidence | Website treatment |
|---|---|---|
| Daily checklist and child filters | Interactive, memory-only prototype | Demonstrate with sample-data notice |
| Lesson sequence builder | Editable form; fixed preview independent of inputs | Planned capability; avoid claiming working generation |
| Missed-day recovery | Sample confirm/undo toggle | Describe intended preview-and-confirm behavior |
| Attendance and hours | Illustrative confirmation and totals | Planned recordkeeping, not a verified attendance engine |
| Grades and transcripts | Sample values and document preview | Planned reports; no working export claim |
| Retrospective/shared activities | Required in baseline; missing screen design | Planned feature without fabricated app screenshots |
| Reading logs and budgeting | Prototype screens; later candidate scope | Clearly labeled ideas for later |
| Receipt capture | Not implemented | Omit from core marketing |
| Cloud sync and student access | Deferred roadmap | Omit from launch feature promises |
| Pricing | $29/year and $39/year hypotheses | Say pricing is not finalized; no purchase flow |
| Local persistence and recovery | Proposed implementation | State as goals only |

Also omit testimonials, user counts, ratings, savings claims, release dates, compliance guarantees, AI tutoring, and unlimited storage unless independently established later. Crop or annotate the prototype's proposed-price screen if it appears in promotional imagery.

## Visual direction

- Preserve the prototype's calm sage palette: background `#F5F6F1`, white cards, dark green text `#223B30`, accent `#365C45`, and pale green surfaces `#E6EDDF`. Check contrast in the final implementation.
- Use a readable system sans-serif, generous spacing, rounded cards, and restrained phone frames. Large headings should feel welcoming without looking like a children's worksheet.
- Make the actual product screens the main visuals. Avoid unrelated stock classroom imagery.
- Desktop: text and screen pairs, a three-column benefit row, and a compact gallery. Mobile: single-column content, one primary screen at a time, and comfortably sized controls.
- Use semantic headings, descriptive links, meaningful image alternatives, keyboard-operable galleries, visible focus states, and reduced-motion support. Do not require animation or horizontal scrolling to understand the page.

## Delivery plan

### Stage 1 — Preview website

Build the responsive homepage and a wrapped version of the existing interactive prototype. Create readable screen assets from the repository's sample data. Add source-backed copy, metadata, social sharing imagery, and working navigation. Publish privacy and support pages only with accurate operational details. A static site is sufficient for this scope; choose implementation and hosting when the build begins.

Acceptance: all feature claims reflect their current status; every action works; the preview explains its limitations; content remains usable on mobile and by keyboard; no placeholder download or signup actions remain.

### Stage 2 — Family feedback and launch interest

After selecting the service and contact owner, add an optional launch-update form with email validation, consent, error/success states, duplicate handling, and unsubscribe support. Collect minimal information. Invite families to share planning challenges only through an explicitly configured feedback route. Measure prototype interest and voluntary signup conversion if analytics are enabled and disclosed. Avoid collecting children's educational records.

Acceptance: a real submission reaches the intended service, operational messages work, and privacy text matches actual collection and retention practices.

### Stage 3 — App launch website

Replace design imagery with actual app screenshots, verify shipped features, add a real App Store link, confirm device support and pricing, and update support/privacy information. Move unfinished capabilities into a clearly separate roadmap or remove them. Add dedicated feature pages only when useful content warrants them.

Acceptance: download links resolve correctly; screenshots match the release; pricing and availability are verified; support and legal content reflect the operating product.

## Assets and decisions needed before publishing

- Confirm public brand styling: use **HomeSchoolHelper** consistently for now.
- Approve or create the app icon/logo; text branding is enough for the first preview build.
- Choose domain and hosting, and provide the support contact.
- Decide whether launch-update collection is needed at the preview stage and select its provider if so.
- Capture and review the six featured prototype screens, including any price/status annotations.
- Verify website data practices and any analytics before writing the final privacy page.
- Keep pricing, release timing, and minimum device requirements unpublished until settled.

## Suggested first build scope

One polished homepage, one interactive-preview route, six prototype screen images, and verified support/privacy content. Lead with daily clarity, flexibility, and records. This makes the application concept understandable now and provides a direct path to a launch site later.
