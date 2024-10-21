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

    def run(self):
        print("Server is running. Waiting for moves...")
        while True:
            try:
                # Read the incoming message line by line
                if self.ser.in_waiting > 0:
                    received_data = self.ser.readline().decode('utf-8').strip()
                    print(f"Received raw data: {received_data}")

                    if received_data:
                        try:
                            # Parse the received JSON
                            received_message = json.loads(received_data)
                            player_move = received_message.get("move")

                            if player_move:
                                print(f"Received move: {player_move}")

                                # Generate server's move
                                server_move = random.choice(["rock", "paper", "scissors"])

                                # Determine winner
                                result = self.determine_winner(player_move, server_move)

                                # Prepare and send response
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