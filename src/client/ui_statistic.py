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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)
import res_dialog_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 285)
        Dialog.setMinimumSize(QSize(400, 285))
        Dialog.setMaximumSize(QSize(400, 285))
        icon = QIcon()
        icon.addFile(u":/icons/media/statistics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: #8BC6EC;\n"
"background-image: linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);\n"
"font-family: Banshrift-Light;")
        self.main_statistic_frame = QFrame(Dialog)
        self.main_statistic_frame.setObjectName(u"main_statistic_frame")
        self.main_statistic_frame.setGeometry(QRect(20, 10, 361, 271))
        self.verticalLayout = QVBoxLayout(self.main_statistic_frame)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.total_games_played_frame = QFrame(self.main_statistic_frame)
        self.total_games_played_frame.setObjectName(u"total_games_played_frame")
        self.total_gemas_played_frame = QHBoxLayout(self.total_games_played_frame)
        self.total_gemas_played_frame.setSpacing(3)
        self.total_gemas_played_frame.setObjectName(u"total_gemas_played_frame")
        self.total_gemas_played_frame.setContentsMargins(1, 1, 1, 1)
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

        self.total_gemas_played_frame.addWidget(self.total_games_played_text_lb)

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

        self.total_gemas_played_frame.addWidget(self.total_games_played_counter_lb)


        self.verticalLayout.addWidget(self.total_games_played_frame)

        self.player_wins_frame = QFrame(self.main_statistic_frame)
        self.player_wins_frame.setObjectName(u"player_wins_frame")
        self.total_gemas_played_frame_2 = QHBoxLayout(self.player_wins_frame)
        self.total_gemas_played_frame_2.setSpacing(3)
        self.total_gemas_played_frame_2.setObjectName(u"total_gemas_played_frame_2")
        self.total_gemas_played_frame_2.setContentsMargins(1, 1, 1, 1)
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

        self.total_gemas_played_frame_2.addWidget(self.player_wins_text_lb)

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

        self.total_gemas_played_frame_2.addWidget(self.player_wins_counter_lb)


        self.verticalLayout.addWidget(self.player_wins_frame)

        self.ai_wins_frame = QFrame(self.main_statistic_frame)
        self.ai_wins_frame.setObjectName(u"ai_wins_frame")
        self.total_gemas_played_frame_3 = QHBoxLayout(self.ai_wins_frame)
        self.total_gemas_played_frame_3.setSpacing(3)
        self.total_gemas_played_frame_3.setObjectName(u"total_gemas_played_frame_3")
        self.total_gemas_played_frame_3.setContentsMargins(1, 1, 1, 1)
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

        self.total_gemas_played_frame_3.addWidget(self.ai_wins_text_lb)

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

        self.total_gemas_played_frame_3.addWidget(self.ai_wins_counter_lb)


        self.verticalLayout.addWidget(self.ai_wins_frame)

        self.win_rate_frame = QFrame(self.main_statistic_frame)
        self.win_rate_frame.setObjectName(u"win_rate_frame")
        self.total_gemas_played_frame_4 = QHBoxLayout(self.win_rate_frame)
        self.total_gemas_played_frame_4.setSpacing(3)
        self.total_gemas_played_frame_4.setObjectName(u"total_gemas_played_frame_4")
        self.total_gemas_played_frame_4.setContentsMargins(1, 1, 1, 1)
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

        self.total_gemas_played_frame_4.addWidget(self.win_rate_text_lb)

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

        self.total_gemas_played_frame_4.addWidget(self.win_rate_value_lb)


        self.verticalLayout.addWidget(self.win_rate_frame)


        self.retranslateUi(Dialog)

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
    # retranslateUi

