#!/usr/bin/env python3
import os
from onportrait import app, db

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
