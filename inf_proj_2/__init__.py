# -*- coding: utf-8 -*-
"""
/***************************************************************************
 INF_PROJ_2
                                 A QGIS plugin
 Wtyczka obliczjąca przewyższenia, pola pow. itd.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        copyright            : (C) 2023 by Aleksandra Zawadka
        email                : lozawadka@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load INF_PROJ_2 class from file INF_PROJ_2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .INF_PROJ_2 import INF_PROJ_2
    return INF_PROJ_2(iface)