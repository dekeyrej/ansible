#!/usr/bin/env bash
for i in aqi nfl mlb moon weather github events mycal; do kubectl scale -n default deployment $i --replicas=1; done
