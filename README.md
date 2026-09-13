# M2FS 2026B - LAEs

This project is for generating the required files for M2FS mask making for the Observing run we have assigned for Oct 7-8 2026 (2026B, LCO, PI. V. Gonzalez, Co-I: XianZhong Zheng).

I originally generated the files in a very manual process but we ended up with a problem in which the coordinates of the calibration stars appear to be outside the FoV of M2FS (centered on a Shack-Hartmann star). The coordinates of the Shack-Hartmann star were provided by XiaoXu (postdoc working with XianZhong) on July 29, whereas the coordinates of the flux calibration stars were obtained from DS9 catalog tool.

I am now in the process of understanding and fixing the issue. I had a meeting with Mario Mateo on Sept 13 and I am working on implementing the checks we discussed which have to do with understanding the coordinates reported by GAIA.
