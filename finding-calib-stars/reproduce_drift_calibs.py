import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.time import Time

catalog = Table.read("../output/J0022_CFG01_calib_stars_v2.csv", format="ascii.tab")
dr2_pos = SkyCoord(
    catalog["RA_ICRS"] * u.deg,
    catalog["DE_ICRS"] * u.deg,
    frame="icrs",
    obstime="J2015.5",
    pm_ra_cosdec=catalog["pmRA"] * u.mas / u.yr,
    pm_dec=catalog["pmDE"] * u.mas / u.yr,
)

j2000_pos = SkyCoord(
    ra=catalog["_RAJ2000"] * u.deg,
    dec=catalog["_DEJ2000"] * u.deg,
    frame="icrs",
    obstime="J2000.0",
    pm_ra_cosdec=catalog["pmRA"] * u.mas / u.yr,
    pm_dec=catalog["pmDE"] * u.mas / u.yr,
)

dr2_obs = dr2_pos.apply_space_motion(new_obstime=Time("2026-10-07"))
j2000_obs = j2000_pos.apply_space_motion(new_obstime=Time("2026-10-07"))

print(dr2_obs.separation(j2000_obs).to("arcsec"))
print(
    j2000_pos.separation(dr2_pos.apply_space_motion(new_obstime=Time("J2000.0"))).to(
        "arcsec"
    )
)

# Trying to reproduce the problem that Mario is finding. I will take the
# J2000.0 positions (which are the ones I sent him) and I will assume they are
# epoch 2026.1 (which is mentioned in the .plate file). Then I will plot them
# and see if they are outside the circle. This is just an experiment I am
# trying to figure out what is going wrong.
# - That did not work.
#
# Next try: Mario assumes these are J2026.10 when they are J2000.0 but he also
# assumes FK5 coordinates.

pos_xiao = (5.2410717956, -0.7170246351)
sh_xiao = SkyCoord(
    ra=pos_xiao[0] * u.deg,
    dec=pos_xiao[1] * u.deg,
    frame="icrs",
    equinox="J2000",
    obstime=Time("J2026.10"),
    pm_ra_cosdec=-3.745 * u.mas / u.yr,
    pm_dec=-2.062 * u.mas / u.yr,
)

# mm_pos = SkyCoord(
#     ra=catalog["_RAJ2000"] * u.deg,
#     dec=catalog["_DEJ2000"] * u.deg,
#     frame="icrs",
#     obstime="J2026.1",
#     pm_ra_cosdec=catalog["pmRA"] * u.mas / u.yr,
#     pm_dec=catalog["pmDE"] * u.mas / u.yr,
# )

mm_pos = SkyCoord(
    ra=catalog["_RAJ2000"] * u.deg,
    dec=catalog["_DEJ2000"] * u.deg,
    frame="fk5",
    equinox="J2000.0",
    obstime="J2000.0",
    pm_ra_cosdec=catalog["pmRA"] * u.arcsec / u.yr,
    pm_dec=catalog["pmDE"] * u.arcsec / u.yr,
)

mm_pos_obs = mm_pos.apply_space_motion(new_obstime=Time("J2026.10"))
mm_pos_obs_icrs = mm_pos_obs.transform_to("icrs")

rad = (14.5 * u.arcmin).to("deg")
circle = plt.Circle(
    (sh_xiao.ra.to("deg").value, sh_xiao.dec.to("deg").value),
    radius=rad.value,
    edgecolor="blue",
    facecolor="lightblue",
    linewidth=2,
)


plt.figure(1)
plt.clf()

plt.plot(sh_xiao.ra.to("deg"), sh_xiao.dec.to("deg"), marker="*", ms=12)
# plt.plot(mm_pos.ra.to("deg"), mm_pos.dec.to("deg"), "o")
plt.plot(mm_pos_obs_icrs.ra.to("deg"), mm_pos_obs_icrs.dec.to("deg"), "o")
plt.gca().add_patch(circle)

plt.gca().set_aspect("equal")
plt.plot()
