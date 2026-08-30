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
        "Latest writing",
        "site-backdrop",
        "https://x.com/i_m_mortal_mj",
    )
    # The site is dark-only; no runtime theme switching should survive a build.
    assert_not_has("index.html", "theme-toggle", "data-theme")
    assert_has(
        "projects/index.html",
        "Projects",
        "Lumina Studio: A Zero Dependency AI Creative Suite",
        "aria-current=page>Projects",
    )
    assert_has(
        "talks/index.html",
        "Talks",
        "Juju Does Everything",
    )
    assert_has(
        "talks/juju-does-everything/index.html",
        "Juju Does Everything. Here Is What That Is Like.",
        "UbuCon Asia 2026",
        "on-stage-wide.png",
        "on-stage-portrait.png",
        "venue.png",
        "audience.png",
    )
    assert_has("404.html", "Page not found", "Back home")
    assert_has("CNAME", "blogs.immortalcodes.com")
    assert_has(
        "css/site.css",
        ":focus-visible",
        "prefers-reduced-motion",
        "@media (max-width: 720px)",
        # The backdrop field: ridges, colour zones and film grain.
        "site-backdrop",
        "repeating-linear-gradient",
        "zone-ember",
        "feTurbulence",
        # Dark pools that follow the text, and chrome that fades via masks
        # rather than being separated by borders.
        "--pool",
        "mask-image",
        "backdrop-filter",
        "overflow-x: clip",
        "flex: 1 0 auto",
        "social-button",
    )
    assert_not_has("css/site.css", "theme-toggle", "prefers-color-scheme")
    assert_has("favicon.svg", "ImmortalCodes")
    assert_has("index.xml", "React ≠ Magic", "Handmade Git Commands")
    assert_not_has("index.xml", "<title>Archive</title>", "0001")
    print("smoke_site: all generated site checks passed")


if __name__ == "__main__":
    main()
