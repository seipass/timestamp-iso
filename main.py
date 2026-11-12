from __future__ import annotations
def run(value):
 from datetime import datetime,timezone
 return datetime.fromtimestamp(value,timezone.utc).isoformat()
