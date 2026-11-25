import json, os, urllib.request
name = os.environ.get("VERSION_NAME", "")
body = {"message": {"topic": "updates",
  "notification": {"title": "تحديث جديد متاح", "body": f"الإصدار {name} جاهز. افتح التطبيق للتحديث."},
  "android": {"priority": "HIGH", "notification": {"channel_id": "updates"}}}}
req = urllib.request.Request(f"https://fcm.googleapis.com/v1/projects/{os.environ['FCM_PROJECT_ID']}/messages:send",
  data=json.dumps(body).encode(), headers={"Authorization": "Bearer " + os.environ["ACCESS_TOKEN"], "Content-Type": "application/json"})
try:
    print(urllib.request.urlopen(req).read().decode())
except urllib.error.HTTPError as e:
    print(e.code, e.read().decode()); raise
