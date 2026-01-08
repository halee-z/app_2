# 📋 STEP-BY-STEP DEPLOYMENT GUIDE

**Date**: 2026-01-09
**Status**: Starting deployment process
**Repository**: https://github.com/halee-z/Todo.app_phase.2.git

---

## ✅ STEP 1: DEPLOY FRONTEND TO VERCEL

### What you need:
- ✅ Vercel account (logged in)
- ✅ GitHub account connected to Vercel
- ✅ Repository: `Todo.app_phase.2`

### Instructions:

**1.1** Go to: https://vercel.com/new

**1.2** You should see the "New Project" page

**1.3** Select your repository:
   - Look for: `halee-z/Todo.app_phase.2`
   - If you don't see it, click "Browse All Repositories"
   - Search for: `Todo.app_phase.2`
   - Click on it to select it

**1.4** Configure project settings:
   - **Project Name**: `todo-app-frontend` (or any name you want)
   - **Framework**: Select "Next.js"
   - **Root Directory**: `./frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

**1.5** Click **"Deploy"** button

**⏳ Wait**: Deployment will take 2-3 minutes
- You'll see: "Deploying..."
- Then: "Domains" section appears
- Finally: ✅ "Deployment complete!"

**1.6** When done, you'll see a URL like:
```
https://todo-app-frontend-XXXXX.vercel.app
```

### ✅ STEP 1 COMPLETE When:
- Page shows "Congratulations! Your project has been successfully deployed"
- You can see a live URL
- The URL is accessible (click it to test)

---

## ✅ STEP 2: GET FRONTEND URL AND SAVE IT

### What you got:
After step 1, Vercel gives you a **Frontend URL**.

### Example:
```
https://todo-app-frontend-abc123xyz.vercel.app
```

### Copy this URL:
1. Look at the page after deployment
2. You'll see the URL at the top
3. Click the copy icon or select and copy
4. **Save it somewhere** - you'll need it in Step 4

### ✅ STEP 2 COMPLETE When:
- You have the Frontend URL saved
- You can paste it somewhere safe
- You can access it in browser

---

## ✅ STEP 3: DEPLOY BACKEND TO VERCEL

### Go back to: https://vercel.com/new

### Instructions:

**3.1** Click **"New Project"** again (or go to new link above)

**3.2** Select the same repository:
   - `halee-z/Todo.app_phase.2`
   - (Same repo, different folder)

**3.3** Configure project settings:
   - **Project Name**: `todo-app-backend`
   - **Framework**: Select "Other" (or "Python")
   - **Root Directory**: `./backend`
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty

**3.4** Click **"Deploy"** button

**⏳ Wait**: Deployment will take 2-3 minutes
- Similar to frontend deployment
- Wait for ✅ "Deployment complete!"

**3.5** You'll get a Backend URL like:
```
https://todo-app-backend-YYYYY.vercel.app
```

### ✅ STEP 3 COMPLETE When:
- Deployment finished
- You have Backend URL
- Page shows deployment success

---

## ✅ STEP 4: CONFIGURE BACKEND ENVIRONMENT VARIABLES

### This is important! The backend needs:
- Database connection
- JWT secret
- CORS origins
- Other settings

### Instructions:

**4.1** After backend deploys, you're on the deployment page

**4.2** Click **"Settings"** tab (or go to project settings)

**4.3** Look for **"Environment Variables"** in left menu

**4.4** Click **"Add New"** to add variables:

Add these variables (one by one):

| Name | Value | Notes |
|------|-------|-------|
| `DATABASE_URL` | `sqlite+aiosqlite:///./todo_app.db` | For testing (change to Neon URL later) |
| `JWT_SECRET` | `your-super-secret-jwt-key-min-32-characters-long-CHANGE-THIS` | Generate random 32+ chars |
| `JWT_ALGORITHM` | `HS256` | Keep this exact value |
| `JWT_EXPIRATION_DAYS` | `7` | Keep this exact value |
| `DEBUG` | `False` | Keep this exact value |
| `API_HOST` | `0.0.0.0` | Keep this exact value |
| `API_PORT` | `8000` | Keep this exact value |
| `ALLOWED_ORIGINS` | Paste your **FRONTEND URL** | This is the URL from Step 2 |

**4.5** For example, ALLOWED_ORIGINS should be:
```
https://todo-app-frontend-abc123xyz.vercel.app
```

**4.6** After adding all variables, click **"Save"**

**4.7** You should see a message asking to redeploy

**4.8** Click **"Redeploy"** (or go to Deployments tab and click redeploy)

**⏳ Wait**: Redeployment takes 2-3 minutes

### ✅ STEP 4 COMPLETE When:
- All environment variables added
- Redeployment finished
- Backend is ready with all settings

---

## ✅ STEP 5: TEST BACKEND API

### Check if backend is working:

**5.1** Go to your Backend URL:
```
https://todo-app-backend-YYYYY.vercel.app/health
```

**5.2** You should see:
```json
{"status":"healthy"}
```

**5.3** If you see that, ✅ backend is working!

**5.4** If you see error:
- Check environment variables were added correctly
- Click redeploy again
- Wait 2-3 minutes
- Try again

### ✅ STEP 5 COMPLETE When:
- Backend health check returns `{"status":"healthy"}`
- No errors in response

---

## ✅ STEP 6: UPDATE FRONTEND WITH BACKEND URL

### The frontend needs to know where the backend is:

**6.1** Go to your frontend Vercel project settings

**6.2** Look for **"Environment Variables"**

**6.3** Add this variable:

| Name | Value |
|------|-------|
| `NEXT_PUBLIC_API_URL` | Your Backend URL |

**6.4** Example:
```
NEXT_PUBLIC_API_URL=https://todo-app-backend-YYYYY.vercel.app
```

**6.5** Click **"Save"**

**6.6** Go to **"Deployments"** tab

**6.7** Find the latest deployment (at top)

**6.8** Click the **"..."** menu → **"Redeploy"**

**⏳ Wait**: Redeployment takes 1-2 minutes

### ✅ STEP 6 COMPLETE When:
- Frontend environment variable added
- Redeployment finished
- Frontend is updated with backend URL

---

## ✅ STEP 7: TEST THE COMPLETE APPLICATION

### Now test everything together:

**7.1** Open your **Frontend URL**:
```
https://todo-app-frontend-abc123xyz.vercel.app
```

**7.2** You should see:
- ✅ Login page loads
- ✅ No errors in console

**7.3** Test Sign Up:
- Click "Sign Up"
- Enter email: `test@example.com`
- Enter password: `TestPassword123`
- Click "Sign Up"

**7.4** You should see:
- ✅ Form submits
- ✅ Redirects to dashboard
- ✅ No errors

**7.5** Test Create Task:
- Enter task: "Buy groceries"
- Enter description: "Milk, eggs, bread"
- Click "Add Task"

**7.6** You should see:
- ✅ Task appears in list
- ✅ No errors

**7.7** Test Mark Complete:
- Click checkbox on task
- Task should show strikethrough

**7.8** Test Delete:
- Click Delete button
- Confirm deletion
- Task should disappear

**7.9** Test Logout:
- Click "Logout" button
- Should redirect to login

### ✅ STEP 7 COMPLETE When:
- All tests pass ✅
- No console errors
- Application works as expected

---

## 🎉 DEPLOYMENT COMPLETE!

When all steps are done:

✅ **Frontend** deployed to Vercel
✅ **Backend** deployed to Vercel
✅ **Environment variables** configured
✅ **Application** working end-to-end
✅ **Live URLs** accessible worldwide

---

## 📊 SUMMARY OF URLs

After deployment, you'll have:

**Frontend URL**:
```
https://todo-app-frontend-XXXXX.vercel.app
```

**Backend URL**:
```
https://todo-app-backend-YYYYY.vercel.app
```

**API Health Check**:
```
https://todo-app-backend-YYYYY.vercel.app/health
```

---

## ⏱️ Total Time Required

- Step 1 (Frontend Deploy): 5 min
- Step 2 (Get URL): 1 min
- Step 3 (Backend Deploy): 5 min
- Step 4 (Env Variables): 3 min
- Step 5 (Test Backend): 2 min
- Step 6 (Update Frontend): 3 min
- Step 7 (Test App): 5 min

**TOTAL: ~25 minutes**

---

## 🆘 TROUBLESHOOTING

### Frontend won't deploy
- Check repository name is correct: `Todo.app_phase.2`
- Check root directory is: `./frontend`
- Check framework is: `Next.js`

### Backend won't deploy
- Check root directory is: `./backend`
- Check framework is: `Other`
- Check `requirements.txt` exists

### Backend health check fails
- Check environment variables were added
- Redeploy backend after adding variables
- Wait 2-3 minutes for redeployment

### Can't sign up
- Check frontend URL is correct
- Check backend URL is in frontend env variables
- Check backend health check works
- Look at browser console for errors

### Tasks not saving
- Check backend database is configured
- Check CORS is set to frontend URL
- Check backend redeploy completed

---

## ✅ NEXT STEPS

After all 7 steps complete:

1. ✅ Share your Frontend URL with others
2. ✅ They can sign up and use the app
3. ✅ Tasks are saved in database
4. ✅ Application is live and accessible

---

**You're ready to deploy! Follow these steps in order. Let me know when you complete each step!** 🚀
