from flask import Flask, request
import telebot

app = Flask(__name__)

# استبدل بمفتاح البوت الخاص بك
bot = telebot.TeleBot("7517544528:AAEwE_8hpzGDqaQyaNSBlRUHi0CZ-ptGn_o")

# استبدل بـ ID المحادثة أو المستخدم الخاص بك
chat_id = "5164991393"

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    try:
        bot.send_message(chat_id, "تم تشغيل البوت بنجاح")  # إرسال رسالة إلى البوت
        return "تم تشغيل بنجاح", 200
    except Exception as e:
        return f"لم يشتغل: {e}", 500

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        print("لم يشتغل:", e)
        
webhook_url = "https://telegram-rla4jetmd-l7ajs-projects.vercel.app"  # استبدله بـ URL Vercel الخاص بك
