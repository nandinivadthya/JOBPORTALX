# JobPortalX - Quick Reference Guide

## 🎯 What's New

### Two User Roles

- **Job Seeker** 👤: Browse and apply for jobs
- **Recruiter** 💼: Post jobs and manage candidates

---

## 🚀 Quick Start

### For Job Seekers

```
1. Go to /register → Select "Job Seeker" → Register
2. Login → Go to Dashboard
3. Browse jobs in "Available Opportunities"
4. Click "Apply Now" → Add cover letter (optional) → Submit
5. Track applications in "My Applications" tab
```

### For Recruiters

```
1. Go to /register → Select "Recruiter" → Register
2. Login → Click "+ Post New Job"
3. Fill job details → Submit
4. Go to "My Jobs" tab to see posted jobs
5. Click "View Applicants" to see candidates
6. Accept or Reject applications
```

---

## 📋 Main Pages

| Page                | URL                      | Access    |
| ------------------- | ------------------------ | --------- |
| Home                | `/`                      | Public    |
| Login               | `/login/`                | Public    |
| Register            | `/register/`             | Public    |
| Employee Dashboard  | `/employee/dashboard/`   | Employee  |
| Recruiter Dashboard | `/recruiter/dashboard/`  | Recruiter |
| Post Job            | `/upload/job/`           | Recruiter |
| Apply for Job       | `/apply/job/<id>/`       | Employee  |
| View Applicants     | `/view/applicants/<id>/` | Recruiter |
| Admin               | `/admin/`                | Superuser |

---

## 🎨 UI Components

### Employee Dashboard

- **Available Opportunities Tab**: Browse all jobs with apply buttons
- **My Applications Tab**: View all your applications with status

### Recruiter Dashboard

- **My Jobs Tab**: View your posted jobs with edit/delete options
- **All Applications Tab**: View applications with accept/reject options
- **Statistics**: Jobs posted, total applications, accepted count

---

## 🔧 Database Fields

### Job Model

```
title          - Job title
company        - Company name
location       - Job location
salary         - Annual salary
description    - Job description
recruiter      - Who posted it (User FK)
created_at     - Posted timestamp
updated_at     - Last updated timestamp
```

### Application Model

```
user           - Job seeker (User FK)
job            - Applied job (Job FK)
applied_date   - Application timestamp
status         - pending/accepted/rejected
cover_letter   - Optional message to recruiter
```

---

## ✨ Key Features

| Feature            | Job Seeker | Recruiter |
| ------------------ | ---------- | --------- |
| Browse Jobs        | ✅         | -         |
| Apply for Jobs     | ✅         | -         |
| Track Applications | ✅         | -         |
| Post Jobs          | -          | ✅        |
| Edit Jobs          | -          | ✅        |
| Delete Jobs        | -          | ✅        |
| View Applicants    | -          | ✅        |
| Accept/Reject Apps | -          | ✅        |
| View Cover Letters | -          | ✅        |

---

## 🔐 Permission Rules

- **Only recruiters** can post, edit, delete jobs
- **Only employees** can apply for jobs
- **Recruiters** can only manage their own jobs
- **Prevent duplicate** applications for same job
- **Auto-redirect** to correct dashboard on login

---

## 📱 Responsive Design

- ✅ Mobile-friendly
- ✅ Tablet optimized
- ✅ Desktop optimized
- ✅ Touch-friendly buttons
- ✅ Readable on all screen sizes

---

## 🛠️ Admin Panel

Access at `/admin/`

**Manage:**

- Jobs (Create, Read, Update, Delete)
- Applications (Read, Update Status)
- Users (Create, Read, Update, Delete)

**Filters:**

- Jobs by location, company, date
- Applications by status, job, date

---

## 📊 Status Workflow

```
Application Submitted
         ↓
    PENDING ← (Default)
    ↙     ↘
ACCEPTED    REJECTED
```

---

## 💾 Database Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Backup database
python manage.py dumpdata > backup.json

# Reset database
python manage.py flush
```

---

## 🧪 Test Data

### Test Employee Account

- Email: employee@test.com
- Password: test123
- Type: Job Seeker

### Test Recruiter Account

- Email: recruiter@test.com
- Password: test123
- Type: Recruiter

### Test Job Post

```
Title: Python Developer
Company: TechCorp
Location: Bangalore
Salary: 600000
Description: We're hiring talented Python developers...
```

---

## 🎯 User Flows

### Employee Flow

```
Home → Register (Employee) → Login → Dashboard
       ↓
   Browse Jobs → Apply → View Applications
       ↓
   Track Status (Pending/Accepted/Rejected)
```

### Recruiter Flow

```
Home → Register (Recruiter) → Login → Dashboard
       ↓
   Post Job → View Applicants → Accept/Reject
       ↓
   Edit/Delete Jobs → View Application Details
```

---

## 🔍 Search & Filter

### Employee Dashboard

- Filter: Applied jobs, Available opportunities

### Recruiter Dashboard

- Filter: Posted jobs by date, Applications by status

---

## 📧 Future Enhancements

- [ ] Email notifications
- [ ] Resume upload
- [ ] Interview scheduling
- [ ] Candidate ratings
- [ ] Advanced searches
- [ ] Job bookmarks
- [ ] Premium listings
- [ ] Mobile app
- [ ] Payment integration
- [ ] Analytics dashboard

---

## ⚠️ Common Issues & Solutions

**Issue**: Migrations not applying

```bash
Solution: python manage.py migrate --fake initial
          python manage.py migrate
```

**Issue**: Duplicate application error

```bash
Solution: Design prevents this automatically
          Each user can apply once per job
```

**Issue**: Can't see jobs as recruiter

```bash
Solution: Login as recruiter, check "My Jobs" tab
          Your own job posts won't appear in employee view
```

---

## 📞 Support

For issues:

1. Check SETUP_AND_USAGE_GUIDE.md
2. Review IMPLEMENTATION_SUMMARY.md
3. Check Django logs in terminal
4. Verify database migrations: `python manage.py showmigrations`

---

## ✅ Verification Checklist

Before going live:

- [ ] All migrations applied
- [ ] Admin user created
- [ ] Test employee account works
- [ ] Test recruiter account works
- [ ] Can post job as recruiter
- [ ] Can apply as employee
- [ ] Can view applicants
- [ ] Dashboard redirects work
- [ ] Responsive design works
- [ ] All forms validate

---

**Version**: 1.0
**Last Updated**: February 2025
**Status**: Production Ready ✅
