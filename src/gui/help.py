from curses import KEY_MARK
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600,400)
        
        self.all = QVBoxLayout()
        self.main = QScrollArea()
        self.vbox = QVBoxLayout()
        self.w = QWidget()
        self.w.setLayout(self.vbox)

        self.main.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        
        self.main_label = QLabel("How to use pwdKeeper")
        self.main_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.main_label.setAlignment(Qt.AlignCenter)

        self.content = QLabel("""
To start working with pwdKeeper, click on the 'Create a new safe' button.
A save file dialog will pop up. Enter a name for your safe, keeping the
.pwdKeeper file extension intact. Next, you need to create a strong password
for the safe. If you repeat the password correctly in the second input field,
a brute force estimation will pop up below the 'Enter!' button. This is an
estimate of how long it might take an attacker to crack the password to your
safe. Therefore, make sure you use a strong password that would take a longer
time to be cracked.
When you create a password and enter the safe, you will be presented with its
interior. There is a search bar, a button to add new entries, and a list of
entries. Also present is a button to change to another safe, as well as a
button to show this help text. In the top left corner, you can see the name of
the safe you are in at the moment.
Click on the button with a green plus - the add entry button - to add an entry
to your safe. You can also use the hotkeys Ctrl-T, Ctrl-N, or F5. A new window
will pop up, prompting you to enter the name of the service for which you want
to save the password, and the login details (username or email, and password).
Note that the service textbox is a dropdown menu, as is the username/email one.
The former contains a predetermined list of some popular services. The latter
will suggest your usernames or emails after you have made some entries. Enter
the required info and click on the 'Add account' button.
The entry you made will appear in the list, along with the appropriate icon
(or, if there is no icon for your service, it will use a generic one). You can
click on the 'Edit' button to amend the info you entered, or the 'Remove' button
to remove the entry. Hovering over the three asterisks in the password field
will reveal the password. Clicking on either the username or the password will
copy the clicked value to clipboard.
The search bar will filter by service name, username/email, and password. So if
you remember only part of the login info, or merely that you have an account on
that service, you can find it easily using the search bar. You can easily focus
on the search bar with the hotkeys Ctrl-F or F3.
To create a new safe or load another one, click on the 'Change the safe' button.
This will bring you back to the first page, from where you can launch a save or
load file dialog.""")
        self.content.setWordWrap(True)

        self.vbox.addWidget(self.main_label)
        self.vbox.addWidget(self.content)

        self.main.setWidget(self.w)
        self.all.addWidget(self.main)

        self.setLayout(self.all)