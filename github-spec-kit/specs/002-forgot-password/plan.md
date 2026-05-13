# Implementation Plan: Forgot Password

## Feature: 002 - Forgot Password

## Date: 2026-05-09

## Status: Pending

---

## 1. Technology Choices

| Component        | Technology       | Rationale                                         |
|------------------|------------------|---------------------------------------------------|
| Backend          | Python + Flask   | Existing stack, no new dependencies needed        |
| Token Generation | `random` module  | Python stdlib, no extra dependency                |
| Token Storage    | In-memory dict   | Keeps it simple, no database needed               |
| Expiry Tracking  | `datetime`       | Python stdlib, compare timestamps for expiry      |
| Templating       | Jinja2 (Flask)   | Already in use for login and dashboard pages      |
| Styling          | Vanilla CSS      | Reuse existing `style.css` with minimal additions |

## 2. Updated Project Structure

```
github-spec-kit/
├── memory/
│   └── constitution.md              # Updated with forgot-password context
├── specs/
│   ├── 001-login-feature/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   └── implement.md
│   └── 002-forgot-password/
│       ├── spec.md                  # Feature specification (this feature)
│       ├── plan.md                  # This implementation plan
│       ├── tasks.md                 # Task breakdown
│       └── implement.md            # Implementation instructions
├── templates/
│   └── html/
│       ├── login.html               # Modified — add "Forgot Password?" link
│       ├── dashboard.html           # Unchanged
│       ├── forgot_password.html     # NEW — username input for reset
│       └── reset_password.html      # NEW — token + new password form
├── static/
│   └── css/
│       └── style.css                # Minor additions for new pages
├── app.py                           # Modified — add new routes & logic
└── requirements.txt                 # Unchanged
```

## 3. Architecture

### 3.1 New Routes

| Route              | Method    | Description                                      |
|--------------------|-----------|--------------------------------------------------|
| `/forgot-password` | GET, POST | Display forgot form / validate username & issue token |
| `/reset-password`  | GET, POST | Display reset form / validate token & update password |

### 3.2 Forgot-Password Flow

```
User clicks "Forgot Password?" on /login
    ↓
GET /forgot-password → Render username form
    ↓
User enters username → POST /forgot-password
    ↓
Validate username against known accounts
    ↓
  ┌─── Valid ──→ Generate 6-digit token → Store in memory with expiry
  │              → Display token on screen → Show link to /reset-password
  └─── Invalid → Flash error "Username not found." → Re-render form
```

### 3.3 Reset-Password Flow

```
User visits /reset-password (via link or manually)
    ↓
GET /reset-password → Render token + new password + confirm password form
    ↓
User submits form → POST /reset-password
    ↓
Validate token → Check expiry → Compare passwords
    ↓
  ┌─── All valid ──→ Update in-memory password → Redirect /login with success flash
  ├─── Token invalid/expired → Flash error → Re-render form
  └─── Passwords mismatch → Flash error → Re-render form
```

### 3.4 Token Storage (In-Memory)

```python
# Simple dict structure — cleared on app restart
reset_tokens = {
    'admin': {
        'token': '482917',
        'expires': datetime(2026, 5, 9, 14, 5, 0)
    }
}
```

- Only one active token per username at a time
- Tokens expire after 5 minutes
- Token is a random 6-digit number (100000–999999)

## 4. File Responsibilities

### `app.py` (Modified)
- Add `import random, datetime` at the top
- Replace hardcoded `VALID_PASSWORD` with a mutable variable (e.g., `credentials` dict)
- Add `reset_tokens` dict for token storage
- Add `GET/POST /forgot-password` route
- Add `GET/POST /reset-password` route
- Update login validation to use the mutable credentials dict

### `templates/html/login.html` (Modified)
- Add a "Forgot Password?" link below the login button pointing to `/forgot-password`

### `templates/html/forgot_password.html` (New)
- HTML5 page matching existing style
- A centered card with a heading "Forgot Password"
- Username input field with a "Submit" button
- Flash message area for errors
- On success: display the generated token and link to `/reset-password`

### `templates/html/reset_password.html` (New)
- HTML5 page matching existing style
- A centered card with a heading "Reset Password"
- Token input field
- New password input field
- Confirm password input field
- Submit button
- Flash message area for errors and success

### `static/css/style.css` (Modified)
- Add styles for `.info-message` (to display the simulated token)
- Add styles for the "Forgot Password?" link on the login page
- Reuse existing `.login-card` styles for new pages (class can be shared)

## 5. Dependencies

No new external dependencies. All functionality uses Python standard library:
- `random.randint()` for token generation
- `datetime.datetime` and `datetime.timedelta` for expiry

## 6. Pre-Implementation Gates

### Simplicity Gate
- [x] No new dependencies added
- [x] No database or external service
- [x] Reuses existing patterns and styles
- [x] In-memory only — resets on app restart

### Anti-Abstraction Gate
- [x] No new models or classes — just a dict for tokens
- [x] No email service simulation beyond displaying the token
- [x] Minimal modifications to existing files
- [x] Same architectural patterns as Feature 001
