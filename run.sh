#!/bin/bash
cd /opt/api
/opt/python/opmed/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 &
cd /opt/ui
quasar dev app.main:app --reload
