from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
import sys, serial, json, time, random,  os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.common.config_handler import ConfigHandler
from ui_main import Ui_MainWindow
from ui_statistic import Ui_Dialog


class GameSession:
    def __init__(self):
        self.games_played = 0
        self.player_score = 0
        self.server_score = 0

    def update_stats(self, result):
        self.games_played += 1
        if result == "You win!" or result == "Player A wins!":
            self.player_score += 1
        elif result == "Server wins!" or result == "Player B wins!":
            self.server_score += 1


class StatisticWindow(QWidget):
    def __init__(self, stats):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Game Statistics")
        self.config_handler = ConfigHandler()

        self.ui.statistic_type_cb.addItems(["Human vs AI", "PVP", "AI vs AI"])
        self.ui.statistic_type_cb.currentTextChanged.connect(self.on_statistic_type_changed)

        current_mode = self.config_handler.get_game_settings()['default_mode']
        initial_stat_type = "PVP" if current_mode == "man_vs_man" else ("Human vs AI" if current_mode == "man_vs_ai"
                                                                        else "AI vs AI")
        # Set the combo box without triggering the signal
        self.ui.statistic_type_cb.blockSignals(True)
        self.ui.statistic_type_cb.setCurrentText(initial_stat_type)
        self.ui.statistic_type_cb.blockSignals(False)

        if current_mode == "man_vs_ai":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_human_vs_ai)
        elif current_mode == "man_vs_man":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_man_vs_man)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ai_vs_ai)

        self.update_stats(current_mode)

    def on_statistic_type_changed(self, stat_type):
        mode = ("man_vs_man" if stat_type == "PVP" else "man_vs_ai" if stat_type == "Human vs AI" else "ai_vs_ai")

        if mode == "man_vs_ai":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_human_vs_ai)
        elif mode == "man_vs_man":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_man_vs_man)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ai_vs_ai)

        self.update_stats(mode)

    def update_stats(self, mode):
        stats = self.config_handler.get_stats(mode)

        if mode == "man_vs_ai":
            games_played = stats['games_played']
            player_score = stats['player_score']
            server_score = stats['server_score']
            win_rate = (player_score / games_played * 100 if games_played > 0 else 0)

            self.ui.total_games_played_counter_lb.setText(str(games_played))
            self.ui.player_wins_counter_lb.setText(str(player_score))
            self.ui.ai_wins_counter_lb.setText(str(server_score))
            self.ui.win_rate_value_lb.setText(f"{win_rate:.1f}%")
        elif mode == "ai_vs_ai":
            ai_games_played = stats['ai_games_played']
            ai_client_score = stats['ai_client_score']
            ai_server_score = stats['ai_server_score']
            win_rate = (ai_client_score / ai_games_played * 100 if ai_games_played > 0 else 0)

            self.ui.total_games_ai_vs_ai_played_counter_lb.setText(str(ai_games_played))
            self.ui.ai_client_wins_counter_lb.setText(str(ai_client_score))
            self.ui.ai_server_wins_counter_lb.setText(str(ai_server_score))
            self.ui.win_rate_ai_vs_ai_value_lb.setText(f"{win_rate:.1f}%")
        else:
            pvp_games_played = stats['pvp_games_played']
            player_a_score = stats['player_a_score']
            player_b_score = stats['player_b_score']
            win_rate = (player_a_score / pvp_games_played * 100 if pvp_games_played > 0 else 0)

            self.ui.total_games_pa_vs_pb_played_counter_lb.setText(str(pvp_games_played))
            self.ui.player_a_wins_counter_lb .setText(str(player_a_score))
            self.ui.player_b_wins_counter_lb.setText(str(player_b_score))
            self.ui.win_rate_pa_vs_pb_value_lb.setText(f"{win_rate:.1f}%")


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rock Paper Scissors")

        self.config_handler = ConfigHandler()
        self.game_session = GameSession()

        conn_settings = self.config_handler.get_connection_settings()
        self.ser = serial.Serial(
            port=conn_settings['port'],
            baudrate=conn_settings['baudrate'],
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=conn_settings['timeout']
        )

        self.ai_timer = QtCore.QTimer()
        self.ai_timer.timeout.connect(self.make_ai_move)

        self.ui.rock_btn.clicked.connect(lambda: self.make_move("rock"))
        self.ui.paper_btn.clicked.connect(lambda: self.make_move("paper"))
        self.ui.scissors_btn.clicked.connect(lambda: self.make_move("scissors"))
        self.ui.reset_statistic_btn.clicked.connect(self.reset_all_stats)
        self.ui.show_statistic_btn.clicked.connect(self.show_statistics)
        self.ui.stop_btn.clicked.connect(self.stop_ai_game)

        self.ui.difficulty_combo.blockSignals(True)
        self.ui.game_mode_combo.blockSignals(True)
        self.setup_combo_boxes()
        self.ui.difficulty_combo.blockSignals(False)
        self.ui.game_mode_combo.blockSignals(False)

        self.ui.game_mode_combo.currentTextChanged.connect(self.on_game_mode_changed)
        self.ui.difficulty_combo.currentTextChanged.connect(self.on_difficulty_changed)

        self.update_stats_display()
        self.ui.stop_btn.setVisible(False)

        current_mode = self.config_handler.get_game_settings()['default_mode']
        if current_mode == "man_vs_ai":
            self.ui.first_choice_player_name_lb.setText("You")
            self.ui.second_choice_player_name_lb.setText("AI")
            self.ui.difficulty_combo.setVisible(True)
        elif current_mode == "man_vs_man":
            self.ui.first_choice_player_name_lb.setText("Player A")
            self.ui.second_choice_player_name_lb.setText("Player B")
            self.ui.difficulty_combo.setVisible(False)
        else:
            self.ui.first_choice_player_name_lb.setText("AI")
            self.ui.second_choice_player_name_lb.setText("AI")
            self.ui.stop_btn.setVisible(True)
            self.ui.stop_btn.setVisible(True)
            self.ui.rock_btn.setEnabled(False)
            self.ui.paper_btn.setEnabled(False)
            self.ui.scissors_btn.setEnabled(False)
            self.ui.difficulty_combo.setVisible(True)
            self.start_ai_game()

    def show_statistics(self):
        stats = self.config_handler.get_stats()
        self.stat_window = StatisticWindow(stats)
        self.stat_window.show()

    def update_stats_display(self):
        self.ui.games_played_counter_lb.setText(str(self.game_session.games_played))
        self.ui.first_choice_player_score_lb.setText(str(self.game_session.player_score))
        self.ui.second_choice_player_score_lb.setText(str(self.game_session.server_score))

    def reset_all_stats(self):
        self.config_handler.reset_stats()
        self.game_session = GameSession()
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

    def setup_combo_boxes(self):
        game_modes = ["Human vs AI", "PVP", "AI vs AI"]
        self.ui.game_mode_combo.addItems(game_modes)
        current_mode = self.config_handler.get_game_settings()['default_mode']
        if current_mode == "man_vs_ai":
            self.ui.game_mode_combo.setCurrentText("Human vs AI")
        elif current_mode == "man_vs_man":
            self.ui.game_mode_combo.setCurrentText("PVP")
        else:
            self.ui.game_mode_combo.setCurrentText("AI vs AI")

        difficulty_levels = ["Easy", "Medium", "Hard"]
        self.ui.difficulty_combo.addItems(difficulty_levels)
        current_difficulty = self.config_handler.get_ai_settings()['difficulty']
        self.ui.difficulty_combo.setCurrentText(current_difficulty.capitalize())

    def on_game_mode_changed(self, mode):
        self.game_session = GameSession()
        self.update_stats_display()

        if mode == "AI vs AI":
            self.ui.stop_btn.setVisible(True)
            self.ui.rock_btn.setEnabled(False)
            self.ui.paper_btn.setEnabled(False)
            self.ui.scissors_btn.setEnabled(False)
            self.ui.first_choice_player_name_lb.setText("AI")
            self.ui.second_choice_player_name_lb.setText("AI")
            self.ui.difficulty_combo.setVisible(True)
            self.start_ai_game()
        elif mode == "PVP":
            self.ui.stop_btn.setVisible(False)
            self.ui.rock_btn.setEnabled(True)
            self.ui.paper_btn.setEnabled(True)
            self.ui.scissors_btn.setEnabled(True)
            self.ui.first_choice_player_name_lb.setText("Player A")
            self.ui.second_choice_player_name_lb.setText("Player B")
            self.ui.difficulty_combo.setVisible(False)
            self.stop_ai_game()
        else:
            self.ui.stop_btn.setVisible(False)
            self.ui.rock_btn.setEnabled(True)
            self.ui.paper_btn.setEnabled(True)
            self.ui.scissors_btn.setEnabled(True)
            self.ui.first_choice_player_name_lb.setText("You")
            self.ui.second_choice_player_name_lb.setText("AI")
            self.ui.difficulty_combo.setVisible(True)
            self.stop_ai_game()

        mode_value = "man_vs_ai" if mode == "Human vs AI" else ("man_vs_man" if mode == "PVP" else "ai_vs_ai")
        self.config_handler.update_game_mode(mode_value)

    def on_difficulty_changed(self, difficulty):
        self.config_handler.update_difficulty(difficulty.lower())

    def make_ai_move(self):
        moves = ["rock", "paper", "scissors"]
        ai_move = random.choice(moves)
        self.make_move(ai_move)

    def start_ai_game(self):
        self.ai_timer.start(2000)

    def stop_ai_game(self):
        self.ai_timer.stop()
        current_mode = self.config_handler.get_game_settings()['default_mode']
        self.ui.stop_btn.setVisible(False)
        self.ui.game_mode_combo.setCurrentText(current_mode)

    def make_move(self, choice):
        self.ser.reset_input_buffer()

        current_mode = self.ui.game_mode_combo.currentText()
        game_mode = "man_vs_man" if current_mode == "PVP" else ("ai_vs_ai" if current_mode == "AI vs AI"
                                                                else "man_vs_ai")
        # Set appropriate timeout based on game mode
        original_timeout = self.ser.timeout
        if game_mode == "man_vs_man":
            self.ser.timeout = None  # Wait indefinitely for PvP mode

        message = {
            "move": choice,
            "difficulty": self.config_handler.get_ai_settings()['difficulty'],
            "game_mode": game_mode
        }
        self.ser.write(json.dumps(message).encode('utf-8') + b'\n')
        print(f"Sent: {json.dumps(message)}")

        if game_mode == "man_vs_man":
            self.ui.first_choice_icon_lb.clear()
            self.ui.first_choice_icon_lb.setText("Choice made!\nWaiting for Player B...")
            # Process events to ensure UI updates
            QApplication.processEvents()
        else:
            time.sleep(0.1)  # Short delay for other modes

        try:
            response = self.ser.readline().decode('utf-8').strip()
            print(f"Received: {response}")

            # Reset timeout to original value
            self.ser.timeout = original_timeout

            if response:
                response_data = json.loads(response)
                server_choice = response_data.get("server_move", "unknown")
                result = response_data.get("result", "Error occurred")

                self.update_choice_icons(choice, server_choice)
                self.ui.result_lb.setText(result)

                self.game_session.update_stats(result)
                self.config_handler.update_game_stats(choice, server_choice, result, game_mode)
                self.update_stats_display()
            else:
                self.ui.result_lb.setText("Error: No response from server")

        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            self.ui.result_lb.setText("Error: Invalid server response")
        except Exception as e:
            print(f"Error: {e}")
            self.ui.result_lb.setText("Error: Communication error")
        finally:
            # Ensure timeout is reset even if an error occurs
            self.ser.timeout = original_timeout

    def closeEvent(self, event):
        self.ser.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())