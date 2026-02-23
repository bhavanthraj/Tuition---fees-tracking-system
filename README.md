# 🎓 Tuition Fee Tracking System

A full-stack tuition fee management system with a Flask backend, Supabase database, and modern dark-themed frontend.

---

## 📦 Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Frontend   | HTML + CSS + JavaScript  |
| Backend    | Python Flask (REST API)  |
| Database   | Supabase (PostgreSQL)    |
| Auth       | Custom login with bcrypt |
| Downloads  | CSV & PDF (ReportLab)    |

---

## 🚀 Getting Started

### 1. Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Open the **SQL Editor** in your Supabase dashboard
3. Copy and paste the contents of `schema.sql` and run it
4. Go to **Settings → API** and copy your:
   - **Project URL** (e.g., `https://xxxxx.supabase.co`)
   - **anon/public key**

### 2. Configure Environment Variables

Edit the `.env` file in the project root:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here
FLASK_SECRET_KEY=any-random-secret-string
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The app will be available at: **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
tuition-fee-tracker/
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── schema.sql              # Supabase database schema
├── .env                    # Environment variables
├── .env.example            # Environment template
├── routes/
│   ├── __init__.py
│   ├── auth.py             # Login & registration routes
│   ├── students.py         # Student CRUD routes
│   ├── courses.py          # Course management routes
│   ├── fees.py             # Fee management routes
│   ├── payments.py         # Payment recording routes
│   ├── dashboard.py        # Dashboard analytics routes
│   └── downloads.py        # CSV & PDF download routes
└── frontend/
    ├── login.html           # Login page
    ├── admin-dashboard.html # Admin dashboard
    ├── student-dashboard.html # Student dashboard
    ├── students.html        # Students list & management
    ├── add-student.html     # Add new student form
    ├── courses.html         # Courses management
    ├── fees.html            # Fees & payment recording
    ├── payment-history.html # All payment history
    ├── receipt.html         # Payment receipt
    ├── css/
    │   └── style.css        # Design system & styles
    └── js/
        ├── api.js           # API client library
        └── app.js           # Core app logic & utilities
```

---

## 🛠️ API Endpoints

### Authentication
| Method | Endpoint          | Description         |
|--------|-------------------|---------------------|
| POST   | `/admin/login`    | Admin login         |
| POST   | `/student/login`  | Student login       |
| POST   | `/admin/register` | Register new admin  |

### Students
| Method | Endpoint                      | Description             |
|--------|-------------------------------|-------------------------|
| POST   | `/students/add`               | Add new student         |
| GET    | `/students`                   | Get all students        |
| GET    | `/students/<id>`              | Get student by ID       |
| GET    | `/students/search/<unique_id>`| Search by student ID    |
| PUT    | `/students/update/<id>`       | Update student          |
| DELETE | `/students/delete/<id>`       | Delete student          |

### Courses
| Method | Endpoint                  | Description         |
|--------|---------------------------|---------------------|
| POST   | `/courses/add`            | Add new course      |
| GET    | `/courses`                | Get all courses     |
| PUT    | `/courses/update/<id>`    | Update course       |
| DELETE | `/courses/delete/<id>`    | Delete course       |

### Fees
| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/fees/assign`            | Assign/update student fee|
| GET    | `/fees/student/<id>`      | Get student fee status   |
| GET    | `/fees/pending`           | Get all pending fees     |
| GET    | `/fees/paid`              | Get all fully paid       |

### Payments
| Method | Endpoint                     | Description             |
|--------|------------------------------|-------------------------|
| POST   | `/payments/add`              | Record a payment        |
| GET    | `/payments/student/<id>`     | Get student payments    |
| GET    | `/payments`                  | Get all payments        |

### Dashboard
| Method | Endpoint                          | Description          |
|--------|-----------------------------------|----------------------|
| GET    | `/dashboard/admin-summary`        | Admin analytics      |
| GET    | `/dashboard/student-summary/<id>` | Student summary      |

### Downloads
| Method | Endpoint                               | Description           |
|--------|----------------------------------------|-----------------------|
| GET    | `/download/payment-history/<id>`       | Download CSV          |
| GET    | `/download/payment-history-pdf/<id>`   | Download PDF          |
| GET    | `/download/all-students-report`        | All students CSV      |

---

## 🔐 First-Time Setup

1. Open the login page at `http://127.0.0.1:5000`
2. Click **"First time? Register as Admin"**
3. Create your admin account
4. Login and start adding courses, then students

---

## 🎨 Features

- ✅ Dark glassmorphism UI with smooth animations
- ✅ Admin & Student portals
- ✅ Full student CRUD management
- ✅ Course management
- ✅ Fee assignment & tracking
- ✅ Payment recording with multiple methods
- ✅ Dashboard with analytics & charts
- ✅ PDF & CSV report downloads
- ✅ Responsive design (mobile-friendly)
- ✅ Toast notifications
- ✅ Search & filter functionality
- ✅ Password hashing with bcrypt

---

## 📝 License

MIT License - feel free to use and modify.
