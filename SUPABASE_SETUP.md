# Supabase Authentication Setup Guide

This guide explains how to set up Supabase authentication for the Unicorn application.

## Prerequisites

1. A Supabase account (sign up at https://supabase.com)
2. A Supabase project created

## Setup Steps

### 1. Create a Supabase Project

1. Go to https://supabase.com and sign in
2. Click "New Project"
3. Fill in your project details:
   - Project name: `unicorn-app` (or your preferred name)
   - Database password: Generate a strong password
   - Region: Choose the closest region to your users
4. Click "Create new project"

### 2. Get Your Supabase Credentials

1. In your Supabase project dashboard, go to **Settings** > **API**
2. You'll find:
   - **Project URL**: This is your `SUPABASE_URL`
   - **anon public key**: This is your `SUPABASE_ANON_KEY`

### 3. Configure the Supabase Client

1. Open `/assets/js/supabase-auth.js`
2. Replace the placeholder values with your actual credentials:

```javascript
const SUPABASE_URL = 'YOUR_SUPABASE_URL'; // Replace with your actual Supabase URL
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY'; // Replace with your actual anon key
```

Example:
```javascript
const SUPABASE_URL = 'https://abcdefghijklmnop.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
```

### 4. Enable Authentication Providers

#### Email/Password Authentication

Email/password authentication is enabled by default in Supabase.

To customize email templates:
1. Go to **Authentication** > **Email Templates** in your Supabase dashboard
2. Customize the templates for:
   - Confirmation email
   - Password reset email
   - Magic link email

#### Google OAuth

1. Go to **Authentication** > **Providers** in your Supabase dashboard
2. Find "Google" and toggle it on
3. You'll need to configure Google OAuth:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google+ API
   - Go to "Credentials" and create OAuth 2.0 credentials
   - Add authorized redirect URIs:
     - `https://YOUR_PROJECT_REF.supabase.co/auth/v1/callback`
   - Copy the Client ID and Client Secret
4. Back in Supabase, enter your Google Client ID and Client Secret
5. Update the redirect URLs in your site settings if needed

### 5. Configure Authentication Settings

1. Go to **Authentication** > **URL Configuration** in Supabase
2. Add your site URL to the **Site URL** field:
   - For production: `https://pripramot.github.io`
   - For development: `http://localhost:3000` (if testing locally)
3. Add redirect URLs to the **Redirect URLs** list:
   - `https://pripramot.github.io/login`
   - `https://pripramot.github.io/en/login`
   - Add any other URLs you want to allow

### 6. Test the Authentication

1. Navigate to your login page (`/login` or `/en/login`)
2. Try signing up with an email and password
3. Check your email for the confirmation link
4. Try logging in with Google OAuth
5. Verify that you're redirected to the home page after successful login

## Features Implemented

✅ Email/Password authentication
✅ Google OAuth authentication
✅ Session management
✅ Automatic redirect after login
✅ Error handling and user feedback
✅ Multi-language support (Thai and English)

## Security Best Practices

1. **Never commit your Supabase credentials** to version control
   - Consider using environment variables or a configuration file
   - Add `.env` to your `.gitignore`

2. **Enable Row Level Security (RLS)** on your database tables:
   ```sql
   ALTER TABLE your_table ENABLE ROW LEVEL SECURITY;
   ```

3. **Create RLS policies** to control data access:
   ```sql
   CREATE POLICY "Users can only see their own data" ON your_table
     FOR SELECT USING (auth.uid() = user_id);
   ```

4. **Enable email confirmations** in Authentication settings

5. **Configure password requirements** in Authentication settings

## Troubleshooting

### Issue: "Supabase library not loaded"

**Solution**: Make sure the Supabase CDN script is loaded before the auth script:
```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="/assets/js/supabase-auth.js"></script>
```

### Issue: Google OAuth not working

**Solution**: 
1. Check that your Google OAuth credentials are correct
2. Verify that the redirect URL in Google Console matches your Supabase callback URL
3. Make sure the Google+ API is enabled in your Google Cloud project

### Issue: Email confirmations not being sent

**Solution**:
1. Check your Supabase email settings
2. Verify your email templates are configured
3. Check the spam folder
4. Consider using a custom SMTP service for better deliverability

### Issue: Authentication works but user is not redirected

**Solution**:
1. Check the browser console for JavaScript errors
2. Verify the redirect logic in `supabase-auth.js`
3. Make sure the redirect URL is in the allowed list in Supabase

## Additional Resources

- [Supabase Authentication Documentation](https://supabase.com/docs/guides/auth)
- [Supabase JavaScript Client](https://supabase.com/docs/reference/javascript/auth-signup)
- [OAuth Configuration Guide](https://supabase.com/docs/guides/auth/social-login)

## Support

For issues or questions:
- Check the [Supabase Community](https://github.com/supabase/supabase/discussions)
- Contact the system administrator via the links on the login page
