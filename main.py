from fastmcp import FastMCP
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import pg8000.native

# Load environment variables
load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
DB_HOST = os.getenv("SUPABASE_DB_HOST")
DB_USER = os.getenv("SUPABASE_DB_USER", "postgres")
DB_PORT = int(os.getenv("SUPABASE_DB_PORT", "5432"))

# Initialize Supabase Client
supabase = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        print(f"Error initializing Supabase client: {e}")

# Initialize MCP Server
mcp = FastMCP("GTS Brain Connector 🧠")

@mcp.tool()
def query_sql(query: str) -> str:
    """
    Execute raw SQL using direct Postgres connection.
    Use this for Admin tasks, Table creation, and complex queries.
    """
    if not DB_PASSWORD:
        return "Error: SUPABASE_DB_PASSWORD not set."
    
    try:
        conn = pg8000.native.Connection(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database="postgres",
            ssl_context=True # Supabase requires SSL
        )
        results = conn.run(query)
        conn.close()
        return str(results)
    except Exception as e:
        return f"SQL Error: {str(e)}"

@mcp.tool()
def read_table(table_name: str, limit: int = 10, select: str = "*") -> str:
    """Read data from a Supabase table via API (Requires Service Key)."""
    if not supabase:
        return "Error: Supabase Service Key not configured (Client unavailable)."
    try:
        response = supabase.table(table_name).select(select).limit(limit).execute()
        return str(response.data)
    except Exception as e:
        return f"Error reading table via API: {str(e)}"

@mcp.tool()
def upload_file(local_path: str, bucket_name: str, destination_path: str) -> str:
    """Upload a local file to a Supabase Storage bucket via API."""
    if not supabase:
        return "Error: Supabase Service Key not configured."
    try:
        with open(local_path, 'rb') as f:
            response = supabase.storage.from_(bucket_name).upload(
                file=f,
                path=destination_path,
                file_options={"upsert": "true"}
            )
        return f"Successfully uploaded to {bucket_name}/{destination_path}"
    except Exception as e:
        return f"Error uploading file: {str(e)}"

@mcp.tool()
def list_files(bucket_name: str, path: str = "") -> str:
    """List files in a Supabase Storage bucket."""
    if not supabase:
        return "Error: Supabase Service Key not configured."
    try:
        response = supabase.storage.from_(bucket_name).list(path)
        return str(response)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@mcp.tool()
def admin_create_user(email: str, password: str, role: str = "user") -> str:
    """
    Create a new user with a specific role (super_admin, mod, user).
    Requires Service Key (God Mode).
    """
    if not supabase:
        return "Error: Supabase Service Key not configured."
    
    try:
        # 1. Create User in Auth
        user = supabase.auth.admin.create_user({
            "email": email,
            "password": password,
            "email_confirm": True,
            "user_metadata": {"role": role}
        })
        
        user_id = user.user.id
        
        # 2. Assign Role in Profiles (Explicitly via REST)
        # Since we disabled the trigger, we MUST do this here.
        profile_data = {
            "id": user_id,
            "email": email,
            "role": role,
            "profile_settings": {
                "theme": "light",
                "notifications": True
            }
        }
        
        # Use upsert to be safe
        supabase.table("profiles").upsert(profile_data).execute()
        
        return f"Successfully created user {email} with role {role} (ID: {user_id})"
    except Exception as e:
        return f"Error creating user: {str(e)}"

@mcp.tool()
def admin_update_role(email: str, new_role: str) -> str:
    """
    Update a user's role (super_admin, mod, user).
    """
    if not supabase:
        return "Error: Supabase Service Key not configured."
        
    try:
        # Update role in profiles directly via REST
        # We need to find the user ID first, or just update by email if RLS allows?
        # Supabase API usually updates by PK (id).
        # But we can query for ID first.
        
        # 1. Get User ID by Email
        # using profiles table itself since it syncs email
        res = supabase.table("profiles").select("id").eq("email", email).single().execute()
        if not res.data:
            return f"Error: User {email} not found in profiles."
            
        user_id = res.data['id']
        
        # 2. Update Role
        response = supabase.table("profiles").update({"role": new_role}).eq("id", user_id).execute()
        return f"Updated role for {email} to {new_role}. Result: {str(response.data)}"
    except Exception as e:
        return f"Error updating role: {str(e)}"

@mcp.tool()
def update_profile_settings(user_id: str, settings_json: str) -> str:
    """
    Update a user's profile settings (JSONB).
    Example settings: {"theme": "dark", "notifications": false}
    """
    if not supabase:
        return "Error: Supabase Service Key not configured."
        
    try:
        import json
        settings = json.loads(settings_json)
        
        # Update using Supabase Client
        response = supabase.table("profiles").update({"profile_settings": settings}).eq("id", user_id).execute()
        return f"Updated settings for {user_id}: {str(response.data)}"
    except Exception as e:
        return f"Error updating settings: {str(e)}"

@mcp.tool()
def google_search(query: str, location: str = "Thailand") -> str:
    """
    Perform a Google search via SerpApi.
    Useful for finding forensic evidence, company info, or general web intel.
    """
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "Error: SERPAPI_API_KEY not set in environment."
    
    try:
        from serpapi import GoogleSearch
        search = GoogleSearch({
            "q": query,
            "location": location,
            "api_key": api_key
        })
        result = search.get_dict()
        return str(result.get("organic_results", []))
    except Exception as e:
        return f"Search Error: {str(e)}"

@mcp.tool()
def social_search(username: str, platform: str = "facebook") -> str:
    """
    Search for a person or account on social media via SerpApi.
    Supports: facebook, twitter, instagram, linkedin, etc.
    """
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "Error: SERPAPI_API_KEY not set in environment."
    
    try:
        from serpapi import GoogleSearch
        query = f"site:{platform}.com {username}"
        search = GoogleSearch({
            "q": query,
            "api_key": api_key
        })
        result = search.get_dict()
        return str(result.get("organic_results", []))
    except Exception as e:
        return f"Social Search Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
