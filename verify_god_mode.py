from main import supabase
import os

print("--- Verifying God Mode ---")
if not supabase:
    print("Supabase client is None!")
    exit(1)

try:
    # Try to list users (Requires Service Key)
    # The 'auth' namespace administration usually requires the service_role key
    print("Attempting to list users (Admin Action)...")
    users = supabase.auth.admin.list_users()
    print(f"Success! Found {len(users)} users.")
    for u in users[:3]:
        print(f" - {u.email} ({u.id})")
        
    print("\nGod Mode Verified: You have full Admin access.")
except Exception as e:
    print(f"\nFailed: {e}")
