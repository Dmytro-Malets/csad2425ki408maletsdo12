"""!
@file server.py
@brief Server implementation for Rock-Paper-Scissors game using serial communication.

This file implements the server-side logic for a Rock-Paper-Scissors game,
handling serial communication with clients and implementing game mechanics
for different modes (Player vs AI, Player vs Player, AI vs AI).

@author Dmytro Malets
@date 2024-11-04
"""

import serial
import json
import random


class GameServer:
    """!
    @brief Server implementation for the Rock-Paper-Scissors game.

    This class implements the server-side logic for a Rock-Paper-Scissors game,
    handling serial communication with clients, game moves processing, and
    implementing various game modes including player vs AI and player vs player.

    @note The server runs on a Raspberry Pi 3 Model B and communicates via serial connection
    """
    def __init__(self):
        """!
        @brief Initialize the GameServer with serial connection settings.

        Sets up the serial connection with predefined parameters and initializes
        game state variables.
        """
        ## @brief Serial connection object
        self.ser = serial.Serial(
            port='/dev/serial0',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        ## @brief Stores the last move for AI strategy
        self.last_move = None

    def determine_winner(self, player_move, server_move):
        """!
        @brief Determine the winner of a game round.

        Implements the Rock-Paper-Scissors game logic to determine the winner
        based on classic rules:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock

        @param player_move The move chosen by the player ("rock", "paper", or "scissors")
        @param server_move The move chosen by the server ("rock", "paper", or "scissors")
        @return str Returns "Draw", "You win!", or "Server wins!" based on the game outcome
        """
        if player_move == server_move:
            return "Draw"
        elif (
            (player_move == "rock" and server_move == "scissors") or
            (player_move == "paper" and server_move == "rock") or
            (player_move == "scissors" and server_move == "paper")
        ):
            return "You win!"
        else:
            return "Server wins!"

    def get_server_move(self, difficulty, game_mode="man_vs_ai"):
        """!
        @brief Generate server's move based on game mode and difficulty.

        In AI mode, generates moves based on difficulty settings:
        - Easy: 70% chance to repeat last move
        - Medium: 30% chance to repeat last move
        - Hard: Pure random choice

        In PvP mode, prompts Player B for input.

        @param difficulty The game difficulty level ("easy", "medium", "hard")
        @param game_mode The game mode ("man_vs_ai", "man_vs_man", "ai_vs_ai")
        @return str The selected move ("rock", "paper", or "scissors")
        @throws KeyboardInterrupt When user interrupts input in PvP mode
        """
        # Handle PvP mode
        if game_mode == "man_vs_man":
            print("\nPlayer B's turn! Enter your move (rock/paper/scissors):")
            while True:
                try:
                    move = input().lower().strip()
                    if move in ["rock", "paper", "scissors"]:
                        return move
                    print("Invalid move! Please enter rock, paper, or scissors.")
                except KeyboardInterrupt:
                    print("\nInput interrupted. Please try again.")
                except Exception as e:
                    print(f"Error reading input: {e}. Please try again.")

        # AI logic for other modes
        ## @brief Implement easy mode strategy
        if difficulty == "easy":
            if self.last_move and random.random() < 0.7:
                return self.last_move
        ## @brief Implement medium mode strategy
        elif difficulty == "medium":
            if self.last_move and random.random() < 0.3:
                return self.last_move

        move = random.choice(["rock", "paper", "scissors"])
        self.last_move = move
        return move

    def run(self):
        """!
        @brief Start the game server and handle client connections.

        Main server loop that:
        1. Waits for client moves via serial connection
        2. Processes received moves
        3. Generates server responses
        4. Sends results back to client

        @note The server runs indefinitely until interrupted
        @throws json.JSONDecodeError When received invalid JSON data
        """
        print("Server is running. Waiting for moves...")
        while True:
            try:
                if self.ser.in_waiting > 0:
                    received_data = self.ser.readline().decode('utf-8').strip()
                    print(f"Received raw data: {received_data}")

                    if received_data:
                        try:
                            received_message = json.loads(received_data)
                            player_move = received_message.get("move")
                            difficulty = received_message.get("difficulty", "hard")
                            game_mode = received_message.get("game_mode", "man_vs_ai")

                            if player_move:
                                server_move = self.get_server_move(difficulty, game_mode)
                                result = self.determine_winner(player_move, server_move)

                                if game_mode == "man_vs_man":
                                    if result == "You win!":
                                        result = "Player A wins!"
                                    elif result == "Server wins!":
                                        result = "Player B wins!"

                                response = {
                                    "server_move": server_move,
                                    "result": result
                                }

                                response_json = json.dumps(response) + '\n'
                                self.ser.write(response_json.encode('utf-8'))
                                print(f"Sent response: {response}")
                            else:
                                print("Error: No move in message")

                        except json.JSONDecodeError as e:
                            print(f"JSON decode error: {e}")
                            error_response = json.dumps({"error": "Invalid JSON format"}) + '\n'
                            self.ser.write(error_response.encode('utf-8'))

            except Exception as e:
                print(f"Error: {e}")
                try:
                    error_response = json.dumps({"error": str(e)}) + '\n'
                    self.ser.write(error_response.encode('utf-8'))
                except:
                    pass


if __name__ == "__main__":
    server = GameServer()
    try:
        server.run()
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        server.ser.close()