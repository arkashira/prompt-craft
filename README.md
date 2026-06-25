# Prompt Craft

Prompt Craft is a web editor for authoring and validating prompts. It supports Markdown-style prompt blocks with syntax highlighting for placeholders and linting for common errors.

## Features

* Syntax highlighting for placeholders
* Linting for common errors (e.g., missing placeholders, duplicate keys)
* Autosaving drafts to local storage
* Syncing to repository on demand

## Usage

1. Create a new prompt using the `Prompt` class.
2. Use the `PromptEditor` class to create, autosave, and lint prompts.
3. Use the `syntax_highlighting` function to highlight placeholders in the prompt text.
