/**
 * Supabase Authentication Module
 * Handles user authentication using Supabase
 */

// Supabase configuration
const SUPABASE_URL = 'YOUR_SUPABASE_URL'; // Replace with your Supabase project URL
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY'; // Replace with your Supabase anon key

// Initialize Supabase client
let supabase;

/**
 * Initialize Supabase client
 */
async function initSupabase() {
  if (typeof window.supabase === 'undefined') {
    console.error('Supabase library not loaded. Please include the Supabase CDN script.');
    return false;
  }
  
  try {
    supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    
    // Check if user is already logged in
    const { data: { session } } = await supabase.auth.getSession();
    if (session) {
      handleAuthSuccess(session.user);
    }
    
    // Listen for auth state changes
    supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN' && session) {
        handleAuthSuccess(session.user);
      } else if (event === 'SIGNED_OUT') {
        handleSignOut();
      }
    });
    
    return true;
  } catch (error) {
    console.error('Error initializing Supabase:', error);
    return false;
  }
}

/**
 * Sign in with email and password
 */
async function signInWithEmail(email, password) {
  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email,
      password: password,
    });

    if (error) throw error;

    handleAuthSuccess(data.user);
    return { success: true, user: data.user };
  } catch (error) {
    console.error('Error signing in:', error);
    showError(error.message || 'เกิดข้อผิดพลาดในการเข้าสู่ระบบ');
    return { success: false, error: error.message };
  }
}

/**
 * Sign in with Google OAuth
 */
async function signInWithGoogle() {
  try {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: {
        redirectTo: window.location.origin + '/login'
      }
    });

    if (error) throw error;

    return { success: true };
  } catch (error) {
    console.error('Error signing in with Google:', error);
    showError(error.message || 'เกิดข้อผิดพลาดในการเข้าสู่ระบบด้วย Google');
    return { success: false, error: error.message };
  }
}

/**
 * Sign up new user
 */
async function signUpWithEmail(email, password) {
  try {
    const { data, error } = await supabase.auth.signUp({
      email: email,
      password: password,
    });

    if (error) throw error;

    showSuccess('สมัครสมาชิกสำเร็จ! กรุณาตรวจสอบอีเมลเพื่อยืนยันบัญชี');
    return { success: true, user: data.user };
  } catch (error) {
    console.error('Error signing up:', error);
    showError(error.message || 'เกิดข้อผิดพลาดในการสมัครสมาชิก');
    return { success: false, error: error.message };
  }
}

/**
 * Sign out current user
 */
async function signOut() {
  try {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
    
    handleSignOut();
    return { success: true };
  } catch (error) {
    console.error('Error signing out:', error);
    showError(error.message || 'เกิดข้อผิดพลาดในการออกจากระบบ');
    return { success: false, error: error.message };
  }
}

/**
 * Handle successful authentication
 */
function handleAuthSuccess(user) {
  console.log('User authenticated:', user);
  showSuccess('เข้าสู่ระบบสำเร็จ! กำลังเปลี่ยนหน้า...');
  
  // Store user info in session storage
  sessionStorage.setItem('unicorn_user', JSON.stringify(user));
  
  // Redirect to home page after 1 second
  setTimeout(() => {
    window.location.href = '/';
  }, 1000);
}

/**
 * Handle sign out
 */
function handleSignOut() {
  sessionStorage.removeItem('unicorn_user');
  showSuccess('ออกจากระบบสำเร็จ');
}

/**
 * Get current user
 */
async function getCurrentUser() {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    return user;
  } catch (error) {
    console.error('Error getting user:', error);
    return null;
  }
}

/**
 * Check if user is authenticated
 */
async function isAuthenticated() {
  const { data: { session } } = await supabase.auth.getSession();
  return !!session;
}

/**
 * Show error message
 */
function showError(message) {
  const messageDiv = document.getElementById('auth-message');
  if (messageDiv) {
    messageDiv.innerHTML = `<div class="alert alert--danger margin-bottom--md" role="alert">${message}</div>`;
    setTimeout(() => {
      messageDiv.innerHTML = '';
    }, 5000);
  } else {
    alert(message);
  }
}

/**
 * Show success message
 */
function showSuccess(message) {
  const messageDiv = document.getElementById('auth-message');
  if (messageDiv) {
    messageDiv.innerHTML = `<div class="alert alert--success margin-bottom--md" role="alert">${message}</div>`;
  } else {
    alert(message);
  }
}

/**
 * Initialize authentication on page load
 */
if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', async () => {
    await initSupabase();
  });
}

// Export functions for use in HTML
if (typeof window !== 'undefined') {
  window.SupabaseAuth = {
    initSupabase,
    signInWithEmail,
    signInWithGoogle,
    signUpWithEmail,
    signOut,
    getCurrentUser,
    isAuthenticated
  };
}
