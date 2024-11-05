# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 600)
        MainWindow.setMinimumSize(QSize(812, 600))
        MainWindow.setMaximumSize(QSize(812, 600))
        font = QFont()
        font.setFamilies([u"Banshrift-Light"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/media/rock-paper-scissors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #8BC6EC;\n"
"background-image: linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);\n"
"font-family: Banshrift-Light;")
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result_lb = QLabel(self.centralwidget)
        self.result_lb.setObjectName(u"result_lb")
        self.result_lb.setGeometry(QRect(310, 550, 190, 35))
        self.result_lb.setMinimumSize(QSize(190, 35))
        self.result_lb.setMaximumSize(QSize(190, 35))
        font1 = QFont()
        font1.setFamilies([u"Banshrift-Light"])
        font1.setPointSize(17)
        self.result_lb.setFont(font1)
        self.result_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.result_lb.setTextFormat(Qt.RichText)
        self.result_lb.setScaledContents(False)
        self.result_lb.setAlignment(Qt.AlignCenter)
        self.main_lb = QLabel(self.centralwidget)
        self.main_lb.setObjectName(u"main_lb")
        self.main_lb.setGeometry(QRect(200, 10, 400, 35))
        self.main_lb.setMinimumSize(QSize(400, 35))
        self.main_lb.setMaximumSize(QSize(400, 35))
        font2 = QFont()
        font2.setFamilies([u"Banshrift-Light"])
        font2.setPointSize(20)
        font2.setBold(False)
        self.main_lb.setFont(font2)
        self.main_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.main_lb.setAlignment(Qt.AlignCenter)
        self.statistic_btns_frame = QFrame(self.centralwidget)
        self.statistic_btns_frame.setObjectName(u"statistic_btns_frame")
        self.statistic_btns_frame.setGeometry(QRect(660, 60, 131, 101))
        self.verticalLayout = QVBoxLayout(self.statistic_btns_frame)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.reset_statistic_btn = QPushButton(self.statistic_btns_frame)
        self.reset_statistic_btn.setObjectName(u"reset_statistic_btn")
        self.reset_statistic_btn.setMinimumSize(QSize(130, 35))
        self.reset_statistic_btn.setMaximumSize(QSize(130, 35))
        font3 = QFont()
        font3.setFamilies([u"Banshrift-Light"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.reset_statistic_btn.setFont(font3)
        self.reset_statistic_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius : 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,65);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/media/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset_statistic_btn.setIcon(icon1)
        self.reset_statistic_btn.setIconSize(QSize(20, 20))
        self.reset_statistic_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.reset_statistic_btn)

        self.show_statistic_btn = QPushButton(self.statistic_btns_frame)
        self.show_statistic_btn.setObjectName(u"show_statistic_btn")
        self.show_statistic_btn.setMinimumSize(QSize(130, 35))
        self.show_statistic_btn.setMaximumSize(QSize(130, 35))
        self.show_statistic_btn.setFont(font3)
        self.show_statistic_btn.setLayoutDirection(Qt.LeftToRight)
        self.show_statistic_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius : 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,65);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"\n"
"")
        self.show_statistic_btn.setText(u"Statistic")
        icon2 = QIcon()
        icon2.addFile(u":/icons/media/statistics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_statistic_btn.setIcon(icon2)
        self.show_statistic_btn.setIconSize(QSize(20, 20))
        self.show_statistic_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.show_statistic_btn)

        self.games_played_couter_frame = QFrame(self.centralwidget)
        self.games_played_couter_frame.setObjectName(u"games_played_couter_frame")
        self.games_played_couter_frame.setGeometry(QRect(290, 230, 261, 41))
        self.games_played_couter_frame.setMaximumSize(QSize(261, 41))
        self.games_played_couter_frame.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.games_played_couter_frame)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.games_played_text_lb = QLabel(self.games_played_couter_frame)
        self.games_played_text_lb.setObjectName(u"games_played_text_lb")
        self.games_played_text_lb.setMinimumSize(QSize(140, 30))
        self.games_played_text_lb.setMaximumSize(QSize(140, 30))
        font4 = QFont()
        font4.setFamilies([u"Banshrift-Light"])
        font4.setPointSize(16)
        self.games_played_text_lb.setFont(font4)
        self.games_played_text_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.games_played_text_lb.setTextFormat(Qt.RichText)
        self.games_played_text_lb.setScaledContents(False)
        self.games_played_text_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.games_played_text_lb)

        self.games_played_counter_lb = QLabel(self.games_played_couter_frame)
        self.games_played_counter_lb.setObjectName(u"games_played_counter_lb")
        self.games_played_counter_lb.setMinimumSize(QSize(50, 30))
        self.games_played_counter_lb.setMaximumSize(QSize(50, 30))
        font5 = QFont()
        font5.setFamilies([u"Banshrift-Light"])
        font5.setPointSize(16)
        font5.setBold(False)
        self.games_played_counter_lb.setFont(font5)
        self.games_played_counter_lb.setToolTipDuration(-1)
        self.games_played_counter_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.games_played_counter_lb.setTextFormat(Qt.RichText)
        self.games_played_counter_lb.setScaledContents(False)
        self.games_played_counter_lb.setAlignment(Qt.AlignCenter)
        self.games_played_counter_lb.setIndent(-1)

        self.horizontalLayout_5.addWidget(self.games_played_counter_lb)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setGeometry(QRect(170, 60, 472, 161))
        self.btn_frame.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,65);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.rock_btn = QPushButton(self.btn_frame)
        self.rock_btn.setObjectName(u"rock_btn")
        self.rock_btn.setMinimumSize(QSize(145, 145))
        self.rock_btn.setMaximumSize(QSize(145, 145))
        self.rock_btn.setStyleSheet(u"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/media/rock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rock_btn.setIcon(icon3)
        self.rock_btn.setIconSize(QSize(120, 120))
        self.rock_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.rock_btn)

        self.scissors_btn = QPushButton(self.btn_frame)
        self.scissors_btn.setObjectName(u"scissors_btn")
        self.scissors_btn.setMinimumSize(QSize(145, 145))
        self.scissors_btn.setMaximumSize(QSize(145, 145))
        self.scissors_btn.setStyleSheet(u"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/media/scissors.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.scissors_btn.setIcon(icon4)
        self.scissors_btn.setIconSize(QSize(120, 120))
        self.scissors_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.scissors_btn)

        self.paper_btn = QPushButton(self.btn_frame)
        self.paper_btn.setObjectName(u"paper_btn")
        self.paper_btn.setMinimumSize(QSize(145, 145))
        self.paper_btn.setMaximumSize(QSize(145, 145))
        self.paper_btn.setStyleSheet(u"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,88);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/media/paper.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.paper_btn.setIcon(icon5)
        self.paper_btn.setIconSize(QSize(120, 120))
        self.paper_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.paper_btn)

        self.choices_frame = QFrame(self.centralwidget)
        self.choices_frame.setObjectName(u"choices_frame")
        self.choices_frame.setGeometry(QRect(10, 290, 791, 161))
        self.horizontalLayout_2 = QHBoxLayout(self.choices_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.first_choice_icon_lb = QLabel(self.choices_frame)
        self.first_choice_icon_lb.setObjectName(u"first_choice_icon_lb")
        self.first_choice_icon_lb.setMinimumSize(QSize(155, 155))
        self.first_choice_icon_lb.setMaximumSize(QSize(155, 155))
        self.first_choice_icon_lb.setStyleSheet(u"QLabel {\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"}")
        self.first_choice_icon_lb.setScaledContents(True)
        self.first_choice_icon_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.first_choice_icon_lb)

        self.vs_icon_lb = QLabel(self.choices_frame)
        self.vs_icon_lb.setObjectName(u"vs_icon_lb")
        self.vs_icon_lb.setMinimumSize(QSize(155, 155))
        self.vs_icon_lb.setMaximumSize(QSize(155, 155))
        self.vs_icon_lb.setPixmap(QPixmap(u":/icons/media/versus.png"))
        self.vs_icon_lb.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.vs_icon_lb)

        self.second_choice_icon_lb = QLabel(self.choices_frame)
        self.second_choice_icon_lb.setObjectName(u"second_choice_icon_lb")
        self.second_choice_icon_lb.setMinimumSize(QSize(155, 155))
        self.second_choice_icon_lb.setMaximumSize(QSize(155, 155))
        self.second_choice_icon_lb.setStyleSheet(u"QLabel {\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"}")
        self.second_choice_icon_lb.setScaledContents(True)
        self.second_choice_icon_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.second_choice_icon_lb)

        self.players_score_frame = QFrame(self.centralwidget)
        self.players_score_frame.setObjectName(u"players_score_frame")
        self.players_score_frame.setGeometry(QRect(80, 460, 651, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.players_score_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.first_player_frame = QFrame(self.players_score_frame)
        self.first_player_frame.setObjectName(u"first_player_frame")
        self.horizontalLayout_3 = QHBoxLayout(self.first_player_frame)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.first_choice_player_name_lb = QLabel(self.first_player_frame)
        self.first_choice_player_name_lb.setObjectName(u"first_choice_player_name_lb")
        self.first_choice_player_name_lb.setMinimumSize(QSize(80, 30))
        self.first_choice_player_name_lb.setMaximumSize(QSize(80, 30))
        self.first_choice_player_name_lb.setFont(font4)
        self.first_choice_player_name_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.first_choice_player_name_lb.setTextFormat(Qt.AutoText)
        self.first_choice_player_name_lb.setScaledContents(False)
        self.first_choice_player_name_lb.setAlignment(Qt.AlignCenter)
        self.first_choice_player_name_lb.setWordWrap(False)
        self.first_choice_player_name_lb.setMargin(0)

        self.horizontalLayout_3.addWidget(self.first_choice_player_name_lb)

        self.first_choice_player_score_lb = QLabel(self.first_player_frame)
        self.first_choice_player_score_lb.setObjectName(u"first_choice_player_score_lb")
        self.first_choice_player_score_lb.setMinimumSize(QSize(70, 30))
        self.first_choice_player_score_lb.setMaximumSize(QSize(70, 30))
        self.first_choice_player_score_lb.setFont(font5)
        self.first_choice_player_score_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.first_choice_player_score_lb.setTextFormat(Qt.RichText)
        self.first_choice_player_score_lb.setScaledContents(False)
        self.first_choice_player_score_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.first_choice_player_score_lb)


        self.horizontalLayout_6.addWidget(self.first_player_frame)

        self.horizontalSpacer_9 = QSpacerItem(268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.second_player_frame = QFrame(self.players_score_frame)
        self.second_player_frame.setObjectName(u"second_player_frame")
        self.horizontalLayout_4 = QHBoxLayout(self.second_player_frame)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.second_choice_player_score_lb = QLabel(self.second_player_frame)
        self.second_choice_player_score_lb.setObjectName(u"second_choice_player_score_lb")
        self.second_choice_player_score_lb.setMinimumSize(QSize(70, 30))
        self.second_choice_player_score_lb.setMaximumSize(QSize(70, 30))
        self.second_choice_player_score_lb.setFont(font4)
        self.second_choice_player_score_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"}")
        self.second_choice_player_score_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.second_choice_player_score_lb)

        self.second_choice_player_name_lb = QLabel(self.second_player_frame)
        self.second_choice_player_name_lb.setObjectName(u"second_choice_player_name_lb")
        self.second_choice_player_name_lb.setMinimumSize(QSize(80, 30))
        self.second_choice_player_name_lb.setMaximumSize(QSize(80, 30))
        self.second_choice_player_name_lb.setFont(font4)
        self.second_choice_player_name_lb.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: none;\n"
"}")
        self.second_choice_player_name_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.second_choice_player_name_lb)


        self.horizontalLayout_6.addWidget(self.second_player_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rock-scissors-paper", None))
        self.result_lb.setText("")
        self.main_lb.setText(QCoreApplication.translate("MainWindow", u"Choose rock, scissors or paper", None))
        self.reset_statistic_btn.setText(QCoreApplication.translate("MainWindow", u"Reset statistic", None))
        self.games_played_text_lb.setText(QCoreApplication.translate("MainWindow", u"Games played", None))
        self.games_played_counter_lb.setText("")
        self.rock_btn.setText("")
        self.scissors_btn.setText("")
        self.paper_btn.setText("")
        self.first_choice_icon_lb.setText("")
        self.vs_icon_lb.setText("")
        self.second_choice_icon_lb.setText("")
        self.first_choice_player_name_lb.setText(QCoreApplication.translate("MainWindow", u"You", None))
        self.first_choice_player_score_lb.setText("")
        self.second_choice_player_score_lb.setText("")
        self.second_choice_player_name_lb.setText(QCoreApplication.translate("MainWindow", u"AI", None))
    # retranslateUi

