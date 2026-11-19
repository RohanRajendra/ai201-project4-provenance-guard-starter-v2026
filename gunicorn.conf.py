"""
The run path (unit 9):

    gunicorn -c gunicorn.conf.py app:app

One worker on purpose. Each worker loads its own copy of gpt2, and the rate
limiter's memory:// store lives inside one process, so two workers would each
allow 5 a minute. HOST and PORT come from the environment, as in config.py.
"""

import os

bind = f"{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '5000')}"
workers = 1
timeout = 120  # the first /submit loads gpt2 inside the request
