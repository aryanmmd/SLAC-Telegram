from telethon import TelegramClient, events
import requests

# اطلاعات حساب تلگرام
api_id = "20287544"  # از my.telegram.org دریافت کنید
api_hash = "9906745c9610f17a0158a6ebda971c4d"  # از my.telegram.org دریافت کنید

# اطلاعات Webhook Slack
slack_webhook_url = "https://hooks.slack.com/services/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"  # از Slack دریافت کنید

# نام کانال (همان‌طور که در تلگرام نشان داده می‌شود)
channel_name = "aryan"  # مثلاً "MyPrivateChannel"

# ایجاد کلاینت Telethon
client = TelegramClient('session_name', api_id, api_hash)

# تنظیم رویداد برای پیام‌های کانال
@client.on(events.NewMessage())
async def handle_new_message(event):
    try:
        # بررسی اینکه پیام از کانال مورد نظر است
        if event.chat.title == channel_name:
            # دریافت پیام
            message_text = event.message.message

            # ارسال پیام به Slack
            response = requests.post(slack_webhook_url, json={"text": message_text})
            
            if response.status_code == 200:
                print(f"پیام ارسال شد: {message_text}")
            else:
                print(f"خطا در ارسال به Slack: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"خطا: {e}")

# اجرای کلاینت
client.start()
print("ربات در حال اجراست...")
client.run_until_disconnected()