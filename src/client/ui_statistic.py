# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_statistic.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import res_dialog_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 350)
        Dialog.setMinimumSize(QSize(400, 350))
        Dialog.setMaximumSize(QSize(400, 350))
        icon = QIcon()
        icon.addFile(u":/icons/statistics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(0.950000000000000)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(30, 95, 50, 255), stop:0.427447 rgba(30, 85, 85, 255), stop:1 rgba(30, 40, 100, 255));\n"
"font-family: Banshrift-Light;")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 52, 381, 291))
        self.stackedWidget.setMaximumSize(QSize(391, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_human_vs_ai = QWidget()
        self.page_human_vs_ai.setObjectName(u"page_human_vs_ai")
        self.main_statistic_frame = QFrame(self.page_human_vs_ai)
        self.main_statistic_frame.setObjectName(u"main_statistic_frame")
        self.main_statistic_frame.setGeometry(QRect(10, 10, 361, 271))
        self.main_statistic_frame.setStyleSheet(u"background-color: none;")
        self.verticalLayout_2 = QVBoxLayout(self.main_statistic_frame)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.total_games_played_frame = QFrame(self.main_statistic_frame)
        self.total_games_played_frame.setObjectName(u"total_games_played_frame")
        self.total_gemas_played_frame_5 = QHBoxLayout(self.total_games_played_frame)
        self.total_gemas_played_frame_5.setSpacing(3)
        self.total_gemas_played_frame_5.setObjectName(u"total_gemas_played_frame_5")
        self.total_gemas_played_frame_5.setContentsMargins(1, 1, 1, 1)
        self.total_games_played_text_lb = QLabel(self.total_games_played_frame)
        self.total_games_played_text_lb.setObjectName(u"total_games_played_text_lb")
        self.total_games_played_text_lb.setMinimumSize(QSize(180, 30))
        self.total_games_played_text_lb.setMaximumSize(QSize(180, 30))
        font = QFont()
        font.setFamilies([u"Banshrift-Light"])
        font.setPointSize(14)
        self.total_games_played_text_lb.setFont(font)
        self.total_games_played_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.total_games_played_text_lb.setTextFormat(Qt.RichText)
        self.total_games_played_text_lb.setScaledContents(False)
        self.total_games_played_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_5.addWidget(self.total_games_played_text_lb)

        self.total_games_played_counter_lb = QLabel(self.total_games_played_frame)
        self.total_games_played_counter_lb.setObjectName(u"total_games_played_counter_lb")
        self.total_games_played_counter_lb.setMinimumSize(QSize(70, 30))
        self.total_games_played_counter_lb.setMaximumSize(QSize(70, 30))
        font1 = QFont()
        font1.setFamilies([u"Banshrift-Light"])
        font1.setPointSize(13)
        self.total_games_played_counter_lb.setFont(font1)
        self.total_games_played_counter_lb.setToolTipDuration(-1)
        self.total_games_played_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.total_games_played_counter_lb.setTextFormat(Qt.RichText)
        self.total_games_played_counter_lb.setScaledContents(False)
        self.total_games_played_counter_lb.setAlignment(Qt.AlignCenter)
        self.total_games_played_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_5.addWidget(self.total_games_played_counter_lb)


        self.verticalLayout_2.addWidget(self.total_games_played_frame)

        self.player_wins_frame = QFrame(self.main_statistic_frame)
        self.player_wins_frame.setObjectName(u"player_wins_frame")
        self.total_gemas_played_frame_6 = QHBoxLayout(self.player_wins_frame)
        self.total_gemas_played_frame_6.setSpacing(3)
        self.total_gemas_played_frame_6.setObjectName(u"total_gemas_played_frame_6")
        self.total_gemas_played_frame_6.setContentsMargins(1, 1, 1, 1)
        self.player_wins_text_lb = QLabel(self.player_wins_frame)
        self.player_wins_text_lb.setObjectName(u"player_wins_text_lb")
        self.player_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.player_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.player_wins_text_lb.setFont(font)
        self.player_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.player_wins_text_lb.setTextFormat(Qt.RichText)
        self.player_wins_text_lb.setScaledContents(False)
        self.player_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_6.addWidget(self.player_wins_text_lb)

        self.player_wins_counter_lb = QLabel(self.player_wins_frame)
        self.player_wins_counter_lb.setObjectName(u"player_wins_counter_lb")
        self.player_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.player_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.player_wins_counter_lb.setFont(font1)
        self.player_wins_counter_lb.setToolTipDuration(-1)
        self.player_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.player_wins_counter_lb.setTextFormat(Qt.RichText)
        self.player_wins_counter_lb.setScaledContents(False)
        self.player_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.player_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_6.addWidget(self.player_wins_counter_lb)


        self.verticalLayout_2.addWidget(self.player_wins_frame)

        self.ai_wins_frame = QFrame(self.main_statistic_frame)
        self.ai_wins_frame.setObjectName(u"ai_wins_frame")
        self.total_gemas_played_frame_7 = QHBoxLayout(self.ai_wins_frame)
        self.total_gemas_played_frame_7.setSpacing(3)
        self.total_gemas_played_frame_7.setObjectName(u"total_gemas_played_frame_7")
        self.total_gemas_played_frame_7.setContentsMargins(1, 1, 1, 1)
        self.ai_wins_text_lb = QLabel(self.ai_wins_frame)
        self.ai_wins_text_lb.setObjectName(u"ai_wins_text_lb")
        self.ai_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.ai_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.ai_wins_text_lb.setFont(font)
        self.ai_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.ai_wins_text_lb.setTextFormat(Qt.RichText)
        self.ai_wins_text_lb.setScaledContents(False)
        self.ai_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_7.addWidget(self.ai_wins_text_lb)

        self.ai_wins_counter_lb = QLabel(self.ai_wins_frame)
        self.ai_wins_counter_lb.setObjectName(u"ai_wins_counter_lb")
        self.ai_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.ai_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.ai_wins_counter_lb.setFont(font1)
        self.ai_wins_counter_lb.setToolTipDuration(-1)
        self.ai_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.ai_wins_counter_lb.setTextFormat(Qt.RichText)
        self.ai_wins_counter_lb.setScaledContents(False)
        self.ai_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.ai_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_7.addWidget(self.ai_wins_counter_lb)


        self.verticalLayout_2.addWidget(self.ai_wins_frame)

        self.win_rate_frame = QFrame(self.main_statistic_frame)
        self.win_rate_frame.setObjectName(u"win_rate_frame")
        self.total_gemas_played_frame_8 = QHBoxLayout(self.win_rate_frame)
        self.total_gemas_played_frame_8.setSpacing(3)
        self.total_gemas_played_frame_8.setObjectName(u"total_gemas_played_frame_8")
        self.total_gemas_played_frame_8.setContentsMargins(1, 1, 1, 1)
        self.win_rate_text_lb = QLabel(self.win_rate_frame)
        self.win_rate_text_lb.setObjectName(u"win_rate_text_lb")
        self.win_rate_text_lb.setMinimumSize(QSize(180, 30))
        self.win_rate_text_lb.setMaximumSize(QSize(180, 30))
        self.win_rate_text_lb.setFont(font)
        self.win_rate_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.win_rate_text_lb.setTextFormat(Qt.RichText)
        self.win_rate_text_lb.setScaledContents(False)
        self.win_rate_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_8.addWidget(self.win_rate_text_lb)

        self.win_rate_value_lb = QLabel(self.win_rate_frame)
        self.win_rate_value_lb.setObjectName(u"win_rate_value_lb")
        self.win_rate_value_lb.setMinimumSize(QSize(70, 30))
        self.win_rate_value_lb.setMaximumSize(QSize(70, 30))
        self.win_rate_value_lb.setFont(font1)
        self.win_rate_value_lb.setToolTipDuration(-1)
        self.win_rate_value_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.win_rate_value_lb.setTextFormat(Qt.RichText)
        self.win_rate_value_lb.setScaledContents(False)
        self.win_rate_value_lb.setAlignment(Qt.AlignCenter)
        self.win_rate_value_lb.setIndent(-1)

        self.total_gemas_played_frame_8.addWidget(self.win_rate_value_lb)


        self.verticalLayout_2.addWidget(self.win_rate_frame)

        self.stackedWidget.addWidget(self.page_human_vs_ai)
        self.page_ai_vs_ai = QWidget()
        self.page_ai_vs_ai.setObjectName(u"page_ai_vs_ai")
        self.main_statistic_frame_2 = QFrame(self.page_ai_vs_ai)
        self.main_statistic_frame_2.setObjectName(u"main_statistic_frame_2")
        self.main_statistic_frame_2.setGeometry(QRect(10, 10, 361, 271))
        self.main_statistic_frame_2.setStyleSheet(u"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.main_statistic_frame_2)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.total_games_ai_vs_ai_played_frame = QFrame(self.main_statistic_frame_2)
        self.total_games_ai_vs_ai_played_frame.setObjectName(u"total_games_ai_vs_ai_played_frame")
        self.total_gemas_played_frame_17 = QHBoxLayout(self.total_games_ai_vs_ai_played_frame)
        self.total_gemas_played_frame_17.setSpacing(3)
        self.total_gemas_played_frame_17.setObjectName(u"total_gemas_played_frame_17")
        self.total_gemas_played_frame_17.setContentsMargins(1, 1, 1, 1)
        self.total_games_ai_vs_ai_played_text_lb = QLabel(self.total_games_ai_vs_ai_played_frame)
        self.total_games_ai_vs_ai_played_text_lb.setObjectName(u"total_games_ai_vs_ai_played_text_lb")
        self.total_games_ai_vs_ai_played_text_lb.setMinimumSize(QSize(180, 30))
        self.total_games_ai_vs_ai_played_text_lb.setMaximumSize(QSize(180, 30))
        self.total_games_ai_vs_ai_played_text_lb.setFont(font)
        self.total_games_ai_vs_ai_played_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.total_games_ai_vs_ai_played_text_lb.setTextFormat(Qt.RichText)
        self.total_games_ai_vs_ai_played_text_lb.setScaledContents(False)
        self.total_games_ai_vs_ai_played_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_17.addWidget(self.total_games_ai_vs_ai_played_text_lb)

        self.total_games_ai_vs_ai_played_counter_lb = QLabel(self.total_games_ai_vs_ai_played_frame)
        self.total_games_ai_vs_ai_played_counter_lb.setObjectName(u"total_games_ai_vs_ai_played_counter_lb")
        self.total_games_ai_vs_ai_played_counter_lb.setMinimumSize(QSize(70, 30))
        self.total_games_ai_vs_ai_played_counter_lb.setMaximumSize(QSize(70, 30))
        self.total_games_ai_vs_ai_played_counter_lb.setFont(font1)
        self.total_games_ai_vs_ai_played_counter_lb.setToolTipDuration(-1)
        self.total_games_ai_vs_ai_played_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.total_games_ai_vs_ai_played_counter_lb.setTextFormat(Qt.RichText)
        self.total_games_ai_vs_ai_played_counter_lb.setScaledContents(False)
        self.total_games_ai_vs_ai_played_counter_lb.setAlignment(Qt.AlignCenter)
        self.total_games_ai_vs_ai_played_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_17.addWidget(self.total_games_ai_vs_ai_played_counter_lb)


        self.verticalLayout_5.addWidget(self.total_games_ai_vs_ai_played_frame)

        self.ai_client_wins_frame = QFrame(self.main_statistic_frame_2)
        self.ai_client_wins_frame.setObjectName(u"ai_client_wins_frame")
        self.total_gemas_played_frame_18 = QHBoxLayout(self.ai_client_wins_frame)
        self.total_gemas_played_frame_18.setSpacing(3)
        self.total_gemas_played_frame_18.setObjectName(u"total_gemas_played_frame_18")
        self.total_gemas_played_frame_18.setContentsMargins(1, 1, 1, 1)
        self.ai_client_wins_text_lb = QLabel(self.ai_client_wins_frame)
        self.ai_client_wins_text_lb.setObjectName(u"ai_client_wins_text_lb")
        self.ai_client_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.ai_client_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.ai_client_wins_text_lb.setFont(font)
        self.ai_client_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.ai_client_wins_text_lb.setTextFormat(Qt.RichText)
        self.ai_client_wins_text_lb.setScaledContents(False)
        self.ai_client_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_18.addWidget(self.ai_client_wins_text_lb)

        self.ai_client_wins_counter_lb = QLabel(self.ai_client_wins_frame)
        self.ai_client_wins_counter_lb.setObjectName(u"ai_client_wins_counter_lb")
        self.ai_client_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.ai_client_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.ai_client_wins_counter_lb.setFont(font1)
        self.ai_client_wins_counter_lb.setToolTipDuration(-1)
        self.ai_client_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.ai_client_wins_counter_lb.setTextFormat(Qt.RichText)
        self.ai_client_wins_counter_lb.setScaledContents(False)
        self.ai_client_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.ai_client_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_18.addWidget(self.ai_client_wins_counter_lb)


        self.verticalLayout_5.addWidget(self.ai_client_wins_frame)

        self.ai_server_wins_frame = QFrame(self.main_statistic_frame_2)
        self.ai_server_wins_frame.setObjectName(u"ai_server_wins_frame")
        self.total_gemas_played_frame_19 = QHBoxLayout(self.ai_server_wins_frame)
        self.total_gemas_played_frame_19.setSpacing(3)
        self.total_gemas_played_frame_19.setObjectName(u"total_gemas_played_frame_19")
        self.total_gemas_played_frame_19.setContentsMargins(1, 1, 1, 1)
        self.ai_server_wins_text_lb = QLabel(self.ai_server_wins_frame)
        self.ai_server_wins_text_lb.setObjectName(u"ai_server_wins_text_lb")
        self.ai_server_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.ai_server_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.ai_server_wins_text_lb.setFont(font)
        self.ai_server_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.ai_server_wins_text_lb.setTextFormat(Qt.RichText)
        self.ai_server_wins_text_lb.setScaledContents(False)
        self.ai_server_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_19.addWidget(self.ai_server_wins_text_lb)

        self.ai_server_wins_counter_lb = QLabel(self.ai_server_wins_frame)
        self.ai_server_wins_counter_lb.setObjectName(u"ai_server_wins_counter_lb")
        self.ai_server_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.ai_server_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.ai_server_wins_counter_lb.setFont(font1)
        self.ai_server_wins_counter_lb.setToolTipDuration(-1)
        self.ai_server_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.ai_server_wins_counter_lb.setTextFormat(Qt.RichText)
        self.ai_server_wins_counter_lb.setScaledContents(False)
        self.ai_server_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.ai_server_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_19.addWidget(self.ai_server_wins_counter_lb)


        self.verticalLayout_5.addWidget(self.ai_server_wins_frame)

        self.win_rate_ai_vs_ai_frame = QFrame(self.main_statistic_frame_2)
        self.win_rate_ai_vs_ai_frame.setObjectName(u"win_rate_ai_vs_ai_frame")
        self.total_gemas_played_frame_20 = QHBoxLayout(self.win_rate_ai_vs_ai_frame)
        self.total_gemas_played_frame_20.setSpacing(3)
        self.total_gemas_played_frame_20.setObjectName(u"total_gemas_played_frame_20")
        self.total_gemas_played_frame_20.setContentsMargins(1, 1, 1, 1)
        self.win_rate_ai_vs_ai_text_lb = QLabel(self.win_rate_ai_vs_ai_frame)
        self.win_rate_ai_vs_ai_text_lb.setObjectName(u"win_rate_ai_vs_ai_text_lb")
        self.win_rate_ai_vs_ai_text_lb.setMinimumSize(QSize(180, 30))
        self.win_rate_ai_vs_ai_text_lb.setMaximumSize(QSize(180, 30))
        self.win_rate_ai_vs_ai_text_lb.setFont(font)
        self.win_rate_ai_vs_ai_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.win_rate_ai_vs_ai_text_lb.setTextFormat(Qt.RichText)
        self.win_rate_ai_vs_ai_text_lb.setScaledContents(False)
        self.win_rate_ai_vs_ai_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_20.addWidget(self.win_rate_ai_vs_ai_text_lb)

        self.win_rate_ai_vs_ai_value_lb = QLabel(self.win_rate_ai_vs_ai_frame)
        self.win_rate_ai_vs_ai_value_lb.setObjectName(u"win_rate_ai_vs_ai_value_lb")
        self.win_rate_ai_vs_ai_value_lb.setMinimumSize(QSize(70, 30))
        self.win_rate_ai_vs_ai_value_lb.setMaximumSize(QSize(70, 30))
        self.win_rate_ai_vs_ai_value_lb.setFont(font1)
        self.win_rate_ai_vs_ai_value_lb.setToolTipDuration(-1)
        self.win_rate_ai_vs_ai_value_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.win_rate_ai_vs_ai_value_lb.setTextFormat(Qt.RichText)
        self.win_rate_ai_vs_ai_value_lb.setScaledContents(False)
        self.win_rate_ai_vs_ai_value_lb.setAlignment(Qt.AlignCenter)
        self.win_rate_ai_vs_ai_value_lb.setIndent(-1)

        self.total_gemas_played_frame_20.addWidget(self.win_rate_ai_vs_ai_value_lb)


        self.verticalLayout_5.addWidget(self.win_rate_ai_vs_ai_frame)

        self.stackedWidget.addWidget(self.page_ai_vs_ai)
        self.page_man_vs_man = QWidget()
        self.page_man_vs_man.setObjectName(u"page_man_vs_man")
        self.main_statistic_frame_3 = QFrame(self.page_man_vs_man)
        self.main_statistic_frame_3.setObjectName(u"main_statistic_frame_3")
        self.main_statistic_frame_3.setGeometry(QRect(10, 10, 361, 271))
        self.main_statistic_frame_3.setStyleSheet(u"background-color: none;")
        self.verticalLayout_6 = QVBoxLayout(self.main_statistic_frame_3)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.total_games_pa_vs_pb_played_frame = QFrame(self.main_statistic_frame_3)
        self.total_games_pa_vs_pb_played_frame.setObjectName(u"total_games_pa_vs_pb_played_frame")
        self.total_gemas_played_frame_21 = QHBoxLayout(self.total_games_pa_vs_pb_played_frame)
        self.total_gemas_played_frame_21.setSpacing(3)
        self.total_gemas_played_frame_21.setObjectName(u"total_gemas_played_frame_21")
        self.total_gemas_played_frame_21.setContentsMargins(1, 1, 1, 1)
        self.total_games_pa_vs_pb_played_text_lb = QLabel(self.total_games_pa_vs_pb_played_frame)
        self.total_games_pa_vs_pb_played_text_lb.setObjectName(u"total_games_pa_vs_pb_played_text_lb")
        self.total_games_pa_vs_pb_played_text_lb.setMinimumSize(QSize(180, 30))
        self.total_games_pa_vs_pb_played_text_lb.setMaximumSize(QSize(180, 30))
        self.total_games_pa_vs_pb_played_text_lb.setFont(font)
        self.total_games_pa_vs_pb_played_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.total_games_pa_vs_pb_played_text_lb.setTextFormat(Qt.RichText)
        self.total_games_pa_vs_pb_played_text_lb.setScaledContents(False)
        self.total_games_pa_vs_pb_played_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_21.addWidget(self.total_games_pa_vs_pb_played_text_lb)

        self.total_games_pa_vs_pb_played_counter_lb = QLabel(self.total_games_pa_vs_pb_played_frame)
        self.total_games_pa_vs_pb_played_counter_lb.setObjectName(u"total_games_pa_vs_pb_played_counter_lb")
        self.total_games_pa_vs_pb_played_counter_lb.setMinimumSize(QSize(70, 30))
        self.total_games_pa_vs_pb_played_counter_lb.setMaximumSize(QSize(70, 30))
        self.total_games_pa_vs_pb_played_counter_lb.setFont(font1)
        self.total_games_pa_vs_pb_played_counter_lb.setToolTipDuration(-1)
        self.total_games_pa_vs_pb_played_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.total_games_pa_vs_pb_played_counter_lb.setTextFormat(Qt.RichText)
        self.total_games_pa_vs_pb_played_counter_lb.setScaledContents(False)
        self.total_games_pa_vs_pb_played_counter_lb.setAlignment(Qt.AlignCenter)
        self.total_games_pa_vs_pb_played_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_21.addWidget(self.total_games_pa_vs_pb_played_counter_lb)


        self.verticalLayout_6.addWidget(self.total_games_pa_vs_pb_played_frame)

        self.player_a_wins_frame = QFrame(self.main_statistic_frame_3)
        self.player_a_wins_frame.setObjectName(u"player_a_wins_frame")
        self.total_gemas_played_frame_22 = QHBoxLayout(self.player_a_wins_frame)
        self.total_gemas_played_frame_22.setSpacing(3)
        self.total_gemas_played_frame_22.setObjectName(u"total_gemas_played_frame_22")
        self.total_gemas_played_frame_22.setContentsMargins(1, 1, 1, 1)
        self.player_a_wins_text_lb = QLabel(self.player_a_wins_frame)
        self.player_a_wins_text_lb.setObjectName(u"player_a_wins_text_lb")
        self.player_a_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.player_a_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.player_a_wins_text_lb.setFont(font)
        self.player_a_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.player_a_wins_text_lb.setTextFormat(Qt.RichText)
        self.player_a_wins_text_lb.setScaledContents(False)
        self.player_a_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_22.addWidget(self.player_a_wins_text_lb)

        self.player_a_wins_counter_lb = QLabel(self.player_a_wins_frame)
        self.player_a_wins_counter_lb.setObjectName(u"player_a_wins_counter_lb")
        self.player_a_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.player_a_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.player_a_wins_counter_lb.setFont(font1)
        self.player_a_wins_counter_lb.setToolTipDuration(-1)
        self.player_a_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.player_a_wins_counter_lb.setTextFormat(Qt.RichText)
        self.player_a_wins_counter_lb.setScaledContents(False)
        self.player_a_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.player_a_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_22.addWidget(self.player_a_wins_counter_lb)


        self.verticalLayout_6.addWidget(self.player_a_wins_frame)

        self.player_b_wins_frame = QFrame(self.main_statistic_frame_3)
        self.player_b_wins_frame.setObjectName(u"player_b_wins_frame")
        self.total_gemas_played_frame_23 = QHBoxLayout(self.player_b_wins_frame)
        self.total_gemas_played_frame_23.setSpacing(3)
        self.total_gemas_played_frame_23.setObjectName(u"total_gemas_played_frame_23")
        self.total_gemas_played_frame_23.setContentsMargins(1, 1, 1, 1)
        self.player_b_wins_text_lb = QLabel(self.player_b_wins_frame)
        self.player_b_wins_text_lb.setObjectName(u"player_b_wins_text_lb")
        self.player_b_wins_text_lb.setMinimumSize(QSize(180, 30))
        self.player_b_wins_text_lb.setMaximumSize(QSize(180, 30))
        self.player_b_wins_text_lb.setFont(font)
        self.player_b_wins_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.player_b_wins_text_lb.setTextFormat(Qt.RichText)
        self.player_b_wins_text_lb.setScaledContents(False)
        self.player_b_wins_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_23.addWidget(self.player_b_wins_text_lb)

        self.player_b_wins_counter_lb = QLabel(self.player_b_wins_frame)
        self.player_b_wins_counter_lb.setObjectName(u"player_b_wins_counter_lb")
        self.player_b_wins_counter_lb.setMinimumSize(QSize(70, 30))
        self.player_b_wins_counter_lb.setMaximumSize(QSize(70, 30))
        self.player_b_wins_counter_lb.setFont(font1)
        self.player_b_wins_counter_lb.setToolTipDuration(-1)
        self.player_b_wins_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.player_b_wins_counter_lb.setTextFormat(Qt.RichText)
        self.player_b_wins_counter_lb.setScaledContents(False)
        self.player_b_wins_counter_lb.setAlignment(Qt.AlignCenter)
        self.player_b_wins_counter_lb.setIndent(-1)

        self.total_gemas_played_frame_23.addWidget(self.player_b_wins_counter_lb)


        self.verticalLayout_6.addWidget(self.player_b_wins_frame)

        self.win_rate_pa_vs_pb_frame = QFrame(self.main_statistic_frame_3)
        self.win_rate_pa_vs_pb_frame.setObjectName(u"win_rate_pa_vs_pb_frame")
        self.total_gemas_played_frame_24 = QHBoxLayout(self.win_rate_pa_vs_pb_frame)
        self.total_gemas_played_frame_24.setSpacing(3)
        self.total_gemas_played_frame_24.setObjectName(u"total_gemas_played_frame_24")
        self.total_gemas_played_frame_24.setContentsMargins(1, 1, 1, 1)
        self.win_rate_pa_vs_pb_text_lb = QLabel(self.win_rate_pa_vs_pb_frame)
        self.win_rate_pa_vs_pb_text_lb.setObjectName(u"win_rate_pa_vs_pb_text_lb")
        self.win_rate_pa_vs_pb_text_lb.setMinimumSize(QSize(180, 30))
        self.win_rate_pa_vs_pb_text_lb.setMaximumSize(QSize(180, 30))
        self.win_rate_pa_vs_pb_text_lb.setFont(font)
        self.win_rate_pa_vs_pb_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.win_rate_pa_vs_pb_text_lb.setTextFormat(Qt.RichText)
        self.win_rate_pa_vs_pb_text_lb.setScaledContents(False)
        self.win_rate_pa_vs_pb_text_lb.setAlignment(Qt.AlignCenter)

        self.total_gemas_played_frame_24.addWidget(self.win_rate_pa_vs_pb_text_lb)

        self.win_rate_pa_vs_pb_value_lb = QLabel(self.win_rate_pa_vs_pb_frame)
        self.win_rate_pa_vs_pb_value_lb.setObjectName(u"win_rate_pa_vs_pb_value_lb")
        self.win_rate_pa_vs_pb_value_lb.setMinimumSize(QSize(70, 30))
        self.win_rate_pa_vs_pb_value_lb.setMaximumSize(QSize(70, 30))
        self.win_rate_pa_vs_pb_value_lb.setFont(font1)
        self.win_rate_pa_vs_pb_value_lb.setToolTipDuration(-1)
        self.win_rate_pa_vs_pb_value_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.win_rate_pa_vs_pb_value_lb.setTextFormat(Qt.RichText)
        self.win_rate_pa_vs_pb_value_lb.setScaledContents(False)
        self.win_rate_pa_vs_pb_value_lb.setAlignment(Qt.AlignCenter)
        self.win_rate_pa_vs_pb_value_lb.setIndent(-1)

        self.total_gemas_played_frame_24.addWidget(self.win_rate_pa_vs_pb_value_lb)


        self.verticalLayout_6.addWidget(self.win_rate_pa_vs_pb_frame)

        self.stackedWidget.addWidget(self.page_man_vs_man)
        self.statistic_type_cb = QComboBox(Dialog)
        self.statistic_type_cb.setObjectName(u"statistic_type_cb")
        self.statistic_type_cb.setGeometry(QRect(20, 11, 361, 31))
        font2 = QFont()
        font2.setFamilies([u"Banshrift-Light"])
        font2.setPointSize(11)
        self.statistic_type_cb.setFont(font2)
        self.statistic_type_cb.setStyleSheet(u"QComboBox{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius : 4px;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"}\n"
"")
        self.statistic_type_cb.setIconSize(QSize(17, 17))

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Statistic", None))
        self.total_games_played_text_lb.setText(QCoreApplication.translate("Dialog", u"Total games played", None))
        self.total_games_played_counter_lb.setText("")
        self.player_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"Player wins", None))
        self.player_wins_counter_lb.setText("")
        self.ai_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"AI wins", None))
        self.ai_wins_counter_lb.setText("")
        self.win_rate_text_lb.setText(QCoreApplication.translate("Dialog", u"Win rate", None))
        self.win_rate_value_lb.setText("")
        self.total_games_ai_vs_ai_played_text_lb.setText(QCoreApplication.translate("Dialog", u"Total games played", None))
        self.total_games_ai_vs_ai_played_counter_lb.setText("")
        self.ai_client_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"AI (client) wins", None))
        self.ai_client_wins_counter_lb.setText("")
        self.ai_server_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"AI (server) wins", None))
        self.ai_server_wins_counter_lb.setText("")
        self.win_rate_ai_vs_ai_text_lb.setText(QCoreApplication.translate("Dialog", u"Win rate", None))
        self.win_rate_ai_vs_ai_value_lb.setText("")
        self.total_games_pa_vs_pb_played_text_lb.setText(QCoreApplication.translate("Dialog", u"Total games played", None))
        self.total_games_pa_vs_pb_played_counter_lb.setText("")
        self.player_a_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"Player A wins", None))
        self.player_a_wins_counter_lb.setText("")
        self.player_b_wins_text_lb.setText(QCoreApplication.translate("Dialog", u"Player B wins", None))
        self.player_b_wins_counter_lb.setText("")
        self.win_rate_pa_vs_pb_text_lb.setText(QCoreApplication.translate("Dialog", u"Win rate", None))
        self.win_rate_pa_vs_pb_value_lb.setText("")
    # retranslateUi

