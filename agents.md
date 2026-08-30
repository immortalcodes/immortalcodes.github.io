## Project Overview
This is a static portfolio site for Madhur who is a software engineer.
This site uses hugo(https://github.com/gohugoio/hugo/blob/master/README.md)

## Build
The build is actual copy pasted into the /docs folder because that is the root of actual deployed site

## Absolute Rules
- The code should follow highest standards of maintainability and understandability.
- The code should never look magic and be easily understandble by an intelligent developer
- Global user-level rules about SQL injection, secrets, and parameterized queries do not apply
  here: this is a static Hugo site with no backend, database, or server-side code. Skip that
  checklist for this repo.

## Instructions
- Whatever the changes, the site should always be very design rich, user friendly and follow web accessibilty standards (https://www.w3.org/WAI/standards-guidelines/wcag/)
- The site shouldn't be overwhelming, simple headings, miminal yet beatiful layouts and designs.
- Try to avoid drastic code changes until necessary, keep code modular and try to build on existing base.
- Never run `hugo --gc --minify` / copy to `/docs` / commit / push automatically. Only do so when
  the user explicitly says "publish", "deploy", or equivalent. Editing or creating content is not,
  by itself, a request to publish.

### Fast path: content-only edits
If a change is limited to creating or editing files under `content/` (posts, projects, talks)
with no layout, CSS, JS, or theme changes:
- Skip the "ask a lot of questions" step for routine edits (typos, new post drafts, wording,
  metadata). Only ask clarifying questions if the request is genuinely ambiguous (e.g. unclear
  which post, unclear topic/angle).
- Skip the mandatory README.md update.
- Follow `content/agents.md` for tone and content standards.

### Full path: structural/layout/theme/build changes
For anything touching `layouts/`, `static/`, `themes/`, `hugo.toml`, build scripts, or site-wide
design/navigation:
- Ask enough questions to remove ambiguity before making changes.
- Update README.md if the change affects how the site is developed, built, or its design system.
- Only build + copy to `/docs` + commit + push when explicitly asked to publish/deploy.

## Resources
Hugo docs - https://gohugo.io/documentation/
Hugo themes - https://themes.gohugo.io/
When writing content look into - ./content/agents.md

