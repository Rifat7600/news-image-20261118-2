"""Draw the 18 November 2026 world-news map: a world map with numbered
story pins and a legend. Writes entry.png (1024x1024) next to this file."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BANNER_H = 96
MAP_TOP = BANNER_H
MAP_BOTTOM = 700
LEGEND_TOP = MAP_BOTTOM

NAVY = (22, 50, 79)
NAVY_DARK = (16, 38, 60)
OCEAN = (220, 234, 245)
LAND = (142, 166, 187)
LAND_EDGE = (120, 145, 168)
RED = (214, 40, 40)
INK = (26, 43, 60)
GREY = (74, 90, 104)
LABEL = (102, 121, 138)
WHITE = (255, 255, 255)
BANNER_SUB = (185, 201, 216)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_BOLD = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", s)
F_REG = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", s)

# Equirectangular projection over the map panel.
def xy(lon, lat):
    x = 20 + (lon + 170) * 984 / 360
    y = MAP_TOP + (75 - lat) * (MAP_BOTTOM - MAP_TOP) / 130
    return (x, y)

def poly(draw, points, fill=LAND, outline=LAND_EDGE, width=2):
    draw.polygon([xy(lon, lat) for lon, lat in points],
                 fill=fill, outline=outline, width=width)

# Simplified continent outlines, in (longitude, latitude).
NORTH_AMERICA = [(-168, 66), (-155, 71), (-140, 70), (-130, 71), (-120, 72),
                 (-110, 73), (-95, 80), (-85, 76), (-80, 73), (-76, 62),
                 (-70, 58), (-65, 49), (-60, 47), (-65, 44), (-70, 42),
                 (-75, 38), (-76, 35), (-80, 32), (-81, 26), (-84, 30),
                 (-90, 21), (-97, 16), (-94, 17), (-92, 15), (-86, 13),
                 (-83, 9), (-80, 8), (-79, 9), (-83, 10), (-90, 14),
                 (-95, 16), (-97, 16), (-105, 20), (-108, 23), (-112, 29),
                 (-117, 33), (-122, 37), (-124, 42), (-124, 48), (-130, 55),
                 (-140, 60), (-152, 58), (-162, 55), (-168, 66)]
GREENLAND = [(-58, 64), (-52, 60), (-44, 60), (-32, 68), (-22, 70),
             (-25, 76), (-40, 78), (-55, 76), (-60, 74), (-58, 64)]
SOUTH_AMERICA = [(-79, 9), (-76, 10), (-72, 12), (-64, 10), (-60, 8),
                 (-52, 5), (-50, 0), (-44, -3), (-35, -8), (-38, -15),
                 (-40, -22), (-48, -28), (-52, -33), (-58, -38), (-62, -41),
                 (-65, -45), (-68, -50), (-70, -54), (-73, -50), (-73, -44),
                 (-73, -37), (-72, -30), (-71, -20), (-75, -15), (-80, -6),
                 (-81, -1), (-80, 4), (-79, 9)]
AFRICA = [(-17, 15), (-16, 20), (-10, 29), (-6, 33), (0, 36), (10, 37),
          (11, 34), (20, 32), (25, 32), (30, 31), (32, 31), (34, 28),
          (37, 22), (39, 18), (43, 12), (48, 11), (51, 11), (51, 2),
          (48, -2), (44, -8), (40, -12), (36, -18), (35, -22), (32, -26),
          (28, -33), (20, -35), (16, -29), (13, -18), (12, -12), (9, -1),
          (9, 4), (4, 6), (-8, 5), (-13, 8), (-17, 12), (-17, 15)]
EUROPE = [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-2, 48), (-4, 48),
          (-1, 50), (2, 51), (4, 53), (7, 54), (8, 57), (10, 59), (12, 58),
          (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (30, 70),
          (28, 71), (25, 71), (21, 70), (18, 69), (14, 67), (12, 64),
          (8, 62), (5, 60), (5, 58), (8, 55), (10, 54), (8, 53), (3, 52),
          (0, 50), (-3, 48), (-5, 46), (-2, 44), (-9, 43), (-10, 40),
          (-10, 36)]
BRITAIN = [(-5, 50), (-3, 53), (-5, 55), (-3, 58), (-1, 57), (0, 53),
           (-1, 51), (-3, 50), (-5, 50)]
ASIA = [(30, 70), (35, 68), (40, 68), (48, 68), (55, 69), (62, 70),
        (70, 72), (75, 73), (80, 73), (90, 75), (100, 77), (110, 76),
        (120, 73), (130, 72), (140, 72), (150, 70), (160, 70), (170, 67),
        (178, 65), (178, 62), (170, 60), (162, 56), (158, 52), (156, 50),
        (150, 45), (142, 45), (140, 40), (138, 38), (135, 35), (132, 33),
        (130, 32), (127, 35), (126, 38), (122, 38), (122, 32), (120, 28),
        (118, 25), (114, 22), (110, 20), (108, 18), (106, 10), (104, 9),
        (101, 7), (100, 10), (98, 12), (97, 16), (94, 17), (92, 21),
        (90, 22), (88, 22), (86, 20), (83, 17), (80, 14), (77, 8),
        (76, 10), (74, 15), (72, 20), (68, 23), (66, 25), (62, 25),
        (58, 26), (56, 27), (53, 28), (51, 28), (50, 30), (48, 30),
        (44, 29), (42, 30), (40, 31), (38, 33), (36, 36), (34, 36),
        (33, 37), (30, 36), (30, 38), (28, 41), (28, 44), (30, 46),
        (28, 48), (28, 50), (30, 55), (30, 60), (30, 70)]
AUSTRALIA = [(113, -22), (114, -28), (115, -33), (118, -35), (124, -33),
             (129, -32), (132, -32), (135, -35), (137, -35), (140, -38),
             (143, -39), (146, -39), (149, -37), (150, -37), (153, -32),
             (153, -27), (151, -24), (148, -20), (146, -19), (144, -15),
             (142, -11), (141, -13), (138, -12), (136, -12), (135, -15),
             (132, -12), (130, -13), (128, -14), (126, -14), (124, -15),
             (122, -17), (120, -20), (117, -20), (114, -22)]
NEW_GUINEA = [(131, -1), (136, -2), (141, -3), (146, -6), (150, -8),
              (150, -10), (146, -8), (142, -8), (138, -7), (134, -4),
              (131, -1)]
JAPAN = [(130, 31), (131, 33), (133, 34), (135, 34), (137, 35), (139, 36),
         (140, 38), (141, 40), (141, 42), (142, 44), (143, 43), (141, 41),
         (140, 39), (139, 37), (137, 36), (135, 34), (133, 33), (131, 32),
         (130, 31)]
BORNEO = [(109, 1), (113, 4), (117, 6), (118, 2), (117, -2), (114, -3),
          (110, -2), (109, 1)]
SUMATRA = [(95, 5), (98, 3), (100, 0), (103, -2), (105, -4), (104, -5),
           (102, -3), (99, 1), (96, 4), (95, 5)]
JAVA = [(105, -6), (108, -7), (111, -7), (114, -8), (114, -9), (111, -8),
        (108, -8), (105, -7), (105, -6)]
MADAGASCAR = [(44, -16), (47, -15), (50, -16), (50, -20), (47, -24),
              (44, -25), (43, -22), (43, -18), (44, -16)]
NEW_ZEALAND = [(167, -45), (170, -43), (173, -41), (175, -38), (177, -38),
               (175, -40), (173, -42), (170, -44), (167, -45)]
ICELAND = [(-22, 64), (-18, 63), (-14, 64), (-15, 66), (-20, 66), (-22, 64)]

CONTINENTS = [ASIA, NORTH_AMERICA, SOUTH_AMERICA, AFRICA, EUROPE, AUSTRALIA,
              GREENLAND, BRITAIN, NEW_GUINEA, JAPAN, BORNEO, SUMATRA, JAVA,
              MADAGASCAR, NEW_ZEALAND, ICELAND]

# (number, lon, lat) of each story pin.
PINS = [
    (1, 114, 22.5),    # Shenzhen: Trump-Xi-Putin
    (2, 47.5, 29.3),   # Kuwait: Iran war
    (3, 34.5, 31.5),   # Gaza
    (4, 121, 14.6),    # Manila: Quad
    (5, 85, 16),       # Bay of Bengal: Cyclone Akvan
    (6, -152, 64),     # Alaska: Peltola Senate win
    (7, 147, -6.3),    # Papua New Guinea: quake
    (8, 105, 60),      # Siberia: plane crash
]

# (headline, place) legend lines, one per pin.
LEGEND = [
    ("Trump, Xi and Putin meet in Shenzhen", "first-ever trilateral at APEC"),
    ("Iran war escalates", "drones hit US base in Kuwait; US strikes Qeshm"),
    ("Israel opens Gaza operation", "concentrated push in three central areas"),
    ("Quad leaders meet in Manila", "US\u2013Philippines trade and defence deal"),
    ("Cyclone Akvan strengthens", "Bay of Bengal, heads for Andhra coast"),
    ("Peltola wins US Senate seat", "Democrat takes Alaska"),
    ("Magnitude 6 earthquake", "strikes Papua New Guinea"),
    ("Russian military plane crashes", "19 killed in Siberia"),
]

OCEAN_LABELS = [
    ("PACIFIC OCEAN", -140, -30),
    ("ATLANTIC OCEAN", -35, -12),
    ("INDIAN OCEAN", 75, -30),
]
LAND_LABELS = [
    ("NORTH AMERICA", -100, 48),
    ("SOUTH AMERICA", -62, -30),
    ("AFRICA", 17, 5),
    ("EUROPE", 15, 52),
    ("ASIA", 85, 50),
    ("AUSTRALIA", 134, -25),
]


def draw_pin(draw, cx, cy, number):
    r = 15
    draw.ellipse([cx - r - 1, cy - r + 1, cx + r + 1, cy + r + 3],
                 fill=(90, 110, 130))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED,
                 outline=WHITE, width=3)
    font = F_BOLD(17)
    text = str(number)
    w = draw.textlength(text, font=font)
    draw.text((cx - w / 2, cy - 12), text, font=font, fill=WHITE)


def main():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    # --- banner ---
    draw.rectangle([0, 0, W, BANNER_H], fill=NAVY)
    title = "THE WORLD \u2014 18 NOVEMBER 2026"
    tfont = F_BOLD(44)
    tw = draw.textlength(title, font=tfont)
    draw.text(((W - tw) / 2, 14), title, font=tfont, fill=WHITE)
    sub = "Wednesday's top stories, mapped"
    sfont = F_REG(21)
    sw = draw.textlength(sub, font=sfont)
    draw.text(((W - sw) / 2, 64), sub, font=sfont, fill=BANNER_SUB)

    # --- map panel ---
    draw.rectangle([0, MAP_TOP, W, MAP_BOTTOM], fill=OCEAN)
    # faint graticule
    for lon in range(-150, 181, 30):
        x, _ = xy(lon, 0)
        draw.line([(x, MAP_TOP), (x, MAP_BOTTOM)], fill=(255, 255, 255), width=1)
    for lat in range(-30, 76, 30):
        _, y = xy(0, lat)
        draw.line([(0, y), (W, y)], fill=(255, 255, 255), width=1)
    for shape in CONTINENTS:
        poly(draw, shape)
    for text, lon, lat in OCEAN_LABELS:
        font = F_REG(16)
        x, y = xy(lon, lat)
        w = draw.textlength(text, font=font)
        draw.text((x - w / 2, y - 8), text, font=font, fill=LABEL)
    for text, lon, lat in LAND_LABELS:
        font = F_BOLD(15)
        x, y = xy(lon, lat)
        w = draw.textlength(text, font=font)
        draw.text((x - w / 2, y - 8), text, font=font, fill=(91, 114, 133))
    for number, lon, lat in PINS:
        cx, cy = xy(lon, lat)
        draw_pin(draw, cx, cy, number)

    # --- legend ---
    draw.rectangle([0, MAP_BOTTOM, W, H], fill=WHITE)
    draw.line([(0, MAP_BOTTOM), (W, MAP_BOTTOM)], fill=(200, 210, 218), width=2)
    hfont = F_BOLD(20)
    draw.text((36, 710), "TODAY'S TOP STORIES", font=hfont, fill=NAVY)
    draw.line([(36, 742), (W - 36, 742)], fill=(200, 210, 218), width=1)
    bold = F_BOLD(21)
    reg = F_REG(21)
    y = 752
    for i, (head, place) in enumerate(LEGEND, start=1):
        cy = y + 15
        draw.ellipse([36 - 12, cy - 12, 36 + 12, cy + 12], fill=RED)
        nfont = F_BOLD(16)
        num = str(i)
        nw = draw.textlength(num, font=nfont)
        draw.text((36 - nw / 2, cy - 11), num, font=nfont, fill=WHITE)
        draw.text((62, y), head, font=bold, fill=INK)
        hw = draw.textlength(head, font=bold)
        draw.text((62 + hw + 8, y), "\u00b7  " + place, font=reg, fill=GREY)
        y += 30
    sfont2 = F_REG(13)
    src = ("Sources: Anadolu \u00b7 Outlook India \u00b7 Times of India \u00b7 "
           "Just Security \u00b7 Korea Herald \u00b7 Japan Times \u00b7 Economic Times")
    draw.text((36, 1000), src, font=sfont2, fill=LABEL)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
