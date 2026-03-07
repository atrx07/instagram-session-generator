#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import uuid
import requests
import pwinput
from rich.console import Console

console = Console()

# CONFIG
APP_VERSION = "269.0.0.30.117"
DEVICE_MODEL = "Pixel 7 Pro"
MANUFACTURER = "Google"
ANDROID_VERSION = "14"
RESOLUTION = "1440x3120"
DPI = "420"
LANGUAGE = "en_US"

# Generate a random device ID
def generate_device_id():
    return str(uuid.uuid4())

#LOGIN FUNCTION
def insta_login_new_session(username, password):
    session = requests.Session()
    device_id = generate_device_id()

    headers = {
        "User-Agent": f"Instagram {APP_VERSION} Android ({ANDROID_VERSION}/30; {DPI}dpi; {RESOLUTION}; {MANUFACTURER}; {DEVICE_MODEL}; {DEVICE_MODEL.lower()}; {LANGUAGE})",
        "X-IG-App-ID": "936619743392459",
        "Accept-Language": LANGUAGE,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    session.headers.update(headers)

    login_url = "https://www.instagram.com/accounts/login/ajax/"

    # Get CSRF token
    r = session.get("https://www.instagram.com/accounts/login/")
    csrf = r.cookies.get("csrftoken")
    session.headers.update({"X-CSRFToken": csrf})

    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
    }

    res = session.post(login_url, data=payload, allow_redirects=True)
    if "authenticated" in res.text:
        sessionid = session.cookies.get("sessionid")
        console.print(f"[green]✅ Logged in successfully![/green]")
        console.print(f"[cyan]New sessionid (tied to Pixel 7 Pro):[/cyan] [bold yellow]{sessionid}[/bold yellow]")
        return sessionid
    else:
        console.print("[red]❌ Login failed! Check username/password or 2FA may be required.[/red]")
        return None

#MAIN
def main():
    console.print("[bold magenta]📲 Grab Fresh Pixel 7 Pro SessionID[/bold magenta]")
    username = input("👉 Enter Instagram Username: ")
    password = pwinput.pwinput(prompt="🔑 Enter Instagram Password: ", mask="*")
    sessionid = insta_login_new_session(username, password)
    if sessionid:
        console.print("[bold green]✅ Save this sessionid for your Pixel 7 Pro cosmetic flex![/bold green]")

if __name__ == "__main__":
    main()
