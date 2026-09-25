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
- `/data-choices/`: current account and data controls, including deletion limitations

All local asset URLs are relative, so the site can also be served under a repository subpath. Deploy the root directory to a static host; exclude development files if desired. The iOS app references https://homeschoohelp.netlify.app. No deployment configuration is stored in this repository; verify Netlify deployment status after pushing.

The prototype at `preview/demo.html` is copied from `chanderson7/HomeschoolHelper`, commit `0c0209e7696b81c5d25e160955a1efe1cf89e1d5`. It contains fictional data and memory-only interactions. App availability, pricing, storage, scheduling, and exports must not be represented as released functionality.

The homepage includes illustrative interface compositions, not actual native-app screenshots. Google Fonts are loaded for typography, with system fallbacks. The prototype may load icons from unpkg.com. There are no analytics, cookies, forms, or app backend in this implementation.

## Verification

```sh
python3 scripts/check_site.py
```

Checks internal file links and fragment targets across the authored pages.

## September 25 app review

Website claims now follow iOS source commit `72bf4ad7adf5a5d56104b1eb40774700789cf817`. The native app now has authentication, local records, and manual cloud backup/restore. The browser demo remains the older concept. See [App Store readiness](APP_STORE_READINESS.md) for outstanding account deletion, contact verification, retention, privacy-label, and native legal-text work before submission. The web pages alone do not establish approval readiness.
