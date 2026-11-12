# 🐧 Penguin Welcome Bot

A clean, lightweight, and modular Discord Welcome Bot built with `discord.py`. Designed for speed, easy customization, and 24/7 stability.

## ✨ Features
- **Custom Welcome Embeds:** Automatically greets new members with their avatar, server icon, and live member count.
- **Modular Cog Architecture:** Clean separation between core startup (`Welcome.py`), features (`cogs/welcome_cog.py`), and settings (`welcome_config.json`).
- **Admin Test Command:** Preview your welcome card anytime using `!testwelcome`.
- **Cloud-Ready:** Supports both local `config.json` and environment variables (`TOKEN`) for 24/7 hosting.

## 🚀 Setup & Installation

### 1. Requirements
Make sure you have **Python 3.10+** installed, then install `discord.py`:
```bash
pip install -U discord.py
```

### 2. Discord Developer Portal
1. Go to the [Discord Developer Portal](https://discord.com) and select your bot.
2. Go to the **Bot** tab and scroll down to **Privileged Gateway Intents**.
3. Enable **Server Members Intent** and **Message Content Intent**.

### 3. Configuration
Open `welcome_config.json` and replace the placeholders with your own details:
```json
{
    "token": "YOUR_BOT_TOKEN",
    "prefix": "!",
    "welcome_channel_id": 123456789012345678,
    "support_channel_id": 123456789012345678,
    "verify_channel_id": 123456789012345678
}
```

### 4. Run the Bot
```bash
python Welcome.py
```

---
*Made by **6YuaZ (Penguin)** — Thanks for your support!*
