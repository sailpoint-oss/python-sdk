# Create Pull Request

## Overview

Create a pull request using the GitHub CLI (`gh`). The PR uses the **current branch** as the head and **main** as the base. The PR title is whatever the user types after the slash command.

## What to do

1. **Title:** Use the text the user provided after the command as the PR title (e.g. `/create-pr Add streaming pagination` → title is "Add streaming pagination"). If the user did not provide any text after the command, ask them for a PR title.
2. **Push if needed:** From the repository root, if the current branch does not have an upstream on origin yet, push it first so `gh pr create` can open a PR:
   - Check: `git rev-parse --abbrev-ref @{u} 2>/dev/null` or equivalent (e.g. if `git status` says "no upstream branch").
   - If the branch is not yet pushed: run `git push -u origin $(git branch --show-current)`.
   - If the push fails (e.g. uncommitted changes, auth), report the error and stop; otherwise continue.
3. **Create the PR:** From the repository root, run:
   - **Command:** `gh pr create --base main --title "<title>" --body "<body>"`
   - Replace `<title>` with the title from step 1. For `<body>`, use a short description (e.g. same as title or "See commits for details"). Quote both so special characters or spaces are handled correctly. (Non-interactive `gh` requires `--body`.)
4. Report the outcome: the PR URL if successful, or any error from `git push` or `gh` (e.g. not logged in, uncommitted changes, conflicts).

## Notes

- Ensure you are in the workspace (repo) root when running `git` and `gh`.
- The current branch is used automatically as the head by `gh pr create`.
- If the user asks for a custom body/description, use that for `--body "..."` instead of the default.
