import configparser
import os
from pathlib import Path
from datetime import datetime

class ConfigHandler:
    def __init__(self, config_path=None):
        if config_path is None:
            # Визначаємо шлях до кореневої директорії проекту
            project_root = Path(__file__).parent.parent.parent.parent
            # Формуємо шлях до config.ini
            config_path = project_root / 'csad2425ki408maletsdo12' / 'config' / 'config.ini'

        self.config_path = str(config_path)
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        """Load configuration from file"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        self.config.read(self.config_path)

    def save_config(self):
        """Save configuration to file"""
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def get_connection_settings(self):
        """Get serial connection settings"""
        return {
            'port': self.config.get('Connection', 'port'),
            'baudrate': self.config.getint('Connection', 'baudrate'),
            'timeout': self.config.getint('Connection', 'timeout')
        }

    def get_game_settings(self):
        """Get game settings"""
        return {
            'save_stats': self.config.getboolean('GameSettings', 'save_stats'),
            'default_mode': self.config.get('GameSettings', 'default_mode')
        }

    def update_game_stats(self, player_move, server_move, result):
        """Update game statistics"""
        # Update scores
        if result == "You win!":
            player_score = self.config.getint('GameState', 'player_score') + 1
            self.config.set('GameState', 'player_score', str(player_score))
        elif result == "Server wins!":
            server_score = self.config.getint('GameState', 'server_score') + 1
            self.config.set('GameState', 'server_score', str(server_score))

        # Update games played
        games_played = self.config.getint('GameState', 'games_played') + 1
        self.config.set('GameState', 'games_played', str(games_played))

        # Update last game info
        self.config.set('LastGame', 'player_move', player_move)
        self.config.set('LastGame', 'server_move', server_move)
        self.config.set('LastGame', 'result', result)
        self.config.set('LastGame', 'timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        self.save_config()

    def get_stats(self):
        """Get game statistics"""
        return {
            'player_score': self.config.getint('GameState', 'player_score'),
            'server_score': self.config.getint('GameState', 'server_score'),
            'games_played': self.config.getint('GameState', 'games_played')
        }

    def reset_stats(self):
        """Reset game statistics"""
        self.config.set('GameState', 'player_score', '0')
        self.config.set('GameState', 'server_score', '0')
        self.config.set('GameState', 'games_played', '0')
        self.save_config()