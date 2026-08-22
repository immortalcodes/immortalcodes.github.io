+++
title = "Lumina Studio: A Zero Dependency AI Creative Suite"
date = 2026-08-22T20:00:00+05:30

tags = ["ai", "javascript", "sideproject"]
author = "Madhur"
draft = false
description = "A browser based AI image and video studio built on plain HTML, CSS and JavaScript, talking to any OpenRouter model through a tiny Node proxy."
summary = "Notes on building Lumina Studio, a cinematic AI creative suite with zero frontend dependencies, dynamic model discovery, and local asset persistence."
+++

Every generative AI demo I tried felt like the same bare bones playground: a text box, a spinner, one hardcoded model, and a UI that looked like it was designed by the API itself. I wanted something that felt like a proper creative tool, something closer to a darkroom than a form submission. So I built [Lumina Studio](https://github.com/immortalcodes/ai-studio), an AI image and video generator that runs entirely in the browser and talks to OpenRouter for the actual model work.

![Lumina Studio interface](/images/projects/lumina-studio/screenshot-1.png)
*Lumina Studio's cinematic, monochrome interface.*

## What it does

Lumina is a single page app for generating images and videos through any OpenRouter model, image or video generators alike, without hardcoding a single one. It fetches your available models live using your own API key, so the list of what you can use is always accurate and never stale.

A few things it handles out of the box:

- **Image and video modes**, each with their own controls (aspect ratio, quality, resolution, style presets, seeds), so tweaking one never quietly breaks the other
- **Reference images**, to guide composition and style, with an influence slider to control how strongly the reference pulls the result
- **Prompt enhancement**, a one click pass through GPT-4o-mini that turns a lazy three word prompt into something a model can actually work with
- **Cost tracking**, per model pricing in the sidebar and a running total for the session, so you know exactly what a burst of experimentation cost you
- **Generation history**, persisted locally, with an optional asset directory so images and videos survive a page reload instead of evaporating as base64 strings

![Lumina Studio interface](/images/projects/lumina-studio/screenshot-2.png)
*Another look at the interface in action.*

## The engineering choices that mattered

The whole frontend, [index.html](https://github.com/immortalcodes/ai-studio/blob/main/index.html), [css/style.css](https://github.com/immortalcodes/ai-studio/blob/main/css/style.css), and the three JS files, is dependency free. No framework, no build step, no bundler. `state` is a plain object, render functions rebuild the DOM sections that need it, and that's the entire reactivity model. It sounds almost stubborn in 2026, but for a project this size a framework would have been ceremony, not help.

The one place a plain static site can't survive alone is talking to OpenRouter directly: browsers block those cross origin calls. So there's a tiny zero dependency Node server, [server.js](https://github.com/immortalcodes/ai-studio/blob/main/server.js), that does exactly three jobs: serves the static files, proxies `/api/*` calls to OpenRouter with the right CORS headers, and exposes a small `/asset-store/*` API to write generated media to disk. That's it. No ORM, no auth layer, no framework middleware chain, because none of that was actually needed.

Image and video generation share almost nothing under the hood despite looking similar in the UI. Images go through OpenRouter's chat completions endpoint, one request per image, with results pulled out of `message.images[]`. Videos are asynchronous jobs: a `POST` kicks one off, then the client polls every four seconds until it's done, extracting the final URL and cost once it completes. Keeping those two paths cleanly separated in [js/api.js](https://github.com/immortalcodes/ai-studio/blob/main/js/api.js) meant neither one had to compromise on its own generation parameters.

![Lumina Studio interface](/images/projects/lumina-studio/screenshot-3.png)
*A closer look at the generation workflow.*

## Design direction

The visual language is monochrome on purpose: true black background, translucent white glass panels, pill shaped controls, and Instrument Serif italic type for the big moments. No color accents, no gradients pretending to be depth. It's the kind of restraint that's harder to pull off than throwing five gradients at a hero section, closer to the "less but better" school than to a typical AI tool's rainbow of buttons.

![Lumina Studio interface](/images/projects/lumina-studio/screenshot-4.png)
*The monochrome, glassmorphic design system, up close.*

## Try it

The whole thing is [MIT licensed](https://github.com/immortalcodes/ai-studio/blob/main/README.md#-license), so grab an [OpenRouter API key](https://openrouter.ai/keys), clone the repo, and `npm start`. The README and [ARCHITECTURE.md](https://github.com/immortalcodes/ai-studio/blob/main/ARCHITECTURE.md) walk through the rest.

## Resources

- [Lumina Studio on GitHub](https://github.com/immortalcodes/ai-studio)
- [OpenRouter](https://openrouter.ai/)
