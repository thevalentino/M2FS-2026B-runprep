from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.time import Time
from astroquery.gaia import Gaia

# Acqu:
# $Gmag > 14.9 && $Gmag < 15.4 && $pmRA < 10 && $pmRA > -10 && $pmDE < 10 && $pmDE > -10
#
# Guides:
# $Gmag < 14.9 && $pmRA < 10 && $pmRA > -10 && $pmDE < 10 && $pmDE > -10
#
# Calibs:
# $Gmag>16.5 && $Gmag < 17 && $pmRA<10 && $pmRA>-10 && $pmDE<10 && $pmDE>-10

data = {
    "J0022_CFG01": {
        "sh_ra": 5.2410717956,
        "sh_dec": -0.7170246351,
        "acqus": "J0022_CFG01_acqu.tsv",
        "guides": "J0022_CFG01_guides.tsv",
        "calibs": "J0022_CFG01_calibs.tsv",
    },
    "J0022_CFG02": {
        "sh_ra": 5.5886277698,
        "sh_dec": -0.485957954,
        "acqus": "J0022_CFG02_acqu.tsv",
        "guides": "J0022_CFG02_guides.tsv",
        "calibs": "J0022_CFG02_calibs.tsv",
    },
    "J0140_CFG07": {
        "sh_ra": 25.0843522142,
        "sh_dec": 2.945202523,
        "acqus": "J0140_CFG07_acqu.tsv",
        "guides": "J0140_CFG07_guides.tsv",
        "calibs": "J0140_CFG07_calibs.tsv",
    },
    "J0140_CFG08": {
        "sh_ra": 25.3484249366,
        "sh_dec": 2.6489896963,
        "acqus": "J0140_CFG08_acqu.tsv",
        "guides": "J0140_CFG08_guides.tsv",
        "calibs": "J0140_CFG08_calibs.tsv",
    },
    "J2259_CFG04": {
        "sh_ra": 344.5743205643,
        "sh_dec": 13.9021129124,
        "acqus": "J2259_CFG04_acqu.tsv",
        "guides": "J2259_CFG04_guides.tsv",
        "calibs": "J2259_CFG04_calibs.tsv",
    },
    "J2259_CFG05": {
        "sh_ra": 345.0547871036,
        "sh_dec": 13.8353116299,
        "acqus": "J2259_CFG05_acqu.tsv",
        "guides": "J2259_CFG05_guides.tsv",
        "calibs": "J2259_CFG05_calibs.tsv",
    },
}

# source = data["J0022_CFG01"]
# source = data["J0022_CFG02"]
# source = data["J0140_CFG07"]
# source = data["J0140_CFG08"]
# source = data["J2259_CFG04"]
source = data["J2259_CFG05"]

types = ["acqus", "guides", "calibs"]
codes = {"guides": "G",
         "acqus": "A",
         "calibs": "T"}
priority = {"acqus": 10,
            "guides": 10,
            "calibs": 9}
line = "{:.9f}  {:.9f}    2000.0 {:d}    {}        {:2d}  {:-9.6f}  {:-9.6f}   {:.4f}"

for t in types:
    stars_fname = source[t]
    stars = Table.read(stars_fname, format="ascii.tab")

    coords = SkyCoord(
        ra=stars["_RAJ2000"] * u.deg,
        dec=stars["_DEJ2000"] * u.deg,
        pm_ra_cosdec=stars["pmRA"] * u.mas / u.yr,
        pm_dec=stars["pmDE"] * u.mas / u.yr,
        frame="icrs",
        obstime=Time("J2000.0"),
    )

    stars_log = []
    for i in range(len(stars)):
        stars_log.append(
            line.format(
                stars["_RAJ2000"][i],
                stars["_DEJ2000"][i],
                stars["Source"][i],
                codes[t],
                priority[t],
                stars["pmRA"][i] / 1000,
                stars["pmDE"][i] / 1000,
                stars["Gmag"][i],
            )
        )

    print(f"# {t}")
    print("\n".join(stars_log))
