import unittest
from unittest.mock import Mock
import sys
import os
import configparser
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.server.server import GameServer
from src.common.config_handler import ConfigHandler

class MockSerial:
    def __init__(self, *args, **kwargs):
        self.write = Mock()
        self.read = Mock(return_value=b'')

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        # Замінюємо справжній Serial на наш mock
        GameServer.serial.Serial = MockSerial
        self.game = GameServer()

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameServer()

    def test_determine_winner_draw(self):
        result = self.game.determine_winner("rock", "rock")
        self.assertEqual(result, "Draw")

    def test_determine_winner_player_wins(self):
        result = self.game.determine_winner("rock", "scissors")
        self.assertEqual(result, "You win!")

    def test_determine_winner_server_wins(self):
        result = self.game.determine_winner("rock", "paper")
        self.assertEqual(result, "Server wins!")


class TestConfigHandler(unittest.TestCase):
    def setUp(self):
        # Створюємо тестовий конфіг файл
        self.test_config_dir = os.path.join(os.path.dirname(__file__), 'test_config')
        os.makedirs(self.test_config_dir, exist_ok=True)
        self.test_config_path = os.path.join(self.test_config_dir, 'test_config.ini')

        # Створюємо базовий конфіг для тестів
        config = configparser.ConfigParser()
        config['Connection'] = {
            'port': 'COM3',
            'baudrate': '115200',
            'timeout': '1'
        }
        config['GameSettings'] = {
            'save_stats': 'true',
            'default_mode': 'man_vs_ai'
        }
        config['GameState'] = {
            'player_score': '0',
            'server_score': '0',
            'games_played': '0'
        }

        with open(self.test_config_path, 'w') as configfile:
            config.write(configfile)

        self.config_handler = ConfigHandler(self.test_config_path)

    def test_load_config(self):
        # Перевіряємо чи правильно завантажуються налаштування з'єднання
        conn_settings = self.config_handler.get_connection_settings()
        self.assertEqual(conn_settings['port'], 'COM3')
        self.assertEqual(conn_settings['baudrate'], 115200)
        self.assertEqual(conn_settings['timeout'], 1)

    def test_get_game_settings(self):
        # Перевіряємо налаштування гри
        game_settings = self.config_handler.get_game_settings()
        self.assertTrue(game_settings['save_stats'])
        self.assertEqual(game_settings['default_mode'], 'man_vs_ai')

    def test_update_game_stats(self):
        # Тестуємо оновлення статистики
        self.config_handler.update_game_stats("rock", "scissors", "You win!")
        stats = self.config_handler.get_stats()
        self.assertEqual(stats['player_score'], 1)
        self.assertEqual(stats['server_score'], 0)
        self.assertEqual(stats['games_played'], 1)

    def test_reset_stats(self):
        # Тестуємо скидання статистики
        self.config_handler.update_game_stats("rock", "scissors", "You win!")
        self.config_handler.reset_stats()
        stats = self.config_handler.get_stats()
        self.assertEqual(stats['player_score'], 0)
        self.assertEqual(stats['server_score'], 0)
        self.assertEqual(stats['games_played'], 0)

    def tearDown(self):
        # Видаляємо тестовий конфіг після завершення тестів
        if os.path.exists(self.test_config_path):
            os.remove(self.test_config_path)
        if os.path.exists(self.test_config_dir):
            os.rmdir(self.test_config_dir)


if __name__ == '__main__':
    unittest.main()