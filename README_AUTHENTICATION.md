# 🎉 Supabase Authentication - คู่มือการใช้งาน (Complete Guide)

## ภาษาไทย (Thai)

### 📋 สิ่งที่ได้รับการติดตั้ง

ระบบยืนยันตัวตนด้วย Supabase ได้ถูกผสานรวมเข้ากับเว็บไซต์ Unicorn เรียบร้อยแล้ว โดยมีฟีเจอร์ดังนี้:

✅ **การเข้าสู่ระบบด้วยอีเมลและรหัสผ่าน**
✅ **การเข้าสู่ระบบด้วย Google (OAuth)**
✅ **การจัดการ Session อัตโนมัติ**
✅ **การแสดงข้อความแจ้งเตือนผู้ใช้**
✅ **รองรับภาษาไทยและภาษาอังกฤษ**

### 🚀 วิธีเริ่มใช้งาน (3 ขั้นตอน)

#### ขั้นตอนที่ 1: สร้างบัญชี Supabase
1. ไปที่ https://supabase.com
2. คลิก "Start your project"
3. สร้าง Project ใหม่
4. จดบันทึก **Project URL** และ **API Key (anon public)**

#### ขั้นตอนที่ 2: ใส่ข้อมูล Credentials
แก้ไขไฟล์ `/assets/js/supabase-auth.js` บรรทัดที่ 7-8:

```javascript
// เปลี่ยนจาก:
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';

// เป็น:
const SUPABASE_URL = 'https://xxxxxxxxxxxxx.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxx...';
```

#### ขั้นตอนที่ 3: ตั้งค่า Supabase Dashboard
1. ไปที่ **Authentication** → **Providers** ใน Supabase
2. เปิดใช้งาน **Email** (เปิดอยู่แล้วตามค่าเริ่มต้น)
3. เปิดใช้งาน **Google** (ถ้าต้องการ - ต้องมี Google OAuth credentials)
4. ไปที่ **Authentication** → **URL Configuration**
5. ตั้งค่า:
   - **Site URL**: `https://pripramot.github.io`
   - **Redirect URLs**: 
     ```
     https://pripramot.github.io/login
     https://pripramot.github.io/en/login
     ```

### 🎯 ทดสอบระบบ

1. เปิดหน้า https://pripramot.github.io/login
2. ลองสมัครสมาชิกด้วยอีเมล
3. ตรวจสอบอีเมลยืนยันตัวตน
4. ลองเข้าสู่ระบบ
5. ระบบจะพาไปหน้าแรกอัตโนมัติ

### 📖 เอกสารเพิ่มเติม

- **[SUPABASE_SETUP.md](./SUPABASE_SETUP.md)** - คู่มือการตั้งค่าแบบละเอียด
- **[QUICK_START.md](./QUICK_START.md)** - คู่มือเริ่มต้นแบบย่อ
- **[IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md)** - สรุปการทำงานของระบบ

### 🔧 การแก้ปัญหา

#### ปัญหา: ไม่สามารถเข้าสู่ระบบได้
- ตรวจสอบว่าใส่ Credentials ถูกต้องแล้ว
- เปิด Browser Console (F12) ดูข้อผิดพลาด
- ตรวจสอบว่าเปิดใช้งาน Authentication ใน Supabase

#### ปัญหา: ไม่ได้รับอีเมลยืนยัน
- ตรวจสอบโฟลเดอร์ Spam
- ตรวจสอบการตั้งค่าอีเมลใน Supabase
- ลองส่งอีเมลยืนยันใหม่

#### ปัญหา: Google Login ไม่ทำงาน
- ตรวจสอบว่าได้ตั้งค่า Google OAuth ใน Supabase แล้ว
- ตรวจสอบ Redirect URL ใน Google Cloud Console
- ตรวจสอบว่าเปิดใช้งาน Google+ API

### 📞 ติดต่อสอบถาม

- **Facebook**: https://facebook.com/gts.wannakeeree
- **GitHub**: https://github.com/gittisak-go

---

## English

### 📋 What's Been Installed

The Supabase authentication system has been successfully integrated into the Unicorn website with the following features:

✅ **Email and Password Authentication**
✅ **Google OAuth Sign-in**
✅ **Automatic Session Management**
✅ **User Notification Messages**
✅ **Multi-language Support (Thai/English)**

### 🚀 Getting Started (3 Steps)

#### Step 1: Create Supabase Account
1. Go to https://supabase.com
2. Click "Start your project"
3. Create a new project
4. Note down your **Project URL** and **API Key (anon public)**

#### Step 2: Add Credentials
Edit the file `/assets/js/supabase-auth.js` lines 7-8:

```javascript
// Change from:
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';

// To:
const SUPABASE_URL = 'https://xxxxxxxxxxxxx.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxx...';
```

#### Step 3: Configure Supabase Dashboard
1. Go to **Authentication** → **Providers** in Supabase
2. Enable **Email** (enabled by default)
3. Enable **Google** (optional - requires Google OAuth credentials)
4. Go to **Authentication** → **URL Configuration**
5. Set:
   - **Site URL**: `https://pripramot.github.io`
   - **Redirect URLs**: 
     ```
     https://pripramot.github.io/login
     https://pripramot.github.io/en/login
     ```

### 🎯 Testing

1. Open https://pripramot.github.io/login
2. Try signing up with email
3. Check confirmation email
4. Try logging in
5. System will redirect to home page automatically

### 📖 Additional Documentation

- **[SUPABASE_SETUP.md](./SUPABASE_SETUP.md)** - Detailed setup guide
- **[QUICK_START.md](./QUICK_START.md)** - Quick reference
- **[IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md)** - Implementation overview

### 🔧 Troubleshooting

#### Issue: Cannot log in
- Check that credentials are correct
- Open Browser Console (F12) for errors
- Verify Authentication is enabled in Supabase

#### Issue: Not receiving confirmation email
- Check Spam folder
- Check email settings in Supabase
- Try resending confirmation email

#### Issue: Google Login doesn't work
- Check that Google OAuth is configured in Supabase
- Verify Redirect URL in Google Cloud Console
- Check that Google+ API is enabled

### 📞 Contact

- **Facebook**: https://facebook.com/gts.wannakeeree
- **GitHub**: https://github.com/gittisak-go

---

## 📦 Files Created/Modified

```
✅ /assets/js/supabase-auth.js         - Authentication module (220 lines)
✅ /login/index.html                    - Thai login page (updated)
✅ /en/login/index.html                 - English login page (updated)
✅ /SUPABASE_SETUP.md                   - Detailed setup guide (164 lines)
✅ /QUICK_START.md                      - Quick start guide (211 lines)
✅ /IMPLEMENTATION_SUMMARY.md           - Implementation summary (265 lines)
✅ /README_AUTHENTICATION.md            - This file
```

**Total**: 920+ lines of code and documentation added

---

## 🎓 How It Works

### Authentication Flow

```
User visits login page
        ↓
Supabase library loads
        ↓
Check existing session
        ↓
    ┌───┴───┐
    │       │
Session   No Session
exists    (show login form)
    │           ↓
    │     User enters credentials
    │           ↓
    │     Supabase authenticates
    │           ↓
    │     Session created
    │           ↓
    └─────┬─────┘
          ↓
    Redirect to home
```

### Session Management

- **Automatic**: Sessions are managed by Supabase
- **Persistent**: Sessions survive page refreshes
- **Secure**: Stored in browser localStorage
- **Auto-logout**: Can be configured in Supabase

### API Functions Available

```javascript
// Check if logged in
const isLoggedIn = await window.SupabaseAuth.isAuthenticated();

// Get current user
const user = await window.SupabaseAuth.getCurrentUser();

// Sign in
await window.SupabaseAuth.signInWithEmail(email, password);

// Sign in with Google
await window.SupabaseAuth.signInWithGoogle();

// Sign out
await window.SupabaseAuth.signOut();
```

---

## 🔐 Security Features

✅ **Secure token storage** (handled by Supabase)
✅ **HTTPS enforced** (GitHub Pages)
✅ **OAuth 2.0** for Google sign-in
✅ **Session tokens** with automatic refresh
✅ **Row Level Security** ready

### Recommended Security Settings

1. **Enable email confirmation** in Supabase Authentication settings
2. **Set password requirements** (minimum length, special characters)
3. **Enable rate limiting** to prevent brute force attacks
4. **Configure Row Level Security (RLS)** on database tables
5. **Use custom SMTP** for better email deliverability

---

## ✨ Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Email/Password Auth | ✅ Complete | Ready to use |
| Google OAuth | ✅ Complete | Requires Google setup |
| Session Management | ✅ Complete | Automatic |
| Error Handling | ✅ Complete | User-friendly messages |
| Multi-language | ✅ Complete | Thai & English |
| Auto-redirect | ✅ Complete | To home page |
| Documentation | ✅ Complete | 3 comprehensive guides |

---

## 🎉 Ready to Use!

Your Supabase authentication system is ready. Just:
1. Add your Supabase credentials
2. Configure the dashboard
3. Test and deploy!

**Good luck!** 🚀

---

*Last updated: February 6, 2026*
*Repository: pripramot/unicorn-presentations*
