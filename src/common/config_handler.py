import configparser
import os
from pathlib import Path
from datetime import datetime


class ConfigHandler:
    def __init__(self, config_path=None):
        if config_path is None:
            project_root = Path(__file__).parent.parent.parent
            config_path = project_root / 'config' / 'config.ini'
            if not config_path.exists():
                raise FileNotFoundError(f"Config file not found at: {config_path}")

        self.config_path = str(config_path)
        self.config = configparser.ConfigParser()
        self.load_config()

    def get_ai_settings(self):
        """Get AI settings"""
        return {
            'difficulty': self.config.get('AISettings', 'difficulty'),
            'strategy': self.config.get('AISettings', 'strategy')
        }

    def update_game_mode(self, mode):
        """Update game mode setting"""
        self.config.set('GameSettings', 'default_mode', mode)
        self.save_config()

    def update_difficulty(self, difficulty):
        """Update AI difficulty setting"""
        self.config.set('AISettings', 'difficulty', difficulty)
        self.save_config()

    def load_config(self):
        """Load configuration from file"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        self.config.read(self.config_path)
        # print(f"Loaded config from: {self.config_path}")

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

    def update_game_stats(self, player_move, server_move, result, game_mode="man_vs_ai"):
        """Update game statistics based on game mode"""
        if game_mode == "man_vs_ai":
            if result == "You win!":
                player_score = self.config.getint('GameState', 'player_score') + 1
                self.config.set('GameState', 'player_score', str(player_score))
            elif result == "Server wins!":
                server_score = self.config.getint('GameState', 'server_score') + 1
                self.config.set('GameState', 'server_score', str(server_score))
            games_played = self.config.getint('GameState', 'games_played') + 1
            self.config.set('GameState', 'games_played', str(games_played))
        elif game_mode == "man_vs_man":
            if result == "Player A wins!":
                player_a_score = self.config.getint('GameState', 'player_a_score', fallback=0) + 1
                self.config.set('GameState', 'player_a_score', str(player_a_score))
            elif result == "Player B wins!":
                player_b_score = self.config.getint('GameState', 'player_b_score', fallback=0) + 1
                self.config.set('GameState', 'player_b_score', str(player_b_score))
            pvp_games_played = self.config.getint('GameState', 'pvp_games_played', fallback=0) + 1
            self.config.set('GameState', 'pvp_games_played', str(pvp_games_played))
        else:
            if result == "You win!":
                ai_client_score = self.config.getint('GameState', 'ai_client_score') + 1
                self.config.set('GameState', 'ai_client_score', str(ai_client_score))
            elif result == "Server wins!":
                ai_server_score = self.config.getint('GameState', 'ai_server_score') + 1
                self.config.set('GameState', 'ai_server_score', str(ai_server_score))
            ai_games_played = self.config.getint('GameState', 'ai_games_played') + 1
            self.config.set('GameState', 'ai_games_played', str(ai_games_played))

        self.config.set('LastGame', 'player_move', player_move)
        self.config.set('LastGame', 'server_move', server_move)
        self.config.set('LastGame', 'result', result)
        self.config.set('LastGame', 'timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        self.save_config()

    def get_stats(self, mode="man_vs_ai"):
        """Get game statistics based on mode"""
        if mode == "man_vs_ai":
            return {
                'player_score': self.config.getint('GameState', 'player_score'),
                'server_score': self.config.getint('GameState', 'server_score'),
                'games_played': self.config.getint('GameState', 'games_played')
            }
        elif mode == "man_vs_man":
            return {
                'player_a_score': self.config.getint('GameState', 'player_a_score', fallback=0),
                'player_b_score': self.config.getint('GameState', 'player_b_score', fallback=0),
                'pvp_games_played': self.config.getint('GameState', 'pvp_games_played', fallback=0)
            }
        else:
            return {
                'ai_client_score': self.config.getint('GameState', 'ai_client_score'),
                'ai_server_score': self.config.getint('GameState', 'ai_server_score'),
                'ai_games_played': self.config.getint('GameState', 'ai_games_played')
            }

    def reset_stats(self, mode="both"):
        """Reset game statistics for specified mode"""
        if mode in ["both", "man_vs_ai"]:
            self.config.set('GameState', 'player_score', '0')
            self.config.set('GameState', 'server_score', '0')
            self.config.set('GameState', 'games_played', '0')

        if mode in ["both", "man_vs_man"]:
            self.config.set('GameState', 'player_a_score', '0')
            self.config.set('GameState', 'player_b_score', '0')
            self.config.set('GameState', 'pvp_games_played', '0')

        if mode in ["both", "ai_vs_ai"]:
            self.config.set('GameState', 'ai_client_score', '0')
            self.config.set('GameState', 'ai_server_score', '0')
            self.config.set('GameState', 'ai_games_played', '0')

        self.save_config()