#!/usr/bin/env bash

# Denne fil skal køres, når man starter job på UCloud. Den installerer miljøet/pakkerne, som bruges i projektet

## installerer python pakker
pip install --upgrade pip # opgraderer pip

# OBS! Nedenstående linje skal rettes så stien passer med projektet
pip install -r /CALDISS-projects/Leverancer/dlvr_sunburst-script_E24/requirements.txt