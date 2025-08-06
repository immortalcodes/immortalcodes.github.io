+++
title = "Handmade Git Commands"
date = 2025-08-06T12:00:00+01:00

tags = ["git"]
author = "Madhur"
showToc = true
TocOpen = false
draft = false
hidemeta = false
comments = false
description = "Writing your custom git commands"
canonicalURL = "https://canonical.url/to/page"
disableHLJS = true # to disable highlightjs
disableShare = false
hideSummary = false
searchHidden = false
ShowReadingTime = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowWordCount = true
ShowRssButtonInSectionTermList = true
UseHugoToc = true

[cover]
image = "/images/custom-git-commands.png"
alt = "Custom git commands"
caption = "cover"
relative = false # when using page bundles set this to true
hidden = true # only hide on current single page

[editPost]
URL = "https://github.com/immortalcodes/immortalcodes.github.io/issues/new"
Text = "Suggest Changes" # edit text
appendFilePath = false # to append file path to Edit link
+++

![Custom git commands](/images/custom-git-commands.png)

## Handmake your Git commands at home

Long story short, you can extend Git's functionality by creating your own custom commands! It's simpler than you think. Here are 3 steps:

- Create an **executable binary** to do the things you want your git command to do. This could be a shell script, or a program in any language.
- Name it `git-<command-name>`. For example, if you want a command called `git cleanup-branches`, you'd name your script `git-cleanup-branches`.
- Put it in your **$PATH** and make it executable (`chmod +x /path/to/your/script`).

Now you can use your new Git power via:

`git <command-name> [arg-1] [arg-2]`

Pretty neat, huh? 😎

---

## Some tips:

- `/usr/local/bin/` is often a good place to store your personal binaries, as it's usually in your system's default PATH.
- To update $PATH you can edit shell config files. (like `~/.bashrc` for Bash or `~/.zshrc` for Zsh).  
Just add a line like this, replacing `/your-directory/my-git-custom-commands` with the actual path to where you store your scripts:  
`PATH=$PATH:/your-directory/my-git-custom-commands`  
Don't forget to source your shell's config file (e.g., `source ~/.bashrc` or `source ~/.zshrc`) or open a new terminal for the changes to take effect.

---

## Walking through an example:

Let's look at a real-world example of a handy custom Git command: **`git-ignore-local`**.

This tool addresses a common annoyance: sometimes you want to ignore files in your local Git repository without adding them to the project's `.gitignore` file. This is perfect for machine-specific configurations, temporary debug logs, or IDE-generated files that clutter your workspace but shouldn't be shared.

The `git-ignore-local` tool, as described in its README, cleverly uses Git's `.git/info/exclude` file to achieve this. Here's a quick rundown of how it works and why it's so useful:

- **No more `.gitignore` conflicts for local ignores:** You can keep your personal ignore rules separate from the team's shared rules.
- **Easy to add and remove:** Just use `git ignore-local <file_or_pattern>` to add an ignore rule and `git ignore-local --restore <file_or_pattern>` to remove one.
- **Keeps your repository clean:** Avoid committing files that are only relevant to your local development environment.

Imagine you're working on a project and your IDE creates a `.idea/` folder. You don't want to commit this to the main repository, but constantly seeing untracked files is distracting. With `git ignore-local .idea/`, problem solved! ✨

The `git-ignore-local` project provides clear instructions on how to install it, either by downloading a pre-built binary or building it yourself. Once installed (typically by copying the executable to `/usr/local/bin/` and making it executable), you can use it just like any other Git command:

**Ignoring files:**

`git ignore-local .env logs/debug.log`

**Restoring (unignoring) files:**

`git ignore-local --restore logs/debug.log`


This `git-ignore-local` example perfectly illustrates the power of creating your own Git commands. It solves a specific problem in a clean and efficient way, integrating seamlessly with Git's existing workflow.

***So, what Git annoyances do _you_ encounter regularly? Maybe it's time to handmake your own Git command to conquer them! Get creative and happy scripting! 🚀***
