#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import uuid
import requests
import pwinput
from rich.console import Console

console = Console()

# SAMSUNG DEVICE CONFIG
APP_VERSION = "269.0.0.30.117"
DEVICE_MODEL = "SM-S918B"
MANUFACTURER = "Samsung"
ANDROID_VERSION = "14"
RESOLUTION = "1440x3088"
DPI = "500"
LANGUAGE = "en_US"

# Generate random device ID
def generate_device_id():
    return str(uuid.uuid4())

# LOGIN FUNCTION
def insta_login_new_session(username, password):
    session = requests.Session()
    device_id = generate_device_id()

    headers = {
        "User-Agent": f"Instagram {APP_VERSION} Android ({ANDROID_VERSION}/34; {DPI}dpi; {RESOLUTION}; {MANUFACTURER}; {DEVICE_MODEL}; {DEVICE_MODEL.lower()}; {LANGUAGE})",
        "X-IG-App-ID": "936619743392459",
        "Accept-Language": LANGUAGE,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    session.headers.update(headers)

    login_url = "https://www.instagram.com/accounts/login/ajax/"

    # Get CSRF token
    r = session.get("https://www.instagram.com/accounts/login/")
    csrf = r.cookies.get("csrftoken")

    session.headers.update({
        "X-CSRFToken": csrf
    })

    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
    }

    res = session.post(login_url, data=payload, allow_redirects=True)

    try:
        data = res.json()
    except:
        data = {}

    if data.get("authenticated"):
        sessionid = session.cookies.get("sessionid")

        console.print("[green]✅ Logged in successfully![/green]")
        console.print(
            f"[cyan]New sessionid (tied to Samsung Galaxy S23 Ultra):[/cyan] "
            f"[bold yellow]{sessionid}[/bold yellow]"
        )

        return sessionid
    else:
        console.print(
            "[red]❌ Login failed! Username/password incorrect, 2FA required, or checkpoint triggered.[/red]"
        )
        return None


# MAIN
def main():
    console.print("[bold magenta]📱 Grab Fresh Samsung Galaxy S23 Ultra SessionID[/bold magenta]")

    username = input("👉 Enter Instagram Username: ")
    password = pwinput.pwinput(prompt="🔑 Enter Instagram Password: ", mask="*")

    sessionid = insta_login_new_session(username, password)

    if sessionid:
        console.print("[bold green]✅ Save this sessionid for your Samsung device session![/bold green]")


if __name__ == "__main__":
    main()
