![Candy Crush Soda Saga](https://static.wikia.nocookie.net/candy-crush-saga/images/4/48/Candy_Crush_Soda_Saga_HD_new.png/revision/latest/scale-to-width-down/1200?cb=20150301152342)
```
# Telegram Candy Crash Bot
## Overview

This Telegram bot is a simple game inspired by the popular Candy Crush Saga. It allows users to interact with a game board via Telegram messages to swap candies and earn points. The game is played on a 5x5 board filled with different candy emojis.

## Features

- **Game Board Interaction:** Users can interact with the game board using Telegram's inline keyboard functionality.
- **Candy Swapping:** Players select candies to swap their positions randomly, aiming to align similar candies (future scope).
- **Score Tracking:** Scores are tracked throughout the game session.
- **Game Reset:** Players can reset the game at any time.

## How to Play

1. Start a conversation with the bot on Telegram.
2. Use the `/start` command to initialize and display the game board.
3. Click on any candy emoji to swap it with another randomly chosen candy on the board.
4. The game automatically updates the board and your score after each move.
5. To reset the game and start over, press the "Reset Game" button.

## Installation

To run this bot, you need to create a bot in Telegram and get a token. Follow these steps:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/telegram-candy-crash-bot.git
   cd telegram-candy-crash-bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Set up your Telegram Bot Token:**
   Replace the `TOKEN` in the script with your actual Telegram Bot Token.

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

## Screenshots

![Candy Crash Game](path/to/your/candy_crash_game_image.png)

Replace `path/to/your/candy_crash_game_image.png` with the actual path to the screenshot of the game you want to include. Ensure the image depicts the game board with some interactions for clarity.

## Contributing

Feel free to fork the project and submit a pull request if you have features or improvements you would like to add.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### Including a Game Image in the README

1. **Capture a Screenshot:** While the bot is running and the game board is displayed, capture a screenshot of the Telegram chat showing the game in action.

2. **Save the Image:** Save the screenshot in your project repository, preferably in a folder named `images`.

3. **Link the Image in README.md:** Update the image path in the README.md to point to the location where you saved your screenshot. For example:
   ```markdown
   ![Candy Crash Game](images/candy_crash_game.png)
   ```

This setup will help users understand how the game works and how to interact with the bot, while providing a visual reference to enhance the appeal of your repository on GitHub.
