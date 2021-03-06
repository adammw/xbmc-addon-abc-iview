#
#  ABC iView XBMC Plugin
#  Copyright (C) 2012 Andy Botting
#
#  This plugin includes from from python-iview
#  Copyright (C) 2009-2012 by Jeremy Visser <jeremy@visser.name>
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin. If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os
import urllib2
import urllib
import comm
import utils

try:
    import xbmc, xbmcgui, xbmcplugin
except ImportError:
    pass # for PC debugging

def make_category_list():

    try:
        iview_config = comm.get_config()
        categories = comm.get_categories(iview_config)
        categories = sorted(categories, key=lambda k: k['name'].lower())
        categories.insert(0, {'name':'All', 'keyword':'0-z'})

        ok = True
        for g in categories:
            url = "%s?category_id=%s" % (sys.argv[0], g['keyword'])
            listitem = xbmcgui.ListItem(g['name'])

            # Add the program item to the list
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=True)

        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=ok)
        xbmcplugin.setContent(handle=int(sys.argv[1]), content='episodes')
    except:
        d = xbmcgui.Dialog()
        message = utils.dialog_error("Unable to fetch listing")
        d.ok(*message)
        utils.log_error();

