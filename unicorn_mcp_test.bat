@echo off
set "PYTHON_PATH=python"
set "CLI_SCRIPT=C:\Users\usEr\Project\unicorn-presentations\unicorn_cli.py"

echo ========================================================
echo   🦄 UNICORN COMMANDER (SECURITY TEST MODE)
echo ========================================================
echo.
echo AVAILABLE SKILLS (For Security Testing):
echo 1. apify_actor_call (Scraping/Spying)
echo 2. web_analysis_check (OSINT)
echo 3. verify_security_standard (Compliance)
echo 4. cloudflare_shield_status (Defense)
echo 5. google_search (Intel)
echo 6. social_search (Targeting)
echo 7. query_sql (Database Access - RLS Protected)
echo 8. issue_agency_policy (Governance)
echo.
set /p tool="ENTER TOOL NAME (or number 1-8): "

if "%tool%"=="1" set tool=apify_actor_call
if "%tool%"=="2" set tool=web_analysis_check
if "%tool%"=="3" set tool=verify_security_standard
if "%tool%"=="4" set tool=cloudflare_shield_status
if "%tool%"=="5" set tool=google_search
if "%tool%"=="6" set tool=social_search
if "%tool%"=="7" set tool=query_sql
if "%tool%"=="8" set tool=issue_agency_policy

echo.
set /p args="ENTER ARGUMENTS (Space separated, use quotes for strings): "
echo.
echo 🚀 EXECUTING %tool%...
%PYTHON_PATH% "%CLI_SCRIPT%" %tool% %args%
echo.
pause
