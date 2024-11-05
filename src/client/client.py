from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from PySide6.QtGui import QPixmap
import sys
import serial
import json
import time
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.common.config_handler import ConfigHandler
from ui_main import Ui_MainWindow
from ui_statistic import Ui_Dialog


class StatisticWindow(QWidget):
    def __init__(self, stats):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Game Statistics")
        self.update_stats(stats)

    def update_stats(self, stats):
        games_played = stats['games_played']
        player_score = stats['player_score']
        server_score = stats['server_score']
        win_rate = (player_score / games_played * 100 if games_played > 0 else 0)

        self.ui.total_games_played_counter_lb.setText(str(games_played))
        self.ui.player_wins_counter_lb.setText(str(player_score))
        self.ui.ai_wins_counter_lb.setText(str(server_score))
        self.ui.win_rate_value_lb.setText(f"{win_rate:.1f}%")


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rock Paper Scissors")

        self.config_handler = ConfigHandler()

        # Initialize serial connection using config
        conn_settings = self.config_handler.get_connection_settings()
        self.ser = serial.Serial(
            port=conn_settings['port'],
            baudrate=conn_settings['baudrate'],
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=conn_settings['timeout']
        )

        self.ui.rock_btn.clicked.connect(lambda: self.make_move("rock"))
        self.ui.paper_btn.clicked.connect(lambda: self.make_move("paper"))
        self.ui.scissors_btn.clicked.connect(lambda: self.make_move("scissors"))

        self.ui.reset_statistic_btn.clicked.connect(self.reset_stats)
        self.ui.show_statistic_btn.clicked.connect(self.show_statistics)

        self.update_stats_display()

    def update_stats_display(self):
        stats = self.config_handler.get_stats()
        self.ui.games_played_counter_lb.setText(str(stats['games_played']))
        self.ui.first_choice_player_score_lb.setText(str(stats['player_score']))
        self.ui.second_choice_player_score_lb.setText(str(stats['server_score']))

    def show_statistics(self):
        stats = self.config_handler.get_stats()
        self.stat_window = StatisticWindow(stats)
        self.stat_window.show()

    def reset_stats(self):
        self.config_handler.reset_stats()
        self.update_stats_display()

    def update_choice_icons(self, player_choice, server_choice):
        src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root_dir = os.path.dirname(src_dir)
        media_dir = os.path.join(root_dir, "media")

        player_image_path = os.path.join(media_dir, f"{player_choice}.png")
        player_pixmap = QPixmap(player_image_path)
        player_pixmap = player_pixmap.scaled(512, 512)
        self.ui.first_choice_icon_lb.setPixmap(player_pixmap)

        server_image_path = os.path.join(media_dir, f"{server_choice}.png")
        server_pixmap = QPixmap(server_image_path)
        server_pixmap = server_pixmap.scaled(512, 512)
        self.ui.second_choice_icon_lb.setPixmap(server_pixmap)

    def make_move(self, choice):
        self.ser.reset_input_buffer()

        message = {"move": choice}
        self.ser.write(json.dumps(message).encode('utf-8') + b'\n')
        print(f"Sent: {json.dumps(message)}")

        time.sleep(0.1)

        # Read the response
        try:
            response = self.ser.readline().decode('utf-8').strip()
            print(f"Received: {response}")

            if response:
                response_data = json.loads(response)
                server_choice = response_data.get("server_move", "unknown")
                result = response_data.get("result", "Error occurred")

                self.update_choice_icons(choice, server_choice)

                self.ui.result_lb.setText(result)

                self.config_handler.update_game_stats(choice, server_choice, result)
                self.update_stats_display()

            else:
                self.ui.result_lb.setText("Error: No response from server")

        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            self.ui.result_lb.setText("Error: Invalid server response")
        except Exception as e:
            print(f"Error: {e}")
            self.ui.result_lb.setText("Error: Communication error")

    def closeEvent(self, event):
        self.ser.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())