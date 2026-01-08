# Phase II Production Deployment Guide

**Date**: 2026-01-09
**Status**: Ready for deployment
**Platforms**: Vercel (Backend + Frontend), Neon (PostgreSQL)

---

## Pre-Deployment Checklist

### Prerequisites
- ✅ GitHub repository: https://github.com/halee-z/Todo.app_phase.2.git
- ✅ Vercel account (connected to GitHub)
- ✅ Neon PostgreSQL account with database created
- ✅ Neon connection string ready

### Required Information to Gather

1. **Neon Database URL** (format: `postgresql+asyncpg://user:password@host/database?sslmode=require`)
2. **JWT Secret** (minimum 32 characters, should be cryptographically random)
3. **Frontend Domain** (where your Vercel frontend will be deployed)
4. **Backend Domain** (where your Vercel backend will be deployed)

---

## Step 1: Prepare Backend Configuration

### 1.1 Update Environment Variables Template

The backend needs these environment variables set in Vercel:

```
DATABASE_URL=postgresql+asyncpg://user:password@host/neon_db?sslmode=require
JWT_SECRET=<your-32+-char-secret>
JWT_ALGORITHM=HS256
JWT_EXPIRATION_DAYS=7
DEBUG=False
ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app
API_HOST=0.0.0.0
API_PORT=8000
```

**⚠️ IMPORTANT**: Do NOT commit these to git. Set them in Vercel UI only.

### 1.2 Verify Backend Files

Created for Vercel compatibility:
- ✅ `backend/vercel.json` - Vercel configuration
- ✅ `backend/wsgi.py` - ASGI entry point
- ✅ `backend/requirements.txt` - Updated with production dependencies

---

## Step 2: Deploy Backend to Vercel

### 2.1 Create Vercel Project for Backend

```bash
# From your Git repo directory
cd backend

# Install Vercel CLI (if not already installed)
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

**During deployment**:
- Select "Other" as framework
- Root directory: `backend`
- Build command: (leave empty or press enter)
- Output directory: (leave empty)

### 2.2 Add Environment Variables in Vercel Dashboard

1. Go to: https://vercel.com/dashboard
2. Select your backend project
3. Go to: Settings → Environment Variables
4. Add each variable:
   - `DATABASE_URL` = Your Neon connection string
   - `JWT_SECRET` = Your random 32+ char secret
   - `JWT_ALGORITHM` = HS256
   - `JWT_EXPIRATION_DAYS` = 7
   - `DEBUG` = False
   - `ALLOWED_ORIGINS` = https://your-frontend-domain.vercel.app
   - `API_HOST` = 0.0.0.0
   - `API_PORT` = 8000

5. Click "Save"
6. Redeploy: Settings → Deployments → Redeploy

### 2.3 Get Backend URL

After successful deployment, you'll see:
```
✓ Deployed to https://todo-app-backend-XXXXXXXXX.vercel.app
```

Save this URL. You'll need it for frontend configuration.

---

## Step 3: Deploy Frontend to Vercel

### 3.1 Update Frontend Environment Variables

Edit `frontend/.env.production`:

```
NEXT_PUBLIC_API_URL=https://your-backend-vercel-url.vercel.app
```

Replace with actual backend URL from Step 2.3.

### 3.2 Deploy Frontend

```bash
cd frontend

# Deploy to Vercel
vercel --prod
```

**During deployment**:
- Framework: Select "Next.js"
- Root directory: `frontend`
- Build command: `npm run build`
- Output directory: `.next`

### 3.3 Get Frontend URL

After successful deployment:
```
✓ Deployed to https://todo-app-XXXXXXXXXX.vercel.app
```

---

## Step 4: Configure CORS on Backend

Update backend environment variable:

1. Go to backend Vercel project
2. Settings → Environment Variables
3. Edit `ALLOWED_ORIGINS`
4. Set to: `https://your-frontend-vercel-url.vercel.app`
5. Save and redeploy

---

## Step 5: Verify Production Deployment

### 5.1 Test Backend API

```bash
# Health check
curl https://your-backend-url.vercel.app/health

# Expected response:
# {"status":"healthy"}
```

### 5.2 Test Frontend

1. Open: https://your-frontend-url.vercel.app
2. Should redirect to `/login`
3. Create test account
4. Create a task
5. Mark task complete
6. Delete task
7. Logout

### 5.3 Run Production Test Workflow

**Registration Test**:
1. Click "Sign Up"
2. Enter: test@example.com / TestPass123
3. Should redirect to dashboard

**Task Creation Test**:
1. Enter task title: "Buy groceries"
2. Enter description: "Milk, eggs, bread"
3. Click "Add Task"
4. Task should appear in list

**Task Completion Test**:
1. Check the checkbox
2. Title should strikethrough
3. Task moves to "Completed" section

**Task Deletion Test**:
1. Click Delete button
2. Confirm deletion
3. Task removed from list
4. Page refresh - task still gone

**Logout Test**:
1. Click Logout button
2. Should redirect to login

---

## Step 6: Configure Custom Domain (Optional)

### For Backend

1. Go to Vercel backend project
2. Settings → Domains
3. Add custom domain: `api.yourdomain.com`
4. Follow DNS configuration instructions

### For Frontend

1. Go to Vercel frontend project
2. Settings → Domains
3. Add custom domain: `app.yourdomain.com`
4. Follow DNS configuration instructions

Update backend CORS to use custom domain:
```
ALLOWED_ORIGINS=https://app.yourdomain.com
```

---

## Step 7: Set Up Monitoring & Logging

### Vercel Monitoring

1. Go to each Vercel project
2. Analytics → Overview
3. Monitor:
   - Response times
   - Error rates
   - Function invocations

### Database Monitoring

1. Go to Neon Dashboard
2. Monitor:
   - Connection usage
   - Query performance
   - Storage usage

---

## Troubleshooting

### Backend Won't Deploy

**Error**: "Module not found: src.main"
**Fix**: Ensure `backend/wsgi.py` exists and `backend/requirements.txt` has all dependencies

**Error**: "Connection refused to database"
**Fix**:
1. Verify DATABASE_URL in Vercel environment
2. Check Neon allowed IPs include Vercel IPs
3. Test connection string locally

### Frontend API Calls Fail (401/403)

**Error**: "Unauthorized" or "CORS error"
**Fix**:
1. Check `NEXT_PUBLIC_API_URL` points to correct backend
2. Verify backend `ALLOWED_ORIGINS` includes frontend URL
3. Check JWT token is being sent in Authorization header

### Tasks Don't Persist

**Error**: Tasks disappear after refresh
**Fix**:
1. Verify DATABASE_URL uses Neon (not SQLite)
2. Check database migrations ran: `alembic upgrade head`
3. Ensure `user_id` is being saved with tasks

### Auth Token Expires Too Quickly

**Error**: "Your session has expired" after <7 days
**Fix**:
1. Check JWT_EXPIRATION_DAYS=7 in backend environment
2. Verify client isn't clearing localStorage unexpectedly
3. Check token expiration in browser DevTools

---

## Rollback Plan

If deployment has issues:

### Rollback Backend

1. Go to Vercel backend project
2. Deployments tab
3. Find previous working deployment
4. Click "..." → Promote to Production

### Rollback Frontend

1. Go to Vercel frontend project
2. Deployments tab
3. Find previous working deployment
4. Click "..." → Promote to Production

---

## Production Checklist

### Before Going Live

- [ ] All environment variables set in Vercel
- [ ] Database migrations applied (`alembic upgrade head`)
- [ ] Backend API responding with correct CORS headers
- [ ] Frontend can authenticate and create tasks
- [ ] Tasks persist after page refresh
- [ ] All user stories work end-to-end
- [ ] No sensitive data in logs
- [ ] JWT secret is strong (32+ chars, random)
- [ ] DEBUG=False in production

### After Going Live

- [ ] Monitor Vercel analytics daily for first week
- [ ] Check error logs for any issues
- [ ] Test on mobile and desktop browsers
- [ ] Verify all user workflows work
- [ ] Set up alerts for API errors

---

## Post-Deployment Tasks

### 1. Set Up GitHub Actions (Optional)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main, 001-phase-ii-web-app]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: vercel/action@master
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

### 2. Set Up Monitoring Alerts

- Configure Vercel alerts for failed deployments
- Set up Neon alerts for slow queries
- Configure email notifications for errors

### 3. Plan Phase III

- [ ] Add task due dates and scheduling
- [ ] Implement task categories/tags
- [ ] Add task sharing and collaboration
- [ ] Build mobile app
- [ ] Add real-time updates with WebSockets

---

## Support Resources

- **Vercel Docs**: https://vercel.com/docs
- **Neon Docs**: https://neon.tech/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Next.js Docs**: https://nextjs.org/docs

---

## Deployment Timeline

| Step | Time | Status |
|------|------|--------|
| Backend setup | 5 min | ✅ Complete |
| Backend deploy | 2 min | ⏳ Pending |
| Frontend setup | 2 min | ⏳ Pending |
| Frontend deploy | 3 min | ⏳ Pending |
| Verification | 5 min | ⏳ Pending |
| **Total** | **~17 min** | ⏳ |

---

## Next Steps

1. Follow Step 2 to deploy backend
2. Copy backend URL to frontend `.env.production`
3. Follow Step 3 to deploy frontend
4. Test all workflows per Step 5
5. Configure CORS per Step 4
6. Monitor production per Step 7

---

**Questions?** Check the troubleshooting section or refer to official documentation links above.

Good luck! 🚀
