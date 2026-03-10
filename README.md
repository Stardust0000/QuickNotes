# QuickNotes

A beautifully designed **Personal Notes Web App** built using **Django**, with **User Authentication** and **Dark/Light Themes**.  
Create, edit, complete, and delete notes — all stored securely per user.

---

## Features

- User Signup & Login using Django Authentication
- Create new notes
- Edit existing notes
- Mark notes as completed / undo completion
- Delete notes
- Notes filtered per authenticated user
- Dark / Light theme toggle (stored in Local Storage)
- Form validation to prevent empty or invalid notes
- Responsive UI with interactive hover effects

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Auth:** Django Authentication System
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub

---

##  Installation & Setup

```bash
# Clone this repository
git clone https://github.com/Stardust0000/QuickNotes.git
cd QuickNotes

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver

# Then open your browser at:
http://127.0.0.1:8000/
```
---

## Authentication Behavior

### Logged-in users can:
- Add notes
- Edit notes
- Mark notes as Done / Undo
- Delete notes

### Non-logged-in users:
- Can view the home page layout
- Are redirected to login/signup when attempting note actions

All notes are linked to the logged-in user using a **ForeignKey** relationship to Django's built-in User model.

---

## Project Structure (Simplified)
```bash
QuickNotes
├─  manage.py
├─  requirements.txt
├─  .gitignore
├─  db.sqlite3
│
├─  notes
│  ├─  migrations
│  ├─  static
│  │  ├─ style.css
│  │  └─  js
│  │     └─ theme.js
│  ├─  templates
│  │  ├─ home.html
│  │  ├─ login.html
│  │  └─ signup.html
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  └─ urls.py
│
└─  quicknotes
   ├─ settings.py
   ├─ urls.py
   ├─ asgi.py
   └─ wsgi.py
```

---

## Future Improvements

- Add reminders and due dates
- Add tags and categories for notes
- Implement search functionality
- Add pagination for large note lists
- Deploy application using Docker and cloud hosting

---

## Author

Created with care by **CrimsonShadow**  
GitHub: [Stardust0000](https://github.com/Stardust0000)

This project was built to practice:

- Django basics (views, models, forms)
- Authentication & authorization
- Frontend styling, themes, and animations
- Clean UX and validation flows


