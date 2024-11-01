import serial
import json
import random


class GameServer:
    def __init__(self):
        # Configure serial connection
        self.ser = serial.Serial(
            port='/dev/serial0',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.last_move = None

    def determine_winner(self, player_move, server_move):
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

        # AI logic for other modes remains the same
        if difficulty == "easy":
            if self.last_move and random.random() < 0.7:
                return self.last_move
        elif difficulty == "medium":
            if self.last_move and random.random() < 0.3:
                return self.last_move

        move = random.choice(["rock", "paper", "scissors"])
        self.last_move = move
        return move

    def run(self):
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