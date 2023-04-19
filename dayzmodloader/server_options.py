# serveroptions.py

from PyQt5 import QtWidgets

class ServerOptions(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Server Options")
        
        # Create widgets
        self.profiles_path_label = QtWidgets.QLabel("Profiles Path:")
        self.profiles_path_edit = QtWidgets.QLineEdit()
        self.profiles_path_button = QtWidgets.QPushButton("Browse...")
        self.profiles_path_button.clicked.connect(self.on_profiles_path_button_clicked)

        self.mission_label = QtWidgets.QLabel("(DZDIAG) Mission:")
        self.mission_path_edit = QtWidgets.QLineEdit()
        self.mission_button = QtWidgets.QPushButton("Browse...")
        self.mission_button.clicked.connect(self.on_mission_button_clicked)
        
        self.nonavmesh_checkbox = QtWidgets.QCheckBox("No NavMesh")
        self.nosplash_checkbox = QtWidgets.QCheckBox("No Splash")
        self.nopause_checkbox = QtWidgets.QCheckBox("No Pause")
        self.nobenchmark_checkbox = QtWidgets.QCheckBox("No Benchmark")
        self.filepatching_checkbox = QtWidgets.QCheckBox("File Patching")
        self.dologs_checkbox = QtWidgets.QCheckBox("Do Logs")
        self.scriptdebug_checkbox = QtWidgets.QCheckBox("Script Debug")
        self.adminlog_checkbox = QtWidgets.QCheckBox("Admin Log")
        self.netlog_checkbox = QtWidgets.QCheckBox("Net Log")
        self.scrallowfilewrite_checkbox = QtWidgets.QCheckBox("Scr Allow File Write")
        
        self.ok_button = QtWidgets.QPushButton("OK")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Create layouts
        profiles_layout = QtWidgets.QHBoxLayout()
        profiles_layout.addWidget(self.profiles_path_label)
        profiles_layout.addWidget(self.profiles_path_edit)
        profiles_layout.addWidget(self.profiles_path_button)

        mission_layout = QtWidgets.QHBoxLayout()
        mission_layout.addWidget(self.mission_label)
        mission_layout.addWidget(self.mission_path_edit)
        mission_layout.addWidget(self.mission_button)
        
        checkboxes_layout = QtWidgets.QVBoxLayout()
        checkboxes_layout.addWidget(self.nonavmesh_checkbox)
        checkboxes_layout.addWidget(self.nosplash_checkbox)
        checkboxes_layout.addWidget(self.nopause_checkbox)
        checkboxes_layout.addWidget(self.nobenchmark_checkbox)
        checkboxes_layout.addWidget(self.filepatching_checkbox)
        checkboxes_layout.addWidget(self.dologs_checkbox)
        checkboxes_layout.addWidget(self.scriptdebug_checkbox)
        checkboxes_layout.addWidget(self.adminlog_checkbox)
        checkboxes_layout.addWidget(self.netlog_checkbox)
        checkboxes_layout.addWidget(self.scrallowfilewrite_checkbox)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(profiles_layout)
        main_layout.addLayout(mission_layout) 
        main_layout.addLayout(checkboxes_layout)
        main_layout.addLayout(buttons_layout)
        
        self.setLayout(main_layout)
        
    def on_profiles_path_button_clicked(self):
        profiles_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select DayzServerProfile folder")
        if profiles_path:
            self.profiles_path_edit.setText(profiles_path)

    def on_mission_button_clicked(self):
        mission_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Mission Folder")
        if mission_path:
            self.mission_path_edit.setText(mission_path)


    def get_options(self):
        self.server_flags = ""
        options = ""
        if self.nonavmesh_checkbox.isChecked():
            options += " -nonavmesh"
        if self.nosplash_checkbox.isChecked():
            options += " -nosplash"
        if self.nopause_checkbox.isChecked():
            options += " -noPause"
        if self.nobenchmark_checkbox.isChecked():
            options += " -noBenchmark"
        if self.filepatching_checkbox.isChecked():
            options += " -FilePatching"
        if self.dologs_checkbox.isChecked():
            options += " -dologs"
        if self.scriptdebug_checkbox.isChecked():
            options += " -scriptDebug=true"
        if self.adminlog_checkbox.isChecked():
            options += " -adminlog"
        if self.netlog_checkbox.isChecked():
            options += " -netlog"
        if self.scrallowfilewrite_checkbox.isChecked():
            options += " -scrAllowFileWrite"
        return options

    def set_profiles_path(self, path):
        self.profiles_path_edit.setText(path)

    def set_mission_path(self, path):
        self.mission_path_edit.setText(path)