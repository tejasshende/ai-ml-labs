# Feature Specification: Forgot Password

## Feature Number: 002

## Feature Name: Forgot Password

## Date: 2026-05-09

## Status: Pending

---

## 1. Overview

Add a "Forgot Password?" flow that allows a user to reset their password by verifying their username. Since there is no database or email service, the reset will use a simple simulated flow: the user enters their username, and if it matches the known account (`admin`), the app displays a temporary reset token on-screen and presents a form to set a new password. The new password is stored in-memory for the remainder of the application runtime.

## 2. User Stories

### US-004: Initiate Password Reset
**As a** user who has forgotten their password,
**I want to** click a "Forgot Password?" link on the login page,
**So that** I can begin the password recovery process.

**Acceptance Criteria:**
- [ ] A "Forgot Password?" link is visible on the login page below the login button
- [ ] Clicking the link navigates to `/forgot-password`
- [ ] The forgot-password page displays a form asking for the username

### US-005: Verify Username & Get Reset Token
**As a** user on the forgot-password page,
**I want to** enter my username and receive a reset token,
**So that** I can prove I own the account and proceed to set a new password.

**Acceptance Criteria:**
- [ ] Submitting a valid username (`admin`) generates a 6-digit numeric reset token
- [ ] The token is displayed on-screen (simulating an email)
- [ ] Submitting an unknown username shows an error: "Username not found."
- [ ] The token is stored server-side in memory with a short expiry (5 minutes)

### US-006: Reset Password
**As a** user with a valid reset token,
**I want to** enter my token and a new password,
**So that** I can regain access to my account.

**Acceptance Criteria:**
- [ ] A reset form is displayed at `/reset-password` with fields for token, new password, and confirm password
- [ ] Submitting a valid token with matching passwords updates the in-memory password
- [ ] Submitting an invalid or expired token shows an error message
- [ ] Mismatched passwords show an error message
- [ ] On success, user is redirected to `/login` with a flash message: "Password reset successful. Please log in."

## 3. Functional Requirements

| ID     | Requirement                                                 | Priority |
|--------|-------------------------------------------------------------|----------|
| FR-008 | Display "Forgot Password?" link on the login page           | High     |
| FR-009 | Provide a forgot-password page with username input          | High     |
| FR-010 | Validate username against known accounts                    | High     |
| FR-011 | Generate and display a 6-digit reset token on valid request | High     |
| FR-012 | Store token in-memory with 5-minute expiry                  | High     |
| FR-013 | Provide a reset-password page with token and password input | High     |
| FR-014 | Validate token, update in-memory password on success        | High     |
| FR-015 | Redirect to login page with success flash message           | Medium   |
| FR-016 | Show clear error messages for all failure scenarios         | Medium   |

## 4. Non-Functional Requirements

- The forgot-password and reset-password pages should share the same visual style as the login page
- The flow should be intuitive — no more than 2 steps to reset
- Token display must clearly indicate it is a simulated delivery (not a real email)
- Pages should load in under 1 second

## 5. Out of Scope

- Actual email delivery
- SMS or multi-factor reset
- Database storage of tokens or passwords
- Rate limiting or brute-force protection
- Password strength validation rules
- Account lockout on repeated failed resets
