#Coding by Mustafa ip Follow me on instagram: https://www.instagram.com/tofa
import telebot
import random
import time

# Telegram API token
TOKEN = ""


# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Define game board size
BOARD_SIZE = 5

# Define emoji characters for candies
CANDY_EMOJIS = ["🍬", "🍭", "🍫", "🍩", "🍪"]

# Initialize the game board with random candies
game_board = [[random.choice(CANDY_EMOJIS) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Dictionary to store user points
user_points = {}

# Function to create an inline keyboard with candy emojis
def create_inline_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    for emoji in CANDY_EMOJIS:
        keyboard.row(telebot.types.InlineKeyboardButton(emoji, callback_data=emoji))
    keyboard.row(telebot.types.InlineKeyboardButton("Reset Game", callback_data="reset"))
    return keyboard

# Function to display the game board and inline keyboard
def display_board_and_keyboard(chat_id, message_id):
    board_str = ""
    for row in game_board:
        board_str += " ".join(row) + "\n"
    board_str += f"Points: {user_points.get(chat_id, 0)}\n"
    board_str += f"Last updated: {time.strftime('%H:%M:%S', time.localtime())}"
    inline_keyboard = create_inline_keyboard()
    if message_id:
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=board_str, reply_markup=inline_keyboard)
        except telebot.apihelper.ApiTelegramException as e:
            print(f"Error editing message: {e}")
    else:
        bot.send_message(chat_id=chat_id, text=board_str, reply_markup=inline_keyboard)

# Command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    display_board_and_keyboard(message.chat.id, None)

# Callback query handler for candy selection and game reset
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global game_board  # Declare game_board as global
    selected_candy = call.data
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if selected_candy == "reset":
        # Reset the game
        game_board = [[random.choice(CANDY_EMOJIS) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        user_points[chat_id] = 0
        display_board_and_keyboard(chat_id, message_id)
    else:
        # Find the position of the selected candy
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if game_board[i][j] == selected_candy:
                    # Move the candy to a random position
                    new_i, new_j = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
                    game_board[i][j], game_board[new_i][new_j] = game_board[new_i][new_j], game_board[i][j]
                    display_board_and_keyboard(chat_id, message_id)
                    time.sleep(1)  # Add a delay to avoid rate limiting
                    return

# Start the bot
bot.polling()
