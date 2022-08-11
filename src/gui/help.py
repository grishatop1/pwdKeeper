from curses import KEY_MARK
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700,400)
        
        self.all = QVBoxLayout()
        self.main = QScrollArea()
        self.vbox = QVBoxLayout()
        self.w = QWidget()
        self.w.setLayout(self.vbox)

        self.main.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main.setWidgetResizable(True)
        self.vbox.setAlignment(Qt.AlignCenter)
        
        self.main_label = QLabel("How to use pwdKeeper")
        self.main_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.main_label.setAlignment(Qt.AlignCenter)

        self.content = QLabel("""
<h1>Safe creation</h1>
<p>To start working with pwdKeeper, click on the &#39;Create a new safe&#39; button. A save
file dialog will pop up. Enter a name for your safe, keeping the .pwdKeeper file
extension intact.</p>
<p>Next, you need to create a strong password for the safe. If you repeat the
password correctly in the second input field, a brute force estimation will pop
up below the &#39;Enter!&#39; button. This is an estimate of how long it might take an
attacker to crack the password to your safe. Therefore, make sure you use a
strong password that would take a longer time to be cracked.</p>
<h1>Safe interior</h1>
<p>When you create a password and enter the safe, you will be presented with its
interior. There is a search bar, a button to add new entries, and a list of
entries. Also present is a button to change to another safe, as well as a
button to display this help window. In the top left corner, you can see the name of
the safe you are in at the moment.</p>
<h1>Safe usage</h1>
<p>Click on the button with a green plus - the add entry button - to add an entry
to your safe. A new window will pop up, prompting you to enter the name of the
service and the login details (username or email, and password).</p>
<p>Note that the service textbox is a dropdown menu, as is the username/email one.
The former contains a predetermined list of some popular services, though you
can freely enter a new service yourself. The latter will suggest your usernames
or emails after you have made some entries. Enter the required info and click on
the &#39;Add account&#39; button.</p>
<p>The entry you made will appear in the list, along with the appropriate icon (or,
if there is no icon for your service, it will use a generic one). You can click
on the &#39;Edit&#39; button to amend the info you entered, or the &#39;Remove&#39; button to
remove the entry. Hovering over the three asterisks in the password field will
reveal the password. Clicking on either the username or the password will copy
the clicked value to clipboard.</p>
<p>The search bar will filter by service name, username/email, and password. So, if
you remember only part of the login info, or merely that you have an account on
that service, you can find it easily using the search bar.</p>
<p>To create a new safe or load another one, click on the &#39;Change the safe&#39; button.
This will bring you back to the first page, from where you can launch a save or
load file dialog using the two buttons.</p>
<p>If you exit pwdKeeper without previously exiting the safe, upon entering the
program the next time you will immediately be prompted to enter the password for
that safe (the path to the safe will be displayed so you know which safe you are
entering). This is the same password prompt as when you load an existing safe. </p>
<h1>Hotkeys</h1>
<p>Display this help window - Ctrl+H, F1</p>
<p>Focus on the search bar - Ctrl+F, F3</p>
<p>Open entry creation dialog - Ctrl+N, Ctrl+T. F5</p>""")
        self.content.setWordWrap(True)
        self.content.setTextFormat(Qt.RichText)
        self.content.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.vbox.addWidget(self.main_label)
        self.vbox.addSpacing(20)
        self.vbox.addWidget(self.content)

        self.main.setWidget(self.w)
        self.all.addWidget(self.main)

        self.setLayout(self.all)