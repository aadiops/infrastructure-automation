[Unit]
Description=Infrastructure Automation Service
After=network.target

[Service]
Type=simple
User=appuser
Group=appuser
WorkingDirectory=/opt/infrastructure-automation
Environment=FLASK_ENV=production
Environment=LOG_LEVEL=INFO
ExecStart=/usr/bin/python3 /opt/infrastructure-automation/app/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
