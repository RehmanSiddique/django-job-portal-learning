# Application Status Management Guide

## Status Types

Your job portal now supports 4 application statuses:

1. **Applied** (Default) - When user first applies
2. **Interview** - Candidate selected for interview
3. **Accepted** - Job offer accepted
4. **Rejected** - Application rejected

## How to Update Status (Admin)

### Method 1: Quick Edit (Recommended)
1. Go to Django Admin: `http://localhost:8000/admin/`
2. Click on "Applys" in the Core section
3. You'll see a list of all applications
4. **Change status directly in the list** using the dropdown
5. Click "Save" at the bottom

### Method 2: Individual Edit
1. Go to Django Admin
2. Click on "Applys"
3. Click on any application to open details
4. Change the "Status" field
5. Click "Save"

## Admin Features

- **List Display**: See user, job, status, and date at a glance
- **Filters**: Filter by status or date
- **Search**: Search by username or job title
- **Inline Editing**: Change status directly in the list view
- **Ordering**: Applications sorted by newest first

## User View (My Applications)

Users can:
- See all their applications
- View current status with color-coded badges:
  - 🟡 Applied (Yellow)
  - 🔵 Interview (Blue)
  - 🟢 Accepted (Green)
  - 🔴 Rejected (Red)
- Filter applications by status
- View job details
- Withdraw applications

## Status Badge Colors

- **Applied**: Warning (Yellow) - ⏰ Clock icon
- **Interview**: Info (Blue) - 👔 User-tie icon
- **Accepted**: Success (Green) - ✅ Check icon
- **Rejected**: Danger (Red) - ❌ Times icon

## Technical Details

### Model
```python
Status_CHOICES = [
    ('applied', 'Applied'),
    ('interview', 'Interview'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
]
```

### Unique Constraint
- Users can only apply once per job
- Duplicate applications are prevented

### Ordering
- Applications are ordered by newest first
- Applied date is automatically set
