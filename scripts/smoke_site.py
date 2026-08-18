#!/usr/bin/env python3
"""Smoke checks for the generated ImmortalCodes site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def read(rel: str) -> str:
    path = DOCS / rel
    if not path.exists():
        raise AssertionError(f"Missing generated file: docs/{rel}")
    return path.read_text(encoding="utf-8")


def assert_has(rel: str, *needles: str) -> None:
    text = read(rel)
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise AssertionError(f"docs/{rel} missing: {', '.join(missing)}")


def assert_not_has(rel: str, *needles: str) -> None:
    text = read(rel)
    present = [needle for needle in needles if needle in text]
    if present:
        raise AssertionError(f"docs/{rel} unexpectedly contains: {', '.join(present)}")


def main() -> None:
    assert_has(
        "index.html",
        "Projects",
        "Talks",
        "Live Games",
        "Latest writing",
        "More than a blog",
    )
    assert_has(
        "projects/index.html",
        "Projects",
        "No project write-ups yet",
        "Add projects by creating Markdown files in content/projects/",
        "aria-current=page>Projects",
    )
    assert_has(
        "talks/index.html",
        "Talks",
        "No talks published yet",
        "Add talks by creating Markdown files in content/talks/",
    )
    assert_has(
        "games/index.html",
        "Code Breaker",
        "Playable in the browser",
    )
    assert_has(
        "games/code-breaker/index.html",
        "Guess the four-digit access code",
        "id=code-breaker-form",
        "aria-live=polite",
    )
    assert_has("404.html", "Page not found", "Back home")
    assert_has("CNAME", "blogs.immortalcodes.com")
    assert_has("css/site.css", ":focus-visible", "prefers-reduced-motion", "@media (max-width: 720px)")
    assert_has("js/site.js", "data-code-breaker", "attempts remaining")
    assert_has("index.xml", "React ≠ Magic", "Handmade Git Commands")
    assert_not_has("index.xml", "<title>Archive</title>", "0001")
    print("smoke_site: all generated site checks passed")


if __name__ == "__main__":
    main()
