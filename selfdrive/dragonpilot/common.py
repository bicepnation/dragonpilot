#!/usr/bin/env python3.7

dp_is_online = not subprocess.call(["ping", "-W", "4", "-c", "1", "117.28.245.92"])