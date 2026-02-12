@echo off
title UNICORN MCP CONTROL UNIT
echo ==========================================
echo    UNICORN AGENTIC CALL (GPT-5.2)
echo ==========================================
set /p prompt="ENTER MISSION PROMPT: "
echo.
echo SENDING TO GTS BRAIN CONNECTOR...
python C:\Users\usEr\Project\unicorn-presentations\main.py call "%prompt%"
echo.
echo MISSION COMPLETED.
pause
