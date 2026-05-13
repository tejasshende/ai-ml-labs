# Task List: Forgot Password

## Feature: 002 - Forgot Password

## Date: 2026-05-09

## Status: Pending

---

## Tasks

### Task 1: Update Credential Storage in `app.py` [P]
- [ ] Replace hardcoded `VALID_USERNAME` / `VALID_PASSWORD` constants with a mutable `credentials` dict
- [ ] Update the login route to validate against the new `credentials` dict
- [ ] Add `import random` and `from datetime import datetime, timedelta`
- [ ] Add an empty `reset_tokens` dict for token storage

### Task 2: Create Forgot Password HTML Template [P]
- [ ] Create `templates/html/forgot_password.html`
- [ ] Add HTML5 doctype and structure
- [ ] Link existing CSS stylesheet
- [ ] Create centered card with heading "Forgot Password"
- [ ] Add username input field with a "Submit" button
- [ ] Add flash message display area for errors
- [ ] Add conditional block to display the reset token and link to `/reset-password` on success

### Task 3: Create Reset Password HTML Template [P]
- [ ] Create `templates/html/reset_password.html`
- [ ] Add HTML5 doctype and structure
- [ ] Link existing CSS stylesheet
- [ ] Create centered card with heading "Reset Password"
- [ ] Add token input field
- [ ] Add new password input field
- [ ] Add confirm password input field
- [ ] Add submit button
- [ ] Add flash message display area for errors/success

### Task 4: Update Login Template
- [ ] Add a "Forgot Password?" link below the login button in `login.html`
- [ ] Link points to `/forgot-password`
- [ ] Style the link to be subtle but visible

### Task 5: Implement Forgot Password Route
- [ ] Add `GET /forgot-password` route to render the forgot-password form
- [ ] Add `POST /forgot-password` route logic:
  - [ ] Read submitted username from form
  - [ ] Validate username exists in `credentials` dict
  - [ ] If invalid, flash error "Username not found." and re-render
  - [ ] If valid, generate a random 6-digit token (`random.randint(100000, 999999)`)
  - [ ] Store token with expiry (`datetime.now() + timedelta(minutes=5)`) in `reset_tokens`
  - [ ] Pass the token to the template for on-screen display

### Task 6: Implement Reset Password Route
- [ ] Add `GET /reset-password` route to render the reset-password form
- [ ] Add `POST /reset-password` route logic:
  - [ ] Read submitted token, new password, and confirm password from form
  - [ ] Find the matching token in `reset_tokens`
  - [ ] If token not found, flash error "Invalid reset token." and re-render
  - [ ] If token expired, remove it and flash error "Reset token has expired." and re-render
  - [ ] If new password and confirm password don't match, flash error "Passwords do not match." and re-render
  - [ ] If all valid, update the password in `credentials` dict
  - [ ] Remove the used token from `reset_tokens`
  - [ ] Flash success "Password reset successful. Please log in." and redirect to `/login`

### Task 7: Update CSS Styles [P]
- [ ] Add `.info-message` style for displaying the simulated reset token
- [ ] Add `.forgot-link` style for the "Forgot Password?" link on the login page
- [ ] Ensure new pages reuse existing card styles (`.login-card`)

### Task 8: Integration & Verification
- [ ] Run `app.py` and verify all new routes work
- [ ] Test "Forgot Password?" link from the login page
- [ ] Test valid username shows a reset token on screen
- [ ] Test invalid username shows error message
- [ ] Test valid token with matching passwords resets the password
- [ ] Test invalid/expired token shows error message
- [ ] Test mismatched passwords show error message
- [ ] Test login with new password works after reset
- [ ] Test login with old password fails after reset
- [ ] Verify existing login feature still works correctly

---

## Task Dependencies

```
Task 1 (Credentials) ──┐
                        ├──→ Task 5 (Forgot Route) ──┐
Task 2 (Forgot HTML) ──┤                             ├──→ Task 8 (Verify)
                        ├──→ Task 6 (Reset Route) ───┘
Task 3 (Reset HTML) ───┤
Task 4 (Login Link) ───┘
Task 7 (CSS) ──────────────────────────────────────────────→ Task 8 (Verify)
```

**[P]** = Parallelizable — Tasks 1, 2, 3, 7 can be done simultaneously.
Task 4 has no blocking dependency but logically pairs with Task 2.
Tasks 5 and 6 depend on Tasks 1–4. Task 8 depends on all previous tasks.
