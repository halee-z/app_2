# Quick Start: Deploy Phase II to Production

**Time Required**: ~20 minutes
**Prerequisites**: Vercel account, Neon PostgreSQL, GitHub access

---

## ⚡ Super Quick Version (Copy-Paste)

### 1. Get Your Neon Connection String

```bash
# From Neon Dashboard, copy your connection string:
# postgresql+asyncpg://user:password@host.neon.tech/database?sslmode=require
```

### 2. Deploy Backend

```bash
cd backend
npm install -g vercel  # if needed
vercel --prod
# Select "Other" framework when prompted
```

After deployment, save the URL shown:
```
✓ Deployed to https://todo-backend-XXXXX.vercel.app
```

### 3. Add Environment Variables to Vercel

Go to: https://vercel.com/dashboard/todo-backend-XXXXX/settings/environment-variables

Add these variables:
```
DATABASE_URL = postgresql+asyncpg://...  (from Neon)
JWT_SECRET = (generate random string, 32+ chars)
ALLOWED_ORIGINS = https://your-frontend-url.vercel.app
DEBUG = False
```

Click "Save" then "Redeploy"

### 4. Deploy Frontend

```bash
# Update environment file
echo "NEXT_PUBLIC_API_URL=https://todo-backend-XXXXX.vercel.app" > frontend/.env.production

cd frontend
vercel --prod
# Select "Next.js" when prompted
```

Save the frontend URL shown.

### 5. Update Backend CORS

Go back to backend Vercel settings → Environment Variables
- Edit `ALLOWED_ORIGINS`
- Set to: `https://your-frontend-url.vercel.app`
- Save and redeploy

### 6. Test It!

1. Open: https://your-frontend-url.vercel.app
2. Sign up for account
3. Create a task
4. Mark it complete
5. Delete it

✅ Done!

---

## 📖 Detailed Version

See `DEPLOYMENT-GUIDE.md` for:
- Troubleshooting
- Custom domains
- Monitoring setup
- Rollback procedures
- Post-deployment tasks

---

## 🚨 Troubleshooting

### "Cannot connect to database"
- Check Neon IP whitelist allows Vercel
- Verify DATABASE_URL is correct
- Try removing `?sslmode=require` temporarily

### "CORS Error"
- Make sure `ALLOWED_ORIGINS` matches frontend URL exactly
- Redeploy backend after changing CORS
- Check browser console for actual error

### "401 Unauthorized"
- Verify JWT_SECRET is set in backend
- Check token is being sent from frontend
- Look at browser Network tab

---

## 📝 Neon PostgreSQL Setup (If needed)

```bash
# 1. Create account at https://neon.tech
# 2. Create new project
# 3. Create new database (or use default 'neondb')
# 4. Copy connection string: postgresql+asyncpg://...

# 5. Run migrations (optional, for production):
# psql postgresql://... < schema.sql
```

---

## ✅ Verification Checklist

After deployment:
- [ ] Backend API responds: `curl https://backend-url/health`
- [ ] Frontend loads at: https://frontend-url
- [ ] Can sign up new account
- [ ] Can create task with title + description
- [ ] Can mark task complete (strikethrough)
- [ ] Can delete task
- [ ] Tasks persist after refresh
- [ ] Can logout and log back in

---

## 🆘 Need Help?

See `DEPLOYMENT-GUIDE.md` Section: "Troubleshooting"

Or check:
- Vercel logs: `vercel logs <project-name>`
- Neon console: https://console.neon.tech

---

**Status**: ✅ Ready to deploy!

Next steps:
1. Run steps 1-5 above
2. Test step 6
3. Share the live URL!

🚀
