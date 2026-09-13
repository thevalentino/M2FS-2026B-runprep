import pandas as pd
from astropy import units as u
from astropy.coordinates import ICRS, SkyCoord

star_targets = []
targets = []

# field_file = "J0022_CFG01.field"
# field_file = "J0022_CFG02.field"
# field_file = "J2259_CFG04.field"
# field_file = "J2259_CFG05.field"  # stars are outside!!!
field_file = "J2259_CFG05_v3.field"  # stars are outside!!!
# field_file = "J0140_CFG07.field"
# field_file = "J0140_CFG08.field"

with open(field_file, "r") as f:
    for i in range(5):
        f.readline()
    sh_line = f.readline()
    while f.readline() != "# Star targets\n":
        continue
    header = f.readline()  # Star targets header
    # now come the star targets
    star_target_tmp = f.readline()
    while star_target_tmp != "# Targets\n":
        star_targets.append(star_target_tmp)
        star_target_tmp = f.readline()
    header = f.readline()  # Targets header
    # now come the targets
    targets = f.readlines()


def create_sh_coords(sh_line):
    data = sh_line.split()
    ra = float(data[0])
    dec = float(data[1])
    date = data[2]
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame=ICRS, obstime=date)
    return coord


sh = create_sh_coords(sh_line)


def make_df(list_of_data):
    ra = []
    dec = []
    date = []
    id = []
    for line in list_of_data:
        data = line.split()
        ra.append(float(data[0]))
        dec.append(float(data[1]))
        date.append(data[2])
        id.append(int(data[3]))
    df = pd.DataFrame({"ra": ra, "dec": dec, "date": date, "id": id})
    return df


stars = make_df(star_targets)
targets = make_df(targets)

star_coords = SkyCoord(
    ra=stars["ra"].values * u.deg,
    dec=stars["dec"].values * u.deg,
    obstime=stars["date"][0],
    frame=ICRS,
)

target_coords = SkyCoord(
    ra=targets["ra"].values * u.deg,
    dec=targets["dec"].values * u.deg,
    obstime=targets["date"][0],
    frame=ICRS,
)

star_separation = sh.separation(star_coords)
target_separation = sh.separation(target_coords)

star_outside = star_separation > 14.65 * u.arcmin
target_outside = target_separation > 14.65 * u.arcmin
