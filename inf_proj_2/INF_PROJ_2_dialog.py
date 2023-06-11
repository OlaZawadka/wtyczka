# -*- coding: utf-8 -*-
"""
/***************************************************************************
 INF_PROJ_2Dialog
                                 A QGIS plugin
 Wtyczka obliczjąca przewyższenia, pola pow. itd.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Aleksandra Zawadka
        email                : lozawadka@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface 
import numpy as np
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'INF_PROJ_2_dialog_base.ui'))


class INF_PROJ_2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(INF_PROJ_2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_zlicz.clicked.connect(self.przewyzszenie)
        #self.pushbutton_wybwsp.clicked.connect(self.podaj_dane_wsp)
        self.pushButton_pole.clicked.connect(self.polepow)
    import numpy as np

   
    def przewyzszenie(self):
        wybrana_warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        liczba = len(wybrana_warstwa.selectedFeatures())
        if liczba == 2:
            elementy = wybrana_warstwa.selectedFeatures()
            H = []
            Numer = []
            for i in elementy:
                nr = i["Nr"]
                z = float(i["Z"])
                H.append(z)
                Numer.append(nr)
            wys = H[1]-H[0]
            self.label_wynik.setText(f'Przewyższenie między punktami:\n {Numer[0]} i {Numer[1]} wynosi\n {wys:.3f} m')
        else:
            self.label_wynik.setText('Error : Nieodpowiednia liczba punktów.')
            
    def polepow(self):
        wybrana_warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        liczba = wybrana_warstwa.featureCount()
        if liczba >= 3:
            elementy = wybrana_warstwa.selectedFeatures()
            if len(elementy) >= 3:
                Numer = []
                XY = []
                for i in elementy:
                    nr = i["Nr"]
                    x = float(i["X"])
                    y = float(i["Y"])
                    XY.append((x, y))
                    Numer.append(nr)
                XY = np.array(XY)
                X = XY[:, 0]
                Y = XY[:, 1]
                sort = sorted(zip(X, Y), key=lambda point: point[0])
                X, Y = zip(*sort)
                if Y[-2] > Y[-1]:
                    X = list(X)[::-1]
                    Y = list(Y)[::-1]
                P = 0.5 * np.abs(np.dot(X, np.roll(Y, 1)) - np.dot(Y, np.roll(X, 1)))
                n = ' '.join(str(nr) for nr in Numer)
                self.label_wynik.setText(f'Pole powierzchni między punktami\n {n} wynosi:\n {P:.3f} m^2')
            else:
                self.label_wynik.setText('Error: Nie wybrano wystarczającej liczby punktów.')
       