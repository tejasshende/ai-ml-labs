# Task List: Login Screen

## Feature: 001 - Login Screen

## Date: 2026-05-08

## Status: Complete

---

## Tasks

### Task 1: Project Setup [P]
- [x] Create `requirements.txt` with Flask dependency
- [x] Create folder structure: `templates/html/`, `static/css/`
- [x] Create `app.py` with Flask app initialization

### Task 2: Create CSS Stylesheet [P]
- [x] Create `static/css/style.css`
- [x] Define body styles (background, font, centering)
- [x] Define login card styles (container, shadow, padding)
- [x] Define input field styles (width, padding, border)
- [x] Define button styles (color, hover, cursor)
- [x] Define error message styles (color, background)
- [x] Define dashboard styles
- [x] Add responsive design rules

### Task 3: Create Login HTML Template [P]
- [x] Create `templates/html/login.html`
- [x] Add HTML5 doctype and structure
- [x] Link CSS stylesheet
- [x] Create centered login card
- [x] Add username input field
- [x] Add password input field
- [x] Add submit button
- [x] Add flash message display area for errors

### Task 4: Create Dashboard HTML Template [P]
- [x] Create `templates/html/dashboard.html`
- [x] Add HTML5 doctype and structure
- [x] Link CSS stylesheet
- [x] Display welcome message with username
- [x] Add logout button/link

### Task 5: Implement Flask Routes
- [x] Implement `GET /` → redirect to `/login`
- [x] Implement `GET /login` → render login form
- [x] Implement `POST /login` → validate credentials
- [x] Handle valid credentials → set session, redirect to dashboard
- [x] Handle invalid credentials → flash error, re-render login
- [x] Implement `GET /dashboard` → render dashboard (auth check)
- [x] Implement `GET /logout` → clear session, redirect to login

### Task 6: Integration & Verification
- [x] Run `app.py` and verify all routes work
- [x] Test valid login with `admin` / `admin`
- [x] Test invalid login shows error message
- [x] Test dashboard redirects when not logged in
- [x] Test logout clears session

---

## Task Dependencies

```
Task 1 (Setup) ──┐
                  ├──→ Task 5 (Routes) ──→ Task 6 (Verify)
Task 2 (CSS) ────┤
Task 3 (Login) ──┤
Task 4 (Dashboard)┘
```

**[P]** = Parallelizable — Tasks 1, 2, 3, 4 can be done simultaneously.
Task 5 depends on Tasks 1-4. Task 6 depends on Task 5.
