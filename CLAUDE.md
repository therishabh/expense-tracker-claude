# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Spendly** is a personal expense-tracking web application built with Python and Flask. Users can register, log in, and track their daily expenses by category. The project is structured as a teaching exercise — some routes are fully implemented while others are left as stubs for students to complete.

---

## Development Setup

The project uses a Python virtualenv. Always activate it before running any command:

```bash
source venv/bin/activate
```

### Run the development server

```bash
python app.py
```

The server starts at **http://127.0.0.1:5001** with Flask's debug mode and auto-reloader enabled.

### Run the test suite

```bash
pytest
```

### Run a single test file

```bash
pytest tests/test_auth.py
```

Dependencies are listed in `requirements.txt` (Flask, Werkzeug, pytest, pytest-flask). Install with:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
expense-tracker/
├── app.py                  # All Flask routes and app entry point
├── database/
│   ├── db.py               # SQLite database setup and connection
│   └── __init__.py         # Exposes db utilities to the rest of the app
├── templates/
│   ├── base.html           # Shared layout: navbar, footer, asset links
│   ├── landing.html        # Public landing / marketing page
│   ├── login.html          # Login form
│   ├── register.html       # Registration form
│   ├── privacy.html        # Privacy Policy page
│   └── terms.html          # Terms & Conditions page
└── static/
    ├── css/style.css       # All styles — single stylesheet
    └── js/main.js          # All client-side JavaScript
```

---

## Tech Constraints

- **Python 3.9** — the virtualenv is pinned to Python 3.9. Do not use syntax or stdlib features introduced in 3.10+ (e.g. structural pattern matching, `match`/`case`).
- **Flask 3.1.3** — no other backend framework. Do not introduce FastAPI, Django, or any WSGI/ASGI alternative.
- **SQLite only** — the database layer uses SQLite via Python's built-in `sqlite3` module. No PostgreSQL, MySQL, or ORM (e.g. SQLAlchemy) unless explicitly added to `requirements.txt`.
- **No CSS framework** — all styling is hand-written in `static/css/style.css`. Do not add Bootstrap, Tailwind, or any third-party CSS library.
- **No JavaScript framework** — all client-side code is vanilla JS in `static/js/main.js`. Do not introduce React, Vue, Alpine.js, or jQuery.
- **Single-page stylesheet and script** — keep all styles in `style.css` and all JS in `main.js`. Do not create additional CSS or JS files unless the project structure is explicitly reorganised.
- **Dev server port is 5001** — not Flask's default 5000, to avoid conflicts with macOS AirPlay Receiver.

---

## Architecture

### Routing (`app.py`)

Every route is defined in `app.py`. The file is the single entry point for the application — there are no blueprints or separate route files.

**Implemented routes:**

| Route | Function | Template |
|---|---|---|
| `/` | `landing` | `landing.html` |
| `/register` | `register` | `register.html` |
| `/login` | `login` | `login.html` |
| `/privacy-policy` | `privacy` | `privacy.html` |
| `/terms-and-conditions` | `terms` | `terms.html` |

**Stub routes** (return plain strings — to be implemented by students):

| Route | Purpose |
|---|---|
| `/logout` | End user session |
| `/profile` | User profile page |
| `/expenses/add` | Add a new expense |
| `/expenses/<id>/edit` | Edit an existing expense |
| `/expenses/<id>/delete` | Delete an expense |

### Templates

All templates extend `templates/base.html` using Jinja2's `{% extends %}` / `{% block %}` system. `base.html` provides:
- **Navbar** — brand logo, Sign in and Get started links
- **Footer** — tagline, links to Privacy Policy and Terms & Conditions
- Font imports (DM Serif Display + DM Sans from Google Fonts)
- CSS and JS asset tags

When adding a new page, create a template that starts with `{% extends "base.html" %}` and fills in `{% block title %}` and `{% block content %}`.

### Database (`database/`)

`database/db.py` contains the SQLite setup. It is not yet connected to any route — the database layer is ready to be wired up when students implement authentication and expense routes.

---

## Styling

All styles live in `static/css/style.css` as a single file. Styles are organised into clearly commented sections.

### Design tokens (CSS variables)

Defined in `:root` at the top of `style.css`. Always use these variables for colours, radii, and fonts — never hardcode raw values in new styles.

| Variable | Value | Usage |
|---|---|---|
| `--ink` | `#0f0f0f` | Primary text, dark backgrounds |
| `--ink-soft` | `#2d2d2d` | Secondary text |
| `--ink-muted` | `#6b6b6b` | Placeholder / subdued text |
| `--ink-faint` | `#a0a0a0` | Very subtle text (e.g. footer copy) |
| `--paper` | `#f7f6f3` | Page background |
| `--paper-warm` | `#f0ede6` | Section background (e.g. features) |
| `--paper-card` | `#ffffff` | Card / modal backgrounds |
| `--accent` | `#1a472a` | Primary accent — dark green |
| `--accent-light` | `#e8f0eb` | Light green tint (badges, hover states) |
| `--accent-2` | `#c17f24` | Secondary accent — amber |
| `--border` | `#e4e1da` | Default border colour |
| `--font-display` | DM Serif Display | Headings, large numbers |
| `--font-body` | DM Sans | All body text and UI |

### Key style sections

- **Navbar** — sticky top bar, 60px height
- **Hero** — centered layout with a browser-style mock dashboard visual
- **Mock browser** — the dashboard preview on the landing page (stat cards + category bars)
- **Features** — three-column card grid on a warm background
- **CTA section** — centred call-to-action below features
- **Demo modal** — full-screen overlay with YouTube iframe embed
- **Auth pages** — login and register forms (`.auth-section`, `.auth-card`)
- **Legal pages** — Privacy Policy and Terms layout (`.legal-section`, `.legal-body`)
- **Footer** — dark background with brand, tagline, and legal links

---

## JavaScript (`static/js/main.js`)

### Demo video modal

The "See how it works" button on the landing page (`#open-demo-modal`) opens a modal overlay (`#demo-modal`) containing a YouTube iframe.

**How it works:**
- The iframe stores the YouTube embed URL in `data-src`, with `src` left empty on page load (so the video does not preload).
- On open: `data-src` is copied into `src`, starting the video.
- On close: `src` is cleared, stopping playback.
- The modal also closes when clicking the backdrop or pressing `Escape`.

**To update the video URL**, change the `data-src` attribute on the `#demo-iframe` element in `templates/landing.html`:

```html
data-src="https://www.youtube.com/embed/YOUR_VIDEO_ID?enablejsapi=1&rel=0"
```
