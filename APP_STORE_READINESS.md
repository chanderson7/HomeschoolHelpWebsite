# App Store website and policy readiness

Reviewed September 25, 2026 against iOS repository commit `bb8bb85`. This is a source and website handoff checklist, not a declaration of App Store approval or legal compliance.

## Public website routes

- Marketing: `https://homeschoohelp.netlify.app/`
- Privacy: `https://homeschoohelp.netlify.app/privacy/`
- Terms: `https://homeschoohelp.netlify.app/terms/`
- Support: `https://homeschoohelp.netlify.app/support/`
- Data and account choices: `https://homeschoohelp.netlify.app/data-choices/`
- Authentication callback: `https://homeschoohelp.netlify.app/auth/callback`
- Apple association file: `https://homeschoohelp.netlify.app/.well-known/apple-app-site-association`

Apple requires a public privacy policy and a Support URL with actual contact information. Apple's standard EULA applies when no custom license is supplied; this site's service terms supplement it.

## Resolve before submission

1. **Resolve the account-mode contradiction.** `AuthRootView` still shows `LoginView` for every signed-out release user and validates the session remotely at launch and foregrounding. `APP_STORE_SUBMISSION.md`, `LegalContent.swift`, and parts of Settings describe account-free, fully offline use. Either implement a durable local-only path or change every release claim and reviewer note to state that sign-in is required. Apple Guideline 5.1.1(v) asks apps without significant account-based features to allow use without login.
2. **Deploy and test account deletion end to end.** The app now has a Delete Account control and the repository includes `20260925212000_delete_user_account.sql`. Verify that the function is deployed to the production Supabase project, an authenticated user can execute it, backups and the auth user are removed, repeat/error cases are clear, and each local-data choice works. `AuthStore.deleteAccount()` currently catches a remote failure and clears the local session instead of throwing it back to `AccountView`, so the account screen can dismiss without confirming remote deletion.
3. **Configure working support and privacy channels.** DNS currently advertises no MX records for `homeschoolhelper.app`. Configure and test mail delivery, monitor both addresses, and put the responsible legal name plus any required address/phone information on the Support URL and in App Store Connect.
4. **Define operational retention.** The source has no automatic snapshot expiry. The latest-20 query limits the list, not storage. Document retention and deletion timing for accounts, snapshots, logs, support requests, and infrastructure recovery copies.
5. **Validate automatic backup and privacy disclosures.** Automatic Cloud Sync defaults on and inserts new full-state snapshots after changes and on backgrounding. Confirm this is intended for the free and Pro plans, because the paywall calls auto-sync a Pro benefit while the source does not gate it. Verify capacity, duplicate-snapshot behavior, offline recovery, restore behavior, and that App Store privacy answers cover every uploaded field.
6. **Verify portfolio behavior.** Portfolio image files are stored locally, while cloud snapshots serialize portfolio metadata and local filenames. Snapshot restore cannot restore the actual images. Confirm deletion removes image files, account deletion choices behave as described, backup UI explains the limitation, and product copy does not imply photo backup.
7. **Verify StoreKit in App Store Connect.** The repository contains monthly and annual StoreKit test products, purchase/restore code, a management sheet, and paywall text. Create and approve matching production products and subscription group, attach review screenshots, verify tax/banking agreements, localizations, pricing, trial eligibility, renewal disclosures, restore, cancellation, expiration, refunds, family sharing, and feature gates. Avoid hard-coded trial claims unless StoreKit reports the offer for the current user.
8. **Validate the privacy manifest from a release archive.** `PrivacyInfo.xcprivacy` now declares email, user ID, other user content, UserDefaults reason `CA92.1`, and file timestamps reason `C617.1`. Use Xcode's privacy report to inspect the app and Supabase package, confirm every required-reason API and collected-data category, and keep App Store Connect answers aligned. Include StoreKit purchase/entitlement behavior, Open Library ISBN requests, camera/photo permissions, and service logs in the review.
9. **Deploy and validate universal links.** The app's production auth callback uses `https://homeschoohelp.netlify.app/auth/callback`. This website now includes an AASA file with application identifier `26BWL2RFDX.com.chanderson7.HomeSchoolHelper` and a no-cache JSON header. After deployment, verify the exact response has no redirect and the correct content type, reinstall the signed app, then test signup confirmation and password recovery. Replace the wildcard AASA copy currently stored in the iOS repository.
10. **Make native legal text factual.** `LegalContent.swift` claims account-free offline use and “never access or inspect” records, despite mandatory remote verification and infrastructure-level administrative access. It also presents prices and trial details as fixed. Align the in-app documents with the deployed app, the public policy, actual operator practices, and StoreKit product data.
11. **Verify release metadata and reviewer access.** The project still reports version `0.1.0`, build `1`, and iOS 17.0. Confirm app name, subtitle, categories, age-rating answers, copyright, export compliance, availability, screenshots, device compatibility, review notes, seller identity, and EU trader status. The current reviewer guide contains a plaintext demo password; provision and rotate a dedicated non-sensitive review account if sign-in remains required.
12. **Test the actual release build.** Archive with the production configuration and exercise first launch, onboarding, permissions, login callbacks, offline transitions, CRUD, rescheduling/undo, reports, CSV/PDF/ICS exports, camera scanning, Open Library failure, portfolio files, notifications, subscription states, automatic backup, restore, deletion, iPhone/iPad layouts, and VoiceOver/Dynamic Type. Website source review cannot establish that these flows compile or work in production.

## Verified source mapping

- `AuthRootView` and `HomeschoolAuth`: mandatory email account flow, remote session validation, password recovery, and remote deletion RPC.
- `HomeschoolCore`, `HomeschoolStore`, `PlanView`, and `TodayView`: learners, academic years/terms, courses, ordered lessons, dated/flexible assignments, CRUD, paced rescheduling, Student Mode, and local JSON persistence.
- `RecordsView` and `HomeschoolReports`: attendance, activities, grades/categories, GPA/credits, state presets, report cards, transcripts, PDF/CSV/ICS and reading exports.
- `ReadingLogView` and `ISBNScannerView`: books, reading sessions, device barcode scanning, and Open Library ISBN lookup.
- `PortfolioView` and `PortfolioStorage`: portfolio metadata plus locally stored image files.
- `CloudSyncManager` and `AccountView`: automatic snapshots enabled by default, manual snapshots, latest-20 list, restore, and account deletion choices.
- `SubscriptionManager` and `PaywallView`: StoreKit 2 monthly/annual subscriptions, entitlement checks, purchase, restore, and manage-subscription UI.
- `PrivacyInfo.xcprivacy`, entitlements, Info.plist, and website AASA: privacy declarations, camera/photo descriptions, encryption flag, and associated-domain configuration.

## Primary references

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Offering account deletion in your app](https://developer.apple.com/support/offering-account-deletion-in-your-app/)
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)
- [Adding required-reason API entries](https://developer.apple.com/documentation/technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest)
- [App privacy details](https://developer.apple.com/app-store/app-privacy-details/)
- [Platform version information and Support URL](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information)
- [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains)
- [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/)

## Website verification

- Internal links and fragment targets are checked across the authored pages.
- Public legal pages are written to match the reviewed source, including known development limitations.
- The browser prototype remains clearly labeled as fictional and temporary.
- Production backend, StoreKit, mail delivery, release archive, App Store Connect, and signed universal-link behavior were not tested by this website review.
