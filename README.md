# HomeSchoolHelper website

Responsive, dependency-free product-preview website for the proposed HomeSchoolHelper iOS app.

## Run locally

```sh
python3 -m http.server 8080
```

Open http://localhost:8080. No package installation or build is required.

## Pages

- `/`: current native development features, future scope, workflow, and FAQ
- `/preview/`: interactive prototype, with clear limitations
- `/privacy/`: native app and website data practices
- `/support/`: account, records, backup help, and contact links
- `/terms/`: service terms and Apple standard EULA reference
- `/data-choices/`: automatic backup, export, subscription, local-data, and deletion controls
- `/auth/callback/`: safe browser fallback for app authentication links
- `/.well-known/apple-app-site-association`: iOS universal-link association for authentication callbacks

All local asset URLs are relative, so the site can also be served under a repository subpath. Deploy the root directory to a static host; exclude development files if desired. The iOS app references https://homeschoohelp.netlify.app. Netlify reads `_headers` to serve the Apple association file as JSON and keep authentication callbacks out of caches; verify the deployed responses after pushing.

The prototype at `preview/demo.html` is copied from `chanderson7/HomeschoolHelper`, commit `0c0209e7696b81c5d25e160955a1efe1cf89e1d5`. It contains fictional data and memory-only interactions. App availability, pricing, storage, scheduling, and exports must not be represented as released functionality.

The homepage includes illustrative interface compositions, not actual native-app screenshots. Google Fonts are loaded for typography, with system fallbacks. The prototype may load icons from unpkg.com. There are no analytics, cookies, forms, or app backend in this implementation.

## Verification

```sh
python3 scripts/check_site.py
```

Checks internal file links and fragment targets across the authored pages, plus the Apple association file's application identifier and callback path.

## September 25 app review

Website claims were rechecked against iOS source commit `bb8bb85`. The native source now includes grades, reports and exports, reading logs, portfolios, StoreKit subscriptions, automatic and manual cloud snapshots, a privacy manifest, and in-app deletion. The browser demo remains the older concept. See [App Store readiness](APP_STORE_READINESS.md) for remaining account-mode, backend, contact, retention, StoreKit, universal-link, privacy, and release-validation work. The web pages alone do not establish approval readiness.
