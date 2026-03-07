# Instagram Session Generator

A lightweight Python CLI tool that logs into Instagram and retrieves a fresh **`sessionid` cookie** by simulating a real Android device.

The project is organized around **device profiles**, where each script represents a specific smartphone fingerprint (for example a Pixel 7 Pro). Running a device script will attempt a login and output the session cookie for that simulated device.

---

## 📂 Project Structure

```
Instagram-session-generator
│
├── devices
│   └── pixel_7_pro.py
         (more devices added)
│
├── requirements.txt
└── README.md
```

Each script inside the **devices** folder acts as its own executable tool.

---

## ✨ Features

- Simulates Android device logins  
- Generates a random device ID for each session  
- Masked password input for security  
- Colored CLI output using Rich  
- Modular device-based structure  

---

## ⚙️ Requirements

- Python **3.8+**

Install dependencies:

```
pip install -r requirements.txt
```

Dependencies used:

- `requests`
- `pwinput`
- `rich`

---

## 🚀 Usage

Run a device script directly from the terminal.

Example:

```
python devices/pixel_7_pro.py
```

You will then be prompted to enter:

- Instagram username
- Instagram password

Example CLI output:

```
📲 Grab Fresh Pixel 7 Pro SessionID

👉 Enter Instagram Username: example_user
🔑 Enter Instagram Password: ********

✅ Logged in successfully!
New sessionid (tied to Pixel 7 Pro): 123456789%3AABCDEF123456789

✅ Save this sessionid for your Pixel 7 Pro cosmetic flex!
```

---

## 📱 Device Profiles

Each file inside the **devices** directory represents a simulated device configuration.

Example:

```
devices/
└── pixel_7_pro.py
```

Future device profiles can easily be added, such as:

```
devices/
├── pixel_7_pro.py
├── galaxy_s23.py
└── oneplus_12.py
```

---

## ⚠️ Disclaimer

This project is intended for **educational and testing purposes only**.

Automating login requests or interacting with online services through unofficial methods may violate the service's Terms of Service. Use this tool responsibly and only on accounts you own.

The author is not responsible for any misuse of this software.

---

## 👨‍💻 Author

**atrx07**  
insta handle : @atrx07
