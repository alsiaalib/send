import requests
import time
import os
import re
# 
token = os.getenv('TOKEN') #authorization
#token = ""
# Discord API URL
url = "https://discord.com/api/v9/channels/1279755843830677518/messages"

# 
headers = {
    "Content-Type": "application/json",
    "Authorization": f"{token}"
}

# 
nonce_file = 'nonce.txt'
if os.path.exists(nonce_file):
    with open(nonce_file, 'r') as file:
        nonce = file.read().strip()
else:
    nonce = "1289965068559426784" # change middle number +1 every time
    with open(nonce_file, 'w') as file:
        file.write(nonce)
# change nonce number to a large number if not work just like:
# 1289965 0 67559426784
#        ↓
# 1289965 1 67559426784
# 
while True:
    # 
    match = re.search(r"(.*?)(\d{6})(\d{4})", nonce)
    if match:
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        new_middle = str(int(middle) + 1).zfill(6)  # 增加1并保持6位长度
        nonce = f"{prefix}{new_middle}{suffix}"
        
        # 
        data = {
            "mobile_network_type": "wifi",
            "content": "Arcane is a bot with leveling and moderation features. It is online 247, it has the ability to welcome new members, and say goodbye to old ones. Add to Server Arcane can be added to a server for free by clicking the dd to Discordbutton on official site (https://arcane.bot/) or by clicking here (direct link). Custom Commands Arcane allows server admins to set up custom commands. These commands can respond with custom messages in a public channel. They can contain formatting, emoji, or links. Commands can also have cooldown times set. It is restricted to create 5 custom commands without Arcane Premium. Leveling If leveling is enabled, users gain XP when they send messages or talk in voice chats (Premium Only). Users will level up at specific XP thresholds, at which point an announcement is sent in a custom set channel or in a DM. XP for server members is recorded and listed on a server leaderboard, which can be found by entering the /leaderboard command. To avoid spamming, earning XP is limited to 1 message per minute. Use the !rank command to see any user's ranking, level, and XP. This perk is only for premium. Premium Arcane Premium is a paid subscription-based service that unlocks exclusive features. These include: - 12 Hour message logs - Fast logs (Near instant) - Unlimited Reaction roles - Youtube Alerts (5) - Unlimited custom commands - Voice leveling - Custom backgrounds - Custom XP values - Higher Uptime - Trivia Arcane is written in the Rust programming language",
            "nonce": nonce,
            "tts": False,
            "flags": 0
        }
        
        # 
        response = requests.post(url, headers=headers, json=data)
        print(response.status_code)
        print(response.json())
        
        # 
        with open(nonce_file, 'w') as file:
            file.write(nonce)
    else:
        print("error")
        break

    # 
    time.sleep(61)
