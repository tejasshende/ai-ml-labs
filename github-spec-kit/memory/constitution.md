# Project Constitution

## Project Name: Login Screen Application

## Date: 2026-05-08

---

## Article I: Simplicity First

All implementation MUST favor simplicity over complexity. The application shall use minimal dependencies and straightforward patterns. No over-engineering or unnecessary abstractions.

## Article II: Technology Stack

The application MUST use:
- **Python** with Flask as the web framework
- **HTML** for page structure (stored in `templates/html/`)
- **CSS** for styling (stored in `static/css/`)
- **`app.py`** as the single entry point for execution

No JavaScript frameworks, no build tools, no databases.

## Article III: Security Basics

- Credentials default to `admin` / `admin` and are stored in-memory
- Password may be changed at runtime via the forgot-password reset flow
- Form data is submitted via POST method
- No sensitive data is stored persistently
- Flash messages are used for user feedback
- Reset tokens are 6-digit numeric codes with a 5-minute expiry

## Article IV: Separation of Concerns

- HTML templates live in `templates/html/`
- CSS stylesheets live in `static/css/`
- Application logic lives in `app.py`
- Spec documents live in `specs/<NNN>-<feature-name>/`
  - `specs/001-login-feature/` — Login screen
  - `specs/002-forgot-password/` — Forgot password flow

## Article V: Code Quality

- Code MUST be readable and well-commented
- Functions MUST have clear, single responsibilities
- No unused imports or dead code
- Follow PEP 8 style guidelines

## Article VI: User Experience

- The login form MUST provide clear feedback on success/failure
- The interface MUST be clean, centered, and responsive
- Error messages MUST be visible and understandable
- A successful login MUST redirect to a welcome/dashboard page
- The forgot-password flow MUST be discoverable from the login page
- The password-reset flow MUST be intuitive (no more than 2 steps)
- Simulated token delivery MUST clearly indicate it is not a real email

## Article VII: No Over-Engineering

- No database — credentials and tokens are stored in-memory
- No user registration — only login and password reset
- No session persistence beyond runtime
- No tests folder as per project requirements
- No real email delivery — reset tokens are displayed on-screen
- No password strength rules — any non-empty password is accepted
- Maximum simplicity in all decisions
