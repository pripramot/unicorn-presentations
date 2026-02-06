# Supabase Authentication - Quick Start (Thai / ไทย)

## การตั้งค่าอย่างรวดเร็ว

### ขั้นตอนที่ 1: สร้างโปรเจค Supabase

1. ไปที่ https://supabase.com และสมัครสมาชิก
2. สร้างโปรเจคใหม่
3. บันทึก Project URL และ anon public key

### ขั้นตอนที่ 2: ตั้งค่า Credentials

แก้ไขไฟล์ `/assets/js/supabase-auth.js`:

```javascript
const SUPABASE_URL = 'https://xxxxx.supabase.co'; // ใส่ URL ของคุณ
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'; // ใส่ Key ของคุณ
```

### ขั้นตอนที่ 3: เปิดใช้งาน Google OAuth (ถ้าต้องการ)

1. ไปที่ Authentication > Providers ใน Supabase
2. เปิดใช้งาน Google
3. ตั้งค่า Google OAuth ใน Google Cloud Console
4. ใส่ Client ID และ Client Secret

### ขั้นตอนที่ 4: ตั้งค่า Redirect URLs

ใน Supabase Authentication > URL Configuration:

**Site URL:**
```
https://pripramot.github.io
```

**Redirect URLs:**
```
https://pripramot.github.io/login
https://pripramot.github.io/en/login
```

### ขั้นตอนที่ 5: ทดสอบ

1. เปิดหน้า login
2. ลองสมัครสมาชิกด้วยอีเมล
3. ตรวจสอบอีเมลยืนยัน
4. ลองเข้าสู่ระบบ

## ฟีเจอร์ที่มี

✅ เข้าสู่ระบบด้วยอีเมล/รหัสผ่าน
✅ เข้าสู่ระบบด้วย Google
✅ จัดการ Session อัตโนมัติ
✅ แสดงข้อความแจ้งเตือนผู้ใช้
✅ รองรับภาษาไทยและอังกฤษ

## ตัวอย่างการใช้งาน

### ตรวจสอบว่าผู้ใช้เข้าสู่ระบบหรือไม่

```javascript
const isLoggedIn = await window.SupabaseAuth.isAuthenticated();
if (isLoggedIn) {
  // ผู้ใช้เข้าสู่ระบบแล้ว
}
```

### ดึงข้อมูลผู้ใช้ปัจจุบัน

```javascript
const user = await window.SupabaseAuth.getCurrentUser();
console.log(user);
```

### ออกจากระบบ

```javascript
await window.SupabaseAuth.signOut();
```

## การแก้ปัญหา

### ปัญหา: ไม่สามารถเข้าสู่ระบบได้

1. ตรวจสอบว่าได้ใส่ Credentials ที่ถูกต้องใน `supabase-auth.js`
2. ตรวจสอบ Console ของ Browser หาข้อผิดพลาด
3. ตรวจสอบว่าได้เปิดใช้งาน Authentication ใน Supabase

### ปัญหา: ไม่ได้รับอีเมลยืนยัน

1. ตรวจสอบโฟลเดอร์ Spam
2. ตรวจสอบการตั้งค่าอีเมลใน Supabase
3. ลองส่งอีเมลยืนยันใหม่

### ปัญหา: Google OAuth ไม่ทำงาน

1. ตรวจสอบ Google OAuth Credentials
2. ตรวจสอบ Redirect URL ใน Google Console
3. ตรวจสอบว่าเปิดใช้งาน Google+ API

## ติดต่อสอบถาม

- Facebook: https://facebook.com/gts.wannakeeree
- GitHub: https://github.com/gittisak-go

---

# Supabase Authentication - Quick Start (English)

## Quick Setup

### Step 1: Create Supabase Project

1. Go to https://supabase.com and sign up
2. Create a new project
3. Save the Project URL and anon public key

### Step 2: Configure Credentials

Edit the file `/assets/js/supabase-auth.js`:

```javascript
const SUPABASE_URL = 'https://xxxxx.supabase.co'; // Your URL
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'; // Your Key
```

### Step 3: Enable Google OAuth (Optional)

1. Go to Authentication > Providers in Supabase
2. Enable Google
3. Configure Google OAuth in Google Cloud Console
4. Enter Client ID and Client Secret

### Step 4: Configure Redirect URLs

In Supabase Authentication > URL Configuration:

**Site URL:**
```
https://pripramot.github.io
```

**Redirect URLs:**
```
https://pripramot.github.io/login
https://pripramot.github.io/en/login
```

### Step 5: Test

1. Open the login page
2. Try signing up with email
3. Check confirmation email
4. Try logging in

## Features

✅ Email/Password authentication
✅ Google OAuth authentication
✅ Automatic session management
✅ User notification messages
✅ Thai and English language support

## Usage Examples

### Check if user is logged in

```javascript
const isLoggedIn = await window.SupabaseAuth.isAuthenticated();
if (isLoggedIn) {
  // User is logged in
}
```

### Get current user

```javascript
const user = await window.SupabaseAuth.getCurrentUser();
console.log(user);
```

### Sign out

```javascript
await window.SupabaseAuth.signOut();
```

## Troubleshooting

### Issue: Cannot log in

1. Check that you've entered correct credentials in `supabase-auth.js`
2. Check Browser Console for errors
3. Verify Authentication is enabled in Supabase

### Issue: Not receiving confirmation email

1. Check Spam folder
2. Check email settings in Supabase
3. Try resending confirmation email

### Issue: Google OAuth not working

1. Check Google OAuth credentials
2. Check Redirect URL in Google Console
3. Verify Google+ API is enabled

## Contact

- Facebook: https://facebook.com/gts.wannakeeree
- GitHub: https://github.com/gittisak-go
