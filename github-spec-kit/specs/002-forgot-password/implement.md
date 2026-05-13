# Implementation Notes: Forgot Password

## Feature: 002 - Forgot Password

## Date: 2026-05-09

## Status: Pending

---

## Implementation Summary

This document will be updated once all tasks from `tasks.md` have been executed.

## Files to Create

| File                                | Purpose                             |
|-------------------------------------|-------------------------------------|
| `templates/html/forgot_password.html` | Forgot password form (username input) |
| `templates/html/reset_password.html`  | Reset password form (token + new password) |

## Files to Modify

| File                            | Change Description                                        |
|---------------------------------|-----------------------------------------------------------|
| `app.py`                        | Add forgot-password & reset-password routes; use mutable credentials |
| `templates/html/login.html`     | Add "Forgot Password?" link below the login button        |
| `static/css/style.css`          | Add styles for info-message and forgot-password link      |

## How to Run

```bash
# 1. Install dependencies (unchanged)
pip install -r requirements.txt

# 2. Run the application
python app.py

# 3. Open browser to http://127.0.0.1:1234
```

## Credentials

| Username | Password (default) |
|----------|-------------------|
| `admin`  | `admin`           |

> **Note:** After a successful password reset, the password changes to whatever was set in the reset form. The change persists only for the current app session — restarting the app resets it back to `admin`.

## Verification Checklist

- [ ] Login page displays "Forgot Password?" link
- [ ] `/forgot-password` renders a username input form
- [ ] Valid username (`admin`) generates and displays a 6-digit token
- [ ] Invalid username shows "Username not found." error
- [ ] `/reset-password` renders token, new password, and confirm password fields
- [ ] Valid token with matching passwords updates the in-memory password
- [ ] Invalid token shows "Invalid reset token." error
- [ ] Expired token shows "Reset token has expired." error
- [ ] Mismatched passwords show "Passwords do not match." error
- [ ] After reset, user can log in with the new password
- [ ] After reset, old password no longer works
- [ ] Existing login/dashboard/logout features remain fully functional

## Key Design Decisions

1. **Simulated token delivery**: Token is shown directly on-screen since there is no email service. A clear message indicates this is a simulation.
2. **In-memory storage**: Both the mutable password and reset tokens live in memory. Restarting the app resets everything.
3. **6-digit numeric token**: Simple and user-friendly; generated using `random.randint(100000, 999999)`.
4. **5-minute expiry**: Tokens expire after 5 minutes to simulate real-world security practices.
5. **Single token per user**: Requesting a new token overwrites the previous one.
6. **No new dependencies**: Everything uses Python standard library (`random`, `datetime`).
