"""
Helper script to kill all Chrome and Node.js processes (Windows only).
Use this if you get profile lock errors or can't start a new session.
"""
import subprocess

# Kill all Chrome processes
try:
    subprocess.run('taskkill /F /IM chrome.exe', shell=True, check=True)
    print('All Chrome processes killed.')
except Exception as e:
    print('No Chrome processes found or error:', e)

# Kill all Node.js processes
try:
    subprocess.run('taskkill /F /IM node.exe', shell=True, check=True)
    print('All Node.js processes killed.')
except Exception as e:
    print('No Node.js processes found or error:', e)

print('Done. You can now safely run your login or automation scripts.')
