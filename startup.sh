#!/bin/sh
uvicorn api.main:Banjo --host 0.0.0.0 --port 8001 --reload
