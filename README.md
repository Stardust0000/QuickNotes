# QuickNotes

A beautifully designed **Personal Notes Web App** built using **Django**, with **User Authentication** and **Dark/Light Themes**.  
Create, edit, complete, and delete notes — all stored securely per user.

---

## 🌟 Features

- ✅ User Signup & Login (Django Auth)
- ✅ Add New Notes
- ✅ Edit Existing Notes
- ✅ Mark Notes as Done / Undo
- ✅ Delete Notes
- ✅ Notes filtered by logged-in user only
- ✅ Dark / Light Theme toggle (saved in Local Storage)
- ✅ Form validation (no empty or junk notes)
- ✅ Responsive UI with hover and blur effects

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Auth:** Django Authentication System
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub

---

## 🚀 Installation & Setup

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

## 🔐 Authentication Behavior

### ✔ Logged-in users can:
- Add notes
- Edit notes
- Mark notes as Done / Undo
- Delete notes

### 🚫 Non-logged-in users:
- Can see the home page layout
- Cannot add or modify notes (they are redirected to Login/Signup)

All notes are linked to the logged-in user using a **ForeignKey** relationship to Django's built-in User model.

---

## 📁 Project Structure (Simplified)
QuickNotes
├─ 📄 manage.py
├─ 📄 requirements.txt
├─ 📄 .gitignore
├─ 🗄 db.sqlite3
│
├─ 📁 notes
│  ├─ 📁 migrations
│  ├─ 📁 static
│  │  ├─ 🎨 style.css
│  │  └─ 📁 js
│  │     └─ ✨ theme.js
│  ├─ 📁 templates
│  │  ├─ 🏠 home.html
│  │  ├─ 🔐 login.html
│  │  └─ 📝 signup.html
│  ├─ 🧠 models.py
│  ├─ 🧩 forms.py
│  ├─ 🛠 views.py
│  └─ 🌐 urls.py
│
└─ 📁 quicknotes
   ├─ ⚙️ settings.py
   ├─ 🌐 urls.py
   ├─ 🚀 asgi.py
   └─ 🚀 wsgi.py


---

## ✨ Future Improvements

- ⏰ Add reminders and due dates
- 🏷 Add tags/categories to group notes
- 🔍 Add search and filters

---

## 💝 Author

Created with care by **CrimsonShadow**  
GitHub: [Stardust0000](https://github.com/Stardust0000) ✨

This project was built to practice:

- Django basics (views, models, forms)
- Authentication & authorization
- Frontend styling, themes, and animations
- Clean UX and validation flows


