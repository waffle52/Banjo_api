#!/usr/bin/env python3
"""utils.py
This file...
"""
import os
import jwt
from configparser import ConfigParser


def set_up():
     """Sets up configuration for the app"""
     env = os.getenv("ENV",".config")

     if env == ".config":
         config = ConfigParser()
         config.read(".config")
         config = config["AUTH0"]
     else:
         config = {
             "DOMAIN": os.getenv("DOMAIN", "your.domain.com"),
             "API_AUDIENCE": os.getenv("API_AUDIENCE", "your.audience.com"),
             "ISSUER": os.getenv("ISSUER", "https://your.domain.com/"),
             "ALGORITHMS": os.getenv("ALGORITHMS", "HS256"),
         }
    return (config)
