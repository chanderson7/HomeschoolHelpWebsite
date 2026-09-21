# HomeSchoolHelper website

Responsive, dependency-free product-preview website for the proposed HomeSchoolHelper iOS app.

## Run locally

```sh
python3 -m http.server 8080
```

Open http://localhost:8080. No package installation or build is required.

## Pages

- `/`: product story, planned features, workflow, and FAQ
- `/preview/`: interactive prototype, with clear limitations
- `/privacy/`: website data practices
- `/support/`: project and issue links

All local asset URLs are relative, so the site can also be served under a repository subpath. Deploy the root directory to a static host; exclude development files if desired. No hosting deployment is configured by this repository.

The prototype at `preview/demo.html` is copied from `chanderson7/HomeschoolHelper`, commit `0c0209e7696b81c5d25e160955a1efe1cf89e1d5`. It contains fictional data and memory-only interactions. App availability, pricing, storage, scheduling, and exports must not be represented as released functionality.

The homepage includes illustrative interface compositions, not actual native-app screenshots. Google Fonts are loaded for typography, with system fallbacks. The prototype may load icons from unpkg.com. There are no analytics, cookies, forms, or app backend in this implementation.

## Verification

```sh
python3 scripts/check_site.py
```

Checks internal file links and fragment targets across the authored pages.
