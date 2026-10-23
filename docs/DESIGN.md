# Profile design

## Brief and reference

Redesign https://github.com/snuconnectome using https://github.com/dprvda as
the structural benchmark. Inspected its README and hero artwork on 2026-10-23.
Its useful patterns are a large personal introduction, direct navigation,
four linked visual projects, and light/dark assets. Artwork is original;
no reference imagery, personal claims, or statistics are reused.

## Design plan, reviewed before implementation

- Palette: porcelain `#F5F8FC`, midnight blue `#102A43`, teal `#087F8C`,
  violet `#6655A5`, mist `#DCE8EF`, white `#FFFFFF`.
- Type: Pretendard Bold for the name and project titles; Pretendard Regular
  for Korean and English captions. Native GitHub typography for readable,
  selectable descriptions and links. Assets embed rasterized type, requiring
  no remote font service.
- Layout: left-aligned profile identity; one neural-network illustration on
  the right. Two columns of linked projects. Native text below the artwork
  supplies descriptions at mobile sizes. Detailed Korean research is
  preserved in an expandable section.
- Distinction: a schematic of connections across scales, not stock brain
  photography, fabricated neuroscience results, or productivity metrics.
- Restraint: no animation, badges, numerical bragging, ornamental labels,
  generic gradient backgrounds, or invented performance claims.

```text
[ Jiook Cha / Connectome Lab        connection schematic ]
[ Lab website     Publications     Research code     Email ]
[ A short research question and bilingual introduction   ]
[ SwiFT artwork             ][ SwiFUN artwork            ]
[ MBBN artwork              ][ NeuroMamba artwork        ]
[ Four concise, accessible native-text code links         ]
[ Research areas: original Korean detail, expandable      ]
```

Review: rejected a generic metric strip and a decorative brain silhouette.
The final artwork uses connected signal traces and model-specific diagrams.
The diagrams are conceptual illustrations, not measured brain data.
Hero images have dedicated mobile variants. Image alt text and native text
links retain meaning when images cannot load; GitHub provides keyboard focus.

## Content provenance

- Identity, affiliation, research questions, contact and website: original
  profile README at commit `39cc111` (retained in Git history).
- Project descriptions: public READMEs of Transconnectome/SwiFT,
  Transconnectome/SwiFUN, Transconnectome/MBBN and Transconnectome/NeuroMamba.
- Repository visibility checked on 2026-10-23; only public project targets
  appear in the selected-code grid. No unpublished results or private links.
- The account is a user profile, not an organization. The native GitHub
  header, sidebar, pinned repositories and contribution graph are outside
  this README redesign.

## Regenerate

`python3 scripts/build_assets.py`

Requires Pillow and the Pretendard fonts under `~/.fonts/pretendard/`.
Set `PROFILE_FONT_DIR` to a directory containing Pretendard-Bold.ttf and
Pretendard-Regular.ttf on another machine. Assets are committed, so visitors
need no build step. No API keys, widgets or scheduled jobs are required.

## Local validation

- GitHub Markdown API rendered the README and retained all five picture
  elements, seven source elements, mobile media queries and details disclosure.
- All 12 image references resolve to local PNG assets (about 352 KiB total).
- The four original Korean research sections remain intact; only Markdown
  hard line breaks were normalized to HTML br elements.
- Light, dark and mobile hero assets were visually inspected. The PNG files
  `preview-light.png` and `preview-dark.png` are artwork contact sheets,
  not browser screenshots of the complete README.
- Native GitHub browser controls are unavailable in this session; final public
  rendering is checked with a fresh screenshot service after publication.

## Publication verification

Published on 2026-10-23 KST. Profile implementation commit: `c2caeba`.

- Remote main SHA matched the local implementation commit.
- Fresh public desktop (1440 px) and mobile (390 px) screenshots inspected.
- Mobile screenshot confirms the dedicated tall hero is selected correctly.
- Live DOM confirms all three hero sources remain nested inside its picture.
- GitHub's Markdown parser requires the linked hero HTML on one line here;
  splitting inline anchor/picture across lines detached its source elements.
- All four project URLs returned HTTP 200 without authentication.
- Dark assets were visually inspected locally; live dark-mode switching was
  not browser-tested because the available screenshot service has no theme
  control. The public DOM retains the dark-mode media sources.
