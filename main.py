import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
import json




#login
client = wilib.login("su_hoang","1")

well = client.getWellById(31)

zs = well.getAllZoneSets()

z = zs[0].getAllZones()
print(z[0].getInfo())