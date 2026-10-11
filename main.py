from logic import analyze_logs
import json

get_logs_status = analyze_logs()

print(json.dumps(get_logs_status, indent=4, ensure_ascii=False))
