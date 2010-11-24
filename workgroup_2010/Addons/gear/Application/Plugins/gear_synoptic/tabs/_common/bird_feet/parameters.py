'''

    This file is part of GEAR.

    GEAR is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.html>.

    Author:     Jeremie Passerin      geerem@hotmail.com
    Company:    Studio Nest (TM)
    Date:       2010 / 11 / 15

'''

## @package gear_Synoptic.bird_feet.parameters
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
# Built-in
import os

# Gear
from gear.xsi import c

import gear.xsi.plugin as plu
import gear.xsi.parameter as par

##########################################################
# ADD PARAMETERS
##########################################################
def addParameters(prop):

   # Path Parameter for the Synoptic
   path = os.path.join(plu.getPluginPath("gear_Synoptic"), "tabs", "_common", "bird_feet", "bird_feet.htm")
   par.createOrReturnParameters3(prop, "bird_feet_path", c.siString, path, None, None, False, False)

   par.createOrReturnParameters3(prop, "quicksel_A", c.siString, "", None, None, False, False)
   par.createOrReturnParameters3(prop, "quicksel_B", c.siString, "", None, None, False, False)
   par.createOrReturnParameters3(prop, "quicksel_C", c.siString, "", None, None, False, False)
   par.createOrReturnParameters3(prop, "quicksel_D", c.siString, "", None, None, False, False)
   par.createOrReturnParameters3(prop, "quicksel_E", c.siString, "", None, None, False, False)
   par.createOrReturnParameters3(prop, "quicksel_F", c.siString, "", None, None, False, False)
