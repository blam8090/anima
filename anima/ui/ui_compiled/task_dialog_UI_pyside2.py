# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eoyilmaz\Documents\development\anima\anima\anima\ui\ui_files\task_dialog.ui'
#
# Created: Mon May 08 09:33:04 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 788)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dialog_label = QtWidgets.QLabel(Dialog)
        self.dialog_label.setStyleSheet("color: rgb(71, 143, 202);\n"
"font: 18pt;")
        self.dialog_label.setObjectName("dialog_label")
        self.verticalLayout.addWidget(self.dialog_label)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.entity_type_label = QtWidgets.QLabel(Dialog)
        self.entity_type_label.setObjectName("entity_type_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.entity_type_label)
        self.entity_type_comboBox = QtWidgets.QComboBox(Dialog)
        self.entity_type_comboBox.setObjectName("entity_type_comboBox")
        self.entity_type_comboBox.addItem("")
        self.entity_type_comboBox.addItem("")
        self.entity_type_comboBox.addItem("")
        self.entity_type_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entity_type_comboBox)
        self.project_label = QtWidgets.QLabel(Dialog)
        self.project_label.setObjectName("project_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.project_label)
        self.projects_comboBox = QtWidgets.QComboBox(Dialog)
        self.projects_comboBox.setObjectName("projects_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.projects_comboBox)
        self.parent_label = QtWidgets.QLabel(Dialog)
        self.parent_label.setObjectName("parent_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.parent_label)
        self.parent_task_fields_verticalLayout = QtWidgets.QVBoxLayout()
        self.parent_task_fields_verticalLayout.setObjectName("parent_task_fields_verticalLayout")
        self.parent_task_fields_horizontalLayout = QtWidgets.QHBoxLayout()
        self.parent_task_fields_horizontalLayout.setObjectName("parent_task_fields_horizontalLayout")
        self.pick_parent_task_pushButton = QtWidgets.QPushButton(Dialog)
        self.pick_parent_task_pushButton.setObjectName("pick_parent_task_pushButton")
        self.parent_task_fields_horizontalLayout.addWidget(self.pick_parent_task_pushButton)
        self.parent_task_fields_verticalLayout.addLayout(self.parent_task_fields_horizontalLayout)
        self.parent_task_validator_label = QtWidgets.QLabel(Dialog)
        self.parent_task_validator_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.parent_task_validator_label.setObjectName("parent_task_validator_label")
        self.parent_task_fields_verticalLayout.addWidget(self.parent_task_validator_label)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.parent_task_fields_verticalLayout)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_field_verticalLayout = QtWidgets.QVBoxLayout()
        self.name_field_verticalLayout.setObjectName("name_field_verticalLayout")
        self.name_validator_label = QtWidgets.QLabel(Dialog)
        self.name_validator_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.name_validator_label.setObjectName("name_validator_label")
        self.name_field_verticalLayout.addWidget(self.name_validator_label)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.name_field_verticalLayout)
        self.code_label = QtWidgets.QLabel(Dialog)
        self.code_label.setObjectName("code_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.code_label)
        self.code_field_verticalLayout = QtWidgets.QVBoxLayout()
        self.code_field_verticalLayout.setObjectName("code_field_verticalLayout")
        self.code_validator_label = QtWidgets.QLabel(Dialog)
        self.code_validator_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.code_validator_label.setObjectName("code_validator_label")
        self.code_field_verticalLayout.addWidget(self.code_validator_label)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.code_field_verticalLayout)
        self.task_type_label = QtWidgets.QLabel(Dialog)
        self.task_type_label.setObjectName("task_type_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.task_type_label)
        self.asset_type_label = QtWidgets.QLabel(Dialog)
        self.asset_type_label.setObjectName("asset_type_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.asset_type_label)
        self.fps_label = QtWidgets.QLabel(Dialog)
        self.fps_label.setObjectName("fps_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.fps_label)
        self.fps_spinBox = QtWidgets.QSpinBox(Dialog)
        self.fps_spinBox.setMinimum(1)
        self.fps_spinBox.setObjectName("fps_spinBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.fps_spinBox)
        self.cutIn_cutOut_label = QtWidgets.QLabel(Dialog)
        self.cutIn_cutOut_label.setObjectName("cutIn_cutOut_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.cutIn_cutOut_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cutIn_spinBox = QtWidgets.QSpinBox(Dialog)
        self.cutIn_spinBox.setObjectName("cutIn_spinBox")
        self.horizontalLayout_4.addWidget(self.cutIn_spinBox)
        self.cutOut_spinBox = QtWidgets.QSpinBox(Dialog)
        self.cutOut_spinBox.setObjectName("cutOut_spinBox")
        self.horizontalLayout_4.addWidget(self.cutOut_spinBox)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.depends_to_label = QtWidgets.QLabel(Dialog)
        self.depends_to_label.setObjectName("depends_to_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.depends_to_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.depends_to_listWidget = QtWidgets.QListWidget(Dialog)
        self.depends_to_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.depends_to_listWidget.setObjectName("depends_to_listWidget")
        self.horizontalLayout_3.addWidget(self.depends_to_listWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_depending_task_pushButton = QtWidgets.QPushButton(Dialog)
        self.add_depending_task_pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.add_depending_task_pushButton.setObjectName("add_depending_task_pushButton")
        self.verticalLayout_3.addWidget(self.add_depending_task_pushButton)
        self.remove_depending_task_pushButton = QtWidgets.QPushButton(Dialog)
        self.remove_depending_task_pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.remove_depending_task_pushButton.setObjectName("remove_depending_task_pushButton")
        self.verticalLayout_3.addWidget(self.remove_depending_task_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.resources_label = QtWidgets.QLabel(Dialog)
        self.resources_label.setObjectName("resources_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.resources_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resources_comboBox = QtWidgets.QComboBox(Dialog)
        self.resources_comboBox.setEditable(True)
        self.resources_comboBox.setObjectName("resources_comboBox")
        self.verticalLayout_2.addWidget(self.resources_comboBox)
        self.resources_listWidget = QtWidgets.QListWidget(Dialog)
        self.resources_listWidget.setObjectName("resources_listWidget")
        self.verticalLayout_2.addWidget(self.resources_listWidget)
        self.formLayout.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.responsible_label = QtWidgets.QLabel(Dialog)
        self.responsible_label.setObjectName("responsible_label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.responsible_label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.responsible_comboBox = QtWidgets.QComboBox(Dialog)
        self.responsible_comboBox.setEditable(True)
        self.responsible_comboBox.setObjectName("responsible_comboBox")
        self.verticalLayout_4.addWidget(self.responsible_comboBox)
        self.responsible_listWidget = QtWidgets.QListWidget(Dialog)
        self.responsible_listWidget.setObjectName("responsible_listWidget")
        self.verticalLayout_4.addWidget(self.responsible_listWidget)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.schedule_timing_label = QtWidgets.QLabel(Dialog)
        self.schedule_timing_label.setObjectName("schedule_timing_label")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.schedule_timing_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.schedule_timing_spinBox = QtWidgets.QSpinBox(Dialog)
        self.schedule_timing_spinBox.setMaximum(9999)
        self.schedule_timing_spinBox.setObjectName("schedule_timing_spinBox")
        self.horizontalLayout_2.addWidget(self.schedule_timing_spinBox)
        self.schedule_unit_comboBox = QtWidgets.QComboBox(Dialog)
        self.schedule_unit_comboBox.setObjectName("schedule_unit_comboBox")
        self.horizontalLayout_2.addWidget(self.schedule_unit_comboBox)
        self.schedule_model_comboBox = QtWidgets.QComboBox(Dialog)
        self.schedule_model_comboBox.setObjectName("schedule_model_comboBox")
        self.horizontalLayout_2.addWidget(self.schedule_model_comboBox)
        self.formLayout.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.update_bid_label = QtWidgets.QLabel(Dialog)
        self.update_bid_label.setObjectName("update_bid_label")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.update_bid_label)
        self.update_bid_checkBox = QtWidgets.QCheckBox(Dialog)
        self.update_bid_checkBox.setText("")
        self.update_bid_checkBox.setObjectName("update_bid_checkBox")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.update_bid_checkBox)
        self.priority_label = QtWidgets.QLabel(Dialog)
        self.priority_label.setObjectName("priority_label")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.priority_label)
        self.priority_spinBox = QtWidgets.QSpinBox(Dialog)
        self.priority_spinBox.setMaximum(1000)
        self.priority_spinBox.setProperty("value", 500)
        self.priority_spinBox.setObjectName("priority_spinBox")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.priority_spinBox)
        self.sequence_label = QtWidgets.QLabel(Dialog)
        self.sequence_label.setObjectName("sequence_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.sequence_label)
        self.sequence_comboBox = QtWidgets.QComboBox(Dialog)
        self.sequence_comboBox.setObjectName("sequence_comboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sequence_comboBox)
        self.asset_type_comboBox = QtWidgets.QComboBox(Dialog)
        self.asset_type_comboBox.setEditable(True)
        self.asset_type_comboBox.setObjectName("asset_type_comboBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.asset_type_comboBox)
        self.task_type_comboBox = QtWidgets.QComboBox(Dialog)
        self.task_type_comboBox.setEditable(True)
        self.task_type_comboBox.setObjectName("task_type_comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.task_type_comboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.entity_type_comboBox, self.projects_comboBox)
        Dialog.setTabOrder(self.projects_comboBox, self.pick_parent_task_pushButton)
        Dialog.setTabOrder(self.pick_parent_task_pushButton, self.task_type_comboBox)
        Dialog.setTabOrder(self.task_type_comboBox, self.asset_type_comboBox)
        Dialog.setTabOrder(self.asset_type_comboBox, self.sequence_comboBox)
        Dialog.setTabOrder(self.sequence_comboBox, self.fps_spinBox)
        Dialog.setTabOrder(self.fps_spinBox, self.cutIn_spinBox)
        Dialog.setTabOrder(self.cutIn_spinBox, self.cutOut_spinBox)
        Dialog.setTabOrder(self.cutOut_spinBox, self.depends_to_listWidget)
        Dialog.setTabOrder(self.depends_to_listWidget, self.add_depending_task_pushButton)
        Dialog.setTabOrder(self.add_depending_task_pushButton, self.remove_depending_task_pushButton)
        Dialog.setTabOrder(self.remove_depending_task_pushButton, self.resources_comboBox)
        Dialog.setTabOrder(self.resources_comboBox, self.resources_listWidget)
        Dialog.setTabOrder(self.resources_listWidget, self.responsible_comboBox)
        Dialog.setTabOrder(self.responsible_comboBox, self.responsible_listWidget)
        Dialog.setTabOrder(self.responsible_listWidget, self.schedule_timing_spinBox)
        Dialog.setTabOrder(self.schedule_timing_spinBox, self.schedule_unit_comboBox)
        Dialog.setTabOrder(self.schedule_unit_comboBox, self.schedule_model_comboBox)
        Dialog.setTabOrder(self.schedule_model_comboBox, self.update_bid_checkBox)
        Dialog.setTabOrder(self.update_bid_checkBox, self.priority_spinBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Task Dialog", None, -1))
        self.dialog_label.setText(QtWidgets.QApplication.translate("Dialog", "Create Task", None, -1))
        self.entity_type_label.setText(QtWidgets.QApplication.translate("Dialog", "Entity Type", None, -1))
        self.entity_type_comboBox.setItemText(0, QtWidgets.QApplication.translate("Dialog", "Task", None, -1))
        self.entity_type_comboBox.setItemText(1, QtWidgets.QApplication.translate("Dialog", "Asset", None, -1))
        self.entity_type_comboBox.setItemText(2, QtWidgets.QApplication.translate("Dialog", "Shot", None, -1))
        self.entity_type_comboBox.setItemText(3, QtWidgets.QApplication.translate("Dialog", "Sequence", None, -1))
        self.project_label.setText(QtWidgets.QApplication.translate("Dialog", "Project", None, -1))
        self.parent_label.setText(QtWidgets.QApplication.translate("Dialog", "Parent", None, -1))
        self.pick_parent_task_pushButton.setToolTip(QtWidgets.QApplication.translate("Dialog", "Pick parent task", None, -1))
        self.pick_parent_task_pushButton.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.parent_task_validator_label.setText(QtWidgets.QApplication.translate("Dialog", "Validator Message", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("Dialog", "Name", None, -1))
        self.name_validator_label.setText(QtWidgets.QApplication.translate("Dialog", "Validator Message", None, -1))
        self.code_label.setText(QtWidgets.QApplication.translate("Dialog", "Code", None, -1))
        self.code_validator_label.setText(QtWidgets.QApplication.translate("Dialog", "Validator Message", None, -1))
        self.task_type_label.setText(QtWidgets.QApplication.translate("Dialog", "Task Type", None, -1))
        self.asset_type_label.setText(QtWidgets.QApplication.translate("Dialog", "Asset Type", None, -1))
        self.fps_label.setText(QtWidgets.QApplication.translate("Dialog", "FPS", None, -1))
        self.cutIn_cutOut_label.setText(QtWidgets.QApplication.translate("Dialog", "Cut In & Out", None, -1))
        self.depends_to_label.setText(QtWidgets.QApplication.translate("Dialog", "Depends To", None, -1))
        self.add_depending_task_pushButton.setText(QtWidgets.QApplication.translate("Dialog", "+", None, -1))
        self.remove_depending_task_pushButton.setText(QtWidgets.QApplication.translate("Dialog", "-", None, -1))
        self.resources_label.setText(QtWidgets.QApplication.translate("Dialog", "Resources", None, -1))
        self.resources_listWidget.setToolTip(QtWidgets.QApplication.translate("Dialog", "Double click to remove", None, -1))
        self.responsible_label.setText(QtWidgets.QApplication.translate("Dialog", "Responsible", None, -1))
        self.schedule_timing_label.setText(QtWidgets.QApplication.translate("Dialog", "Schedule Timing", None, -1))
        self.update_bid_label.setText(QtWidgets.QApplication.translate("Dialog", "Update Bid", None, -1))
        self.priority_label.setText(QtWidgets.QApplication.translate("Dialog", "Priority", None, -1))
        self.sequence_label.setText(QtWidgets.QApplication.translate("Dialog", "Sequence", None, -1))
