# STORIES.md

## Product: prompt‑craft  
**Goal** – Deliver a SaaS platform that lets users create, test, and refine LLM prompts, improving prompt quality and reducing iteration time.

---

## Epics & Story Backlog

| Epic | Story | Acceptance Criteria |
|------|-------|---------------------|
| **Core Prompt Editor** | **E1.1** As a **Prompt Engineer**, I want a **rich text editor** that supports syntax highlighting for prompt templates, so that I can write prompts quickly and with fewer errors. | • Editor shows syntax highlighting for placeholders (`{variable}`) and control flow (`if/else`).<br>• Auto‑completion for known variables.<br>• Undo/redo, copy/paste, and basic formatting (bold, italic). |
| | **E1.2** As a **Prompt Engineer**, I want to **save prompts** to a project workspace, so that I can reuse and version them. | • “Save” button persists prompt to DB.<br>• Prompts are stored with metadata (name, description, tags, last modified).<br>• Version history shows previous edits with timestamps. |
| | **E1.3** As a **Prompt Engineer**, I want to **import/export prompts** in JSON, so that I can share them with teammates or other tools. | • Export button downloads a JSON file with prompt content and metadata.<br>• Import button accepts a valid JSON file and creates a new prompt. |
| **Prompt Testing & Evaluation** | **E2.1** As a **Prompt Engineer**, I want to **run a prompt against a selected LLM** and see the raw output, so that I can evaluate its behavior. | • “Run” button triggers inference via vLLM.<br>• Output is displayed in a collapsible panel.<br>• Execution time and token usage are shown. |
| | **E2.2** As a **Prompt Engineer**, I want to **compare multiple prompt variants** side‑by‑side, so that I can pick the best one. | • UI shows two prompts and their outputs in split view.<br>• Highlight differences in output text.<br>• Option to mark one as “winner” and save. |
| | **E2.3** As a **Prompt Engineer**, I want to **automatically score prompts** using a predefined rubric (e.g., relevance, conciseness, correctness), so that I can quickly gauge quality. | • Score panel shows numeric score and breakdown.<br>• Scores are calculated using a simple heuristic (token count, keyword match).<br>• Scores persist with prompt metadata. |
| **Prompt Refinement & Suggestions** | **E3.1** As a **Prompt Engineer**, I want the system to **suggest improvements** (e.g., re‑phrasing, adding examples), so that I can iterate faster. | • “Suggest” button triggers a lightweight LLM call that returns a revised prompt.<br>• Suggested prompt appears in a new tab with a diff view.<br>• User can accept or reject the suggestion. |
| | **E3.2** As a **Prompt Engineer**, I want to **track changes** between my prompt and the system’s suggestion, so that I understand the modifications. | • Diff view highlights added, removed, and modified lines.<br>• Hover tooltip shows change reason (if provided by LLM). |
| **Collaboration & Permissions** | **E4.1** As a **Team Lead**, I want to **share a prompt workspace** with teammates, so that we can collaborate. | • Share button generates a unique link.<br>• Invitees can view or edit based on role.<br>• Activity log shows who made changes. |
| | **E4.2** As a **Team Lead**, I want to **set role‑based permissions** (viewer, editor, admin), so that access is controlled. | • Permissions UI lists users and roles.<br>• Role changes take effect immediately.<br>• Unauthorized actions are blocked with an error message. |
| **Analytics & Reporting** | **E5.1** As a **Product Manager**, I want to see **prompt performance metrics** (e.g., average score, usage frequency), so that I can prioritize improvements. | • Dashboard displays charts for top prompts, score trends, and usage counts.<br>• Data is refreshed every 5 minutes.<br>• Export to CSV is available. |
| | **E5.2** As a **Product Manager**, I want to **receive alerts** when a prompt’s score drops below a threshold, so that I can investigate. | • Alert triggers when score < 3.5.<br>• Email notification sent to the prompt owner.<br>• Alert appears in the UI notification center. |
| **Integration & Extensibility** | **E6.1** As a **Developer**, I want a **REST API** to programmatically create, update, and run prompts, so that I can integrate with other tools. | • Endpoints: `/prompts`, `/prompts/{id}/run`.<br>• API uses JWT authentication.<br>• Swagger docs available. |
| | **E6.2** As a **Developer**, I want to **plug in new LLM providers** (e.g., OpenAI, Anthropic), so that users can choose the best model. | • Admin UI lists available providers.<br>• Adding a provider requires API key and endpoint.<br>• Prompts can be tagged with provider. |
| **Security & Compliance** | **E7.1** As a **Security Officer**, I want all data in transit and at rest to be encrypted, so that we meet compliance. | • HTTPS enforced everywhere.<br>• Database fields encrypted with AES‑256.<br>• Audit log records all access. |
| | **E7.2** As a **Security Officer**, I want to **audit user actions** (create, edit, delete), so that we can trace responsibility. | • Audit log table records user ID, action, timestamp, and affected prompt ID.<br>• Exportable to CSV. |
| **User Experience Enhancements** | **E8.1** As a **Prompt Engineer**, I want a **dark mode** toggle, so that I can work comfortably in low light. | • Theme switch persists in user settings.<br>• All UI components adapt to dark theme. |
| | **E8.2** As a **Prompt Engineer**, I want **keyboard shortcuts** (e.g., Ctrl+S to save, Ctrl+R to run), so that I can be more efficient. | • Shortcuts documented in help modal.<br>• Tested across Chrome, Firefox, Safari. |

---

## MVP Release Order

1. **Core Prompt Editor** (E1.1–E1.3)  
2. **Prompt Testing & Evaluation** (E2.1–E2.3)  
3. **Prompt Refinement & Suggestions** (E3.1–E3.2)  
4. **Collaboration & Permissions** (E4.1–E4.2)  
5. **Analytics & Reporting** (E5.1–E5.2)  
6. **Integration & Extensibility** (E6.1–E6.2)  
7. **Security & Compliance** (E7.1–E7.2)  
8. **User Experience Enhancements** (E8.1–E8.2)

---

### Notes

* All stories assume the underlying LLM inference engine is vLLM, as per the company’s verified framework list.  
* Data sets such as `auto`, `instr-resp`, `messages`, and `system-user-assistant` can be leveraged for training internal prompt‑scoring models.  
* The platform must not duplicate existing portfolio items; focus remains on prompt crafting tooling only.
