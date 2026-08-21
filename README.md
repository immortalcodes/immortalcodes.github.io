# ImmortalCodes

A static personal site for Madhur Jain, built with [Hugo](https://gohugo.io/). It publishes engineering notes, projects, talks, and small browser experiments.

## Develop

Run the local Hugo server from the repository root:

    hugo server

## Build and verify

The committed `docs/` directory is the deployed GitHub Pages output. Regenerate it and run the generated-site checks before publishing:

    hugo --gc --minify
    python3 scripts/smoke_site.py

## Design system

The site is dark-only. A fixed backdrop layer renders a single continuous field
behind every page, built from three independent pieces:

1. **Colour zones** — soft radial gradients that place ember and flame in the
   top-left, magenta in the bottom-left, and a near-black void down the right,
   over a diagonal base wash.
2. **Specular folds** — a restrained repeating gradient models each narrow
   pleat as a cylindrical transition from a subtle highlight through a coloured
   midtone into a deep trough. A second, much slower lighting pass varies groups
   of folds, while a dark wash keeps the texture subordinate to the content.
3. **Film grain** — an inline SVG turbulence texture blended in `soft-light` to
   break up gradient banding.

Two rules follow from that field:

- **Text sits in dark pools, not on panels.** Each block of copy carries a
  blurred radial pseudo-element behind it, so the background darkens exactly
  where words are and fades back into colour with no visible edge.
- **Structure comes from zones, not lines.** The header, the footer, section
   breaks, and the active navigation item are all expressed as gradients. The
   header and footer extend beyond their content boxes and dissolve gradually
   through long opacity masks, fading both their tint and backdrop blur into the
   field without dividing borders or visible mask edges.

Decorative pools and blooms may extend beyond their content to create those
soft transitions, so the root viewport clips horizontal paint overflow while
preserving normal vertical scrolling.

The palette is intentionally white-free; the lightest value in use is a warm
off-white (`#f7edea`) reserved for body copy. All foreground colours were checked
against the brightest points of the field and clear WCAG AA at 4.5:1, including
at the weakest edge of a text pool.

The subdued backdrop keeps headings, links, and reading surfaces at the top of
the visual hierarchy.

