 # Task
Generate `user-stories.md` for the `prompt-craft` product.

## Epic: User Management

### As a Site Administrator, I want to create, edit, and delete user accounts, so that I can manage the platform's user base.
- Acceptance Criteria:
  1. Ability to create a new user account with a unique email and password.
  2. Ability to edit a user's account information, including name, email, and password.
  3. Ability to delete a user account permanently, with confirmation.
  4. Ability to view a list of all users and their account information.
  5. Ability to assign roles (e.g., Basic, Pro, Admin) to users.
  6. Ability to set permissions for each role (e.g., prompt creation, testing, refinement, etc.).
  7. Ability to reset a user's password if they forget it.
- Complexity: M

### As a User, I want to log in and out of the platform, so that I can securely access my account and data.
- Acceptance Criteria:
  1. Ability to log in with a valid email and password.
  2. Ability to log out securely.
  3. Ability to recover my account if I forget my password.
  4. Implementation of secure password storage and hashing.
  5. Implementation of rate limiting to prevent brute force attacks.
- Complexity: M

## Epic: Prompt Management

### As a User, I want to create, edit, and delete prompts, so that I can manage my LLM prompt library.
- Acceptance Criteria:
  1. Ability to create a new prompt with a unique name and description.
  2. Ability to edit a prompt's name, description, and content.
  3. Ability to delete a prompt permanently, with confirmation.
  4. Ability to view a list of all prompts and their details.
  5. Ability to organize prompts into categories or folders.
  6. Ability to search for prompts by name, description, or category.
  7. Ability to share prompts with other users.
- Complexity: M

### As a User, I want to test and refine my prompts, so that I can improve their effectiveness and efficiency.
- Acceptance Criteria:
  1. Ability to test a prompt by running it through the LLM model and evaluating the output.
  2. Ability to refine a prompt based on the test results, including adjusting the prompt's content, structure, or parameters.
  3. Ability to save multiple versions of a prompt for comparison and future reference.
  4. Implementation of a scoring system to evaluate the effectiveness of a prompt.
  5. Implementation of a feedback mechanism to help users understand why a prompt is effective or ineffective.
  6. Ability to collaborate with other users on the testing and refinement of prompts.
- Complexity: L

## Epic: Collaboration

### As a User, I want to collaborate with other users on prompt creation, testing, and refinement, so that we can share knowledge and improve the platform collectively.
- Acceptance Criteria:
  1. Ability to invite other users to collaborate on a prompt.
  2. Ability to view the activity and contributions of collaborators on a prompt.
  3. Ability to communicate with collaborators through an integrated messaging system.
  4. Ability to assign tasks or responsibilities to collaborators for prompt development.
  5. Implementation of a version control system to track changes to prompts and collaborator contributions.
- Complexity: L

### As a User, I want to receive notifications about important platform updates, new prompts, and collaborator activity, so that I can stay informed and engaged.
- Acceptance Criteria:
  1. Ability to customize notification preferences (e.g., email, in-app, push notifications).
  2. Ability to receive notifications about new prompts, updates to existing prompts, and collaborator activity.
  3. Ability to snooze or mute notifications temporarily.
  4. Implementation of a system to prioritize notifications based on their importance.
- Complexity: M