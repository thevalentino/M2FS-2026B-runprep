from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.time import Time
from astroquery.gaia import Gaia

data = {
    "J0022_CFG01": {
        "sh_ra": 5.2410717956,
        "sh_dec": -0.7170246351,
        "file": "J0022_CFG01_calibs.tsv",
    },
    "J0022_CFG02": {
        "sh_ra": 5.5886277698,
        "sh_dec": -0.485957954,
        "file": "J0022_CFG02_calibs.tsv",
    },
    "J0140_CFG07": {
        "sh_ra": 25.0843522142,
        "sh_dec": 2.945202523,
        "file": "J0140_CFG07_calibs.tsv",
    },
    "J0140_CFG08": {
        "sh_ra": 25.3484249366,
        "sh_dec": 2.6489896963,
        "file": "J0140_CFG08_calibs.tsv",
    },
    "J2259_CFG04": {
        "sh_ra": 344.5743205643,
        "sh_dec": 13.9021129124,
        "file": "J2259_CFG04_calibs.tsv",
    },
    "J2259_CFG05": {
        "sh_ra": 345.0547871036,
        "sh_dec": 13.8353116299,
        "file": "J2259_CFG05_calibs.tsv",
    },
}

# source = data["J0022_CFG01"]
# source = data["J0022_CFG02"]
# source = data["J0140_CFG07"]
# source = data["J0140_CFG08"]
# source = data["J2259_CFG04"]
source = data["J2259_CFG05"]

# 5.2410717956 -0.7170246351 J2026.10 2542218565870416000    C       10 -0.00375 -0.00206
sh_star = SkyCoord(
    ra=source["sh_ra"] * u.deg,
    dec=source["sh_dec"] * u.deg,
    frame="icrs",
    obstime=Time("J2026.10"),
)

calib_stars_fname = source["file"]
calibs = Table.read(calib_stars_fname, format="ascii.tab")

calib_coords = SkyCoord(
    ra=calibs["_RAJ2000"] * u.deg,
    dec=calibs["_DEJ2000"] * u.deg,
    pm_ra_cosdec=calibs["pmRA"] * u.mas / u.yr,
    pm_dec=calibs["pmDE"] * u.mas / u.yr,
    frame="icrs",
    obstime=Time("J2000.0"),
)

# max_dist_in_ra = (
#     calib_coords.apply_space_motion(new_obstime=Time("J2000.0")).ra.deg
#     - calibs["_RAJ2000"]
# ).max()

# max_dist_in_dec = (
#     calib_coords.apply_space_motion(new_obstime=Time("J2000.0")).dec.deg
#     - calibs["_DEJ2000"]
# ).max()

# print("Max distance in RA in deg: ", (max_dist_in_ra * u.deg).to("arcsec"))
# print("Max distance in DEC in deg: ", (max_dist_in_dec * u.deg).to("arcsec"))
#
# d = sh_star.separation(calib_coords.apply_space_motion(new_obstime=Time("J2026.10")))

# 5.314227672  -0.945647229    J2000  2542069753842816128    T        9  0.030969  -0.009076   16.7640
line = "{:.9f}  {:.9f}    J2000  {:d}    T        9  {:-9.6f}  {:-9.6f}   {:.4f}"
print(
    line.format(
        calibs["_RAJ2000"][0],
        calibs["_DEJ2000"][0],
        calibs["Source"][0],
        calibs["pmRA"][0] / 1000,
        calibs["pmDE"][0] / 1000,
        calibs["Gmag"][0],
    )
)

calib_stars_log = []
for i in range(len(calibs)):
    calib_stars_log.append(
        line.format(
            calibs["_RAJ2000"][i],
            calibs["_DEJ2000"][i],
            calibs["Source"][i],
            calibs["pmRA"][i] / 1000,
            calibs["pmDE"][i] / 1000,
            calibs["Gmag"][i],
        )
    )

print("\n".join(calib_stars_log))
