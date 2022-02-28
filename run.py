#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from grandpybot.views import app

if __name__ == "__main__":
    app.debug=True
    port = int(os.environ.get("PORT", 5400))
    app.run(debug=True, host='0.0.0.0', port=port)