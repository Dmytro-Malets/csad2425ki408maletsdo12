"""!
@file config_handler.py
@brief Handles configuration and statistics persistence for the Rock-Paper-Scissors game.

This file provides methods to read, write, and update game configuration settings and
statistics, enabling persistent storage of settings between game sessions.

@details Configurations are stored in a `.ini` format and managed using Python's
ConfigParser module. The configuration includes game settings, AI difficulty, connection
parameters, and game statistics.

@author Dmytro Malets
@date 2024-11-04
"""

import configparser
import os
from pathlib import Path
from datetime import datetime


class ConfigHandler:
    """!
    @brief Configuration handler for managing game settings and statistics.

    Provides methods to read, update, and save configuration and game statistics
    from a `.ini` file, allowing the game to persist settings across sessions.
    """
    def __init__(self, config_path=None):
        """!
        @brief Initializes the ConfigHandler with the path to the configuration file.

        Loads the configuration file and raises an error if the file is not found.

        @param config_path Optional path to the configuration file. Defaults to
               `<project_root>/config/config.ini` if not specified.
        @throws FileNotFoundError If the configuration file does not exist.
        """
        if config_path is None:
            project_root = Path(__file__).parent.parent.parent
            config_path = project_root / 'config' / 'config.ini'
            if not config_path.exists():
                raise FileNotFoundError(f"Config file not found at: {config_path}")

        self.config_path = str(config_path)
        self.config = configparser.ConfigParser()
        self.load_config()

    def get_ai_settings(self):
        """!
        @brief Retrieve AI settings, including difficulty and strategy.

        Reads and returns AI-related settings from the configuration file.

        @return dict A dictionary containing AI difficulty level and strategy.
        """
        return {
            'difficulty': self.config.get('AISettings', 'difficulty'),
            'strategy': self.config.get('AISettings', 'strategy')
        }

    def update_game_mode(self, mode):
        """!
        @brief Update the default game mode setting in the configuration.

        Saves the specified game mode as the default mode for future sessions.

        @param mode The game mode to set as default (e.g., "man_vs_ai", "man_vs_man", "ai_vs_ai").
        """
        self.config.set('GameSettings', 'default_mode', mode)
        self.save_config()

    def update_difficulty(self, difficulty):
        """!
        @brief Update the AI difficulty setting in the configuration.

        Changes the AI difficulty level and saves it in the configuration file.

        @param difficulty The AI difficulty level to set (e.g., "easy", "medium", "hard").
        """
        self.config.set('AISettings', 'difficulty', difficulty)
        self.save_config()

    def load_config(self):
        """!
        @brief Load configuration from the `.ini` file.

        Reads the configuration file and populates the internal `config` object with
        settings, allowing access to different configuration sections and values.

        @throws FileNotFoundError If the configuration file is not found at `config_path`.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        self.config.read(self.config_path)
        # print(f"Loaded config from: {self.config_path}")

    def save_config(self):
        """!
        @brief Save the current configuration to the `.ini` file.

        Writes any modified settings in the `config` object back to the configuration file,
        ensuring persistent storage of updates.
        """
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def get_connection_settings(self):
        """!
        @brief Retrieve serial connection settings from the configuration.

        Provides the serial connection parameters required to establish communication
        between client and server.

        @return dict A dictionary containing connection settings, including `port`,
                `baudrate`, and `timeout`.
        """
        return {
            'port': self.config.get('Connection', 'port'),
            'baudrate': self.config.getint('Connection', 'baudrate'),
            'timeout': self.config.getint('Connection', 'timeout')
        }

    def get_game_settings(self):
        """!
        @brief Retrieve general game settings from the configuration.

        Returns game settings such as the default game mode and whether statistics
        should be saved.

        @return dict A dictionary with settings `save_stats` (bool) and `default_mode` (str).
        """
        return {
            'save_stats': self.config.getboolean('GameSettings', 'save_stats'),
            'default_mode': self.config.get('GameSettings', 'default_mode')
        }

    def update_game_stats(self, player_move, server_move, result, game_mode="man_vs_ai"):
        """!
        @brief Update and save game statistics based on the outcome of a game round.

        Modifies statistics based on the result of a game round and stores updated values in
        the configuration file. Supports different game modes with distinct statistics for
        each mode (e.g., PvP and AI modes).

        @param player_move The move chosen by the player (e.g., "rock", "paper", "scissors").
        @param server_move The move chosen by the server (e.g., "rock", "paper", "scissors").
        @param result The outcome of the game round (e.g., "You win!", "Server wins!").
        @param game_mode The game mode in which the round was played (default: "man_vs_ai").
        """
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
        """!
        @brief Retrieve game statistics based on the specified game mode.

        Provides statistics relevant to the requested game mode, including scores
        and total games played.

        @param mode The game mode for which to retrieve statistics (e.g., "man_vs_ai",
               "man_vs_man", "ai_vs_ai"). Defaults to "man_vs_ai".
        @return dict A dictionary containing relevant statistics based on the mode.
        """
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
        """!
        @brief Reset game statistics to initial values for the specified mode.

        Resets scores and game counts to zero for either specific modes or all modes.

        @param mode The game mode(s) to reset ("man_vs_ai", "man_vs_man", "ai_vs_ai",
               or "both" to reset all). Defaults to "both".
        """
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