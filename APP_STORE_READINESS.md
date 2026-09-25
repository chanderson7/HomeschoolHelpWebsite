# App Store website and policy readiness

Reviewed September 25, 2026 against iOS repository commit `72bf4ad7adf5a5d56104b1eb40774700789cf817`. The iOS README is stale: actual source includes Supabase accounts and manual cloud backups. This document is a handoff checklist, not a declaration of approval or legal compliance.

## Website routes

The app already references `https://homeschoohelp.netlify.app` (spelling preserved). Its existing privacy route returned HTTP 200 on September 25. After deployment, verify actual content at every URL, not just HTTP status; a host can return its homepage for missing paths.

| App Store field or purpose | URL | Status |
| --- | --- | --- |
| Marketing URL | https://homeschoohelp.netlify.app/ | Updated current development features |
| Privacy Policy URL | https://homeschoohelp.netlify.app/privacy/ | App + website disclosure prepared; operating details pending |
| Support URL | https://homeschoohelp.netlify.app/support/ | Help and source-listed email addresses; mailbox verification pending |
| Terms of Service | https://homeschoohelp.netlify.app/terms/ | New service terms, distinct from Apple EULA |
| User Privacy Choices URL (optional field) | https://homeschoohelp.netlify.app/data-choices/ | Current controls and limitations; NOT a deletion service |

Apple requires publicly accessible privacy and support URLs. A separate custom terms page is not a universal substitute for an EULA: Apple's standard EULA applies when no custom license is supplied. Subscription-specific requirements must be revisited if subscriptions are added; none were found in this build. Website pages do not by themselves satisfy in-app account-deletion requirements.

## Before submitting — unresolved

1. **Implement account deletion in the native app.** Account creation exists, but AccountView offers sign-out and backup/restore only. No user-deletion endpoint or flow was found. Apple requires users to be able to initiate full account deletion in-app. A mailto link is not an adequate substitute for this app. Design verification, session handling, cloud deletion, local cleanup, timing, and completion feedback; test with disposable accounts.
2. **Verify the actual deployed backend.** The checked-in migration provides owner-scoped RLS and a foreign key that cascades backup deletion when an auth user is deleted. This source review did not inspect production data, verify migration deployment, or test deletion. Do not equate SQL permission to delete backup rows with a working account-deletion feature.
3. **Confirm the legal operator and contact details.** The app lists `support@homeschoolhelper.app` and `privacy@homeschoolhelper.app`; copied as source-listed contacts, but delivery/monitoring is not verified. Confirm the responsible individual/business name and applicable contact/address details. Do not submit with unmonitored mailboxes.
4. **Establish actual retention rules.** No automatic snapshot expiry is in the source. A `.limit(20)` history query is not deletion. Define account and backup retention, deletion processing time, exceptions, recovery-copy aging, service logs, support messages, region/provider arrangements, and the process for rights requests. Replace development limitations with actual operational commitments only after they are implemented.
5. **Align the native legal text.** `iOS/HomeSchoolHelper/LegalContent.swift` currently claims complete offline access, no operator access, working backup deletion, and JSON export. The reviewed code does not support these promises. Sign-in is remotely verified at launch and foregrounding; account files remain after sign-out; backups are manual; deletion/export controls are absent. Update the app text to match confirmed behavior and these web disclosures.
6. **Correct the native Terms URL.** In `LegalContent.swift`, `.termsOfService.externalURL` currently points to the homepage. Change it to `https://homeschoohelp.netlify.app/terms/`. Keep privacy/support URLs aligned with the chosen final domain. Ensure legal information is accessible before account creation as well as in Settings.
7. **Complete App Store privacy answers from real operations.** Do not select “Data Not Collected”: account email and IDs are sent to authentication, and learner/school content is uploaded when a backup is requested. Review Email Address, User ID, Name and Other User Content categories, linkage to account identity, app-functionality purposes, and actual service/security logs against Apple's definitions. Optional backup use does not automatically remove disclosure obligations. Website font requests are separate from native-app behavior. Confirm telemetry and SDK practices in the submitted binary.
8. **Verify release metadata and review access.** Supply an active reviewer account or suitable full-featured review mode, working backend, actual native screenshots, device support, privacy manifest/required-reason API declarations as applicable, and truthful release features. Do not use the browser prototype as proof of implemented transcript/grade features.
9. **Review policy wording for the actual release.** The current legal pages deliberately state development limitations. Resolve the operator, contacts, retention, deletion, and any jurisdiction-specific obligations before treating them as final launch policies. No blanket COPPA/GDPR compliance or approval guarantee is made.

## Verified feature mapping

- AuthRootView + HomeschoolAuth: email registration, confirmation, password recovery, session validation; release UI is gated on verified sign-in.
- HomeschoolCore + HomeschoolStore: learner names/grade levels, courses, ordered lessons, dated/flexible assignments, status and dates, attendance/minutes, retrospective activities; per-account local JSON files.
- HomeTabView: learner filters, course roadmaps, lesson date/status editing, move-overdue-to-today, attendance confirmation, shared activities.
- AccountView: manual snapshot upload, latest-20 list, restore replacing local state, optional legacy local import. No continuous sync, deletion UI, or export UI.
- SettingsView: account access, preferences, record counts, legal and support links.
- Migration `20260925001249_school_backups.sql`: snapshot JSON linked to user ID, size/schema checks, owner-scoped non-anonymous policies, cascade on auth-user deletion. Deployment not verified.

## Apple references checked

- [App review: support and privacy links](https://developer.apple.com/app-store/review/)
- [Privacy policy URL and privacy answers](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy)
- [Account deletion requirements](https://developer.apple.com/support/offering-account-deletion-in-your-app/)
- [Standard versus custom EULA](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement/)
- [App privacy details](https://developer.apple.com/app-store/app-privacy-details/)
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

## Verification performed for this change

- Local file/fragment checks cover all six authored pages, including new legal navigation.
- Native app feature/data claims traced to the source revision above; no production user data accessed.
- Public pre-change privacy URL confirmed HTTP 200; verify newly deployed content separately after pushing.
