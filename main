
import math
import random
import sys

import pygame


# The game always draws at this logical resolution, then scales cleanly
# to the user's actual fullscreen resolution.
WIDTH, HEIGHT = 900, 600
FPS = 60

PINK = (255, 105, 180)
HOT_PINK = (238, 64, 137)
RED = (225, 55, 76)
DARK = (38, 29, 47)
WHITE = (255, 255, 255)
PURPLE = (131, 83, 180)
YELLOW = (255, 222, 85)
CYAN = (67, 240, 229)
BLACK = (8, 7, 14)


REALITIES = [
    {
        "min_level": 1,
        "key": "bubblegum",
        "name": "BUBBLEGUM DAYDREAM",
        "subtitle": "soft launch // emotional tutorial",
        "accent": HOT_PINK,
        "panel": (255, 248, 253),
        "text": DARK,
        "font_pack": "pixel",
        "outfit": (131, 83, 180),
    },
    {
        "min_level": 4,
        "key": "club",
        "name": "BASEMENT TECHNO",
        "subtitle": "142 BPM // no photos // feelings allowed",
        "accent": CYAN,
        "panel": (19, 14, 31),
        "text": WHITE,
        "font_pack": "club",
        "outfit": (25, 22, 34),
    },
    {
        "min_level": 7,
        "key": "milan",
        "name": "MILAN AFTERGLOW",
        "subtitle": "tram 9 // aperitivo hour // duomo in the distance",
        "accent": (231, 76, 60),
        "panel": (255, 243, 219),
        "text": (61, 38, 39),
        "font_pack": "milan",
        "outfit": (170, 58, 63),
    },
    {
        "min_level": 10,
        "key": "bookstore",
        "name": "MIDNIGHT BOOKSTORE",
        "subtitle": "open late // theory aisle // unresolved tension",
        "accent": (255, 184, 96),
        "panel": (48, 32, 30),
        "text": (255, 241, 216),
        "font_pack": "book",
        "outfit": (118, 62, 52),
    },
    {
        "min_level": 13,
        "key": "metro",
        "name": "LAST TRAIN HOME",
        "subtitle": "platform 3 // rain outside // one earbud each",
        "accent": (102, 198, 255),
        "panel": (20, 30, 51),
        "text": WHITE,
        "font_pack": "terminal",
        "outfit": (43, 73, 116),
    },
    {
        "min_level": 16,
        "key": "rooftop",
        "name": "NEON ROOFTOP",
        "subtitle": "05:17 // city asleep // secret ending nearby",
        "accent": (255, 119, 154),
        "panel": (33, 21, 54),
        "text": WHITE,
        "font_pack": "future",
        "outfit": (171, 61, 113),
    },
    {
        "min_level": 19,
        "key": "dragon",
        "name": "DRAGON CATHEDRAL",
        "subtitle": "heartfire // stained glass // final reality",
        "accent": (255, 91, 82),
        "panel": (24, 15, 28),
        "text": WHITE,
        "font_pack": "future",
        "outfit": (110, 31, 56),
    },
]


SCENE_DIALOGUE = {
    "bubblegum": [
        "Okay... that was actually kind of smooth.",
        "Affection rising. Dangerous.",
        "You caught that like a protagonist.",
        "Fine. You're a little bit charming.",
        "This tutorial is becoming suspiciously romantic.",
    ],
    "club": [
        "The bassline knows our attachment style.",
        "No talking. Just eye contact at 142 BPM.",
        "You found me next to the left speaker.",
        "Affection is peaking. The DJ did this.",
        "Red flags are harder to see under strobe lights.",
    ],
    "milan": [
        "Meet me where the yellow tram catches the sunset.",
        "Aperitivo is just emotional support with ice.",
        "The Duomo is judging our situationship beautifully.",
        "You brought me a heart. I brought unnecessary sunglasses.",
        "Milan looks cinematic when nobody knows where they are going.",
    ],
    "bookstore": [
        "Meet me between philosophy and speculative fiction.",
        "You keep catching hearts. I keep pretending to read.",
        "This chapter has unbearable romantic tension.",
        "Quiet, please. My feelings are catalogued incorrectly.",
        "I left a note inside the book you recommended.",
    ],
    "metro": [
        "Last train. Bad decisions. Excellent soundtrack.",
        "One earbud each. No skipping my song.",
        "The windows make the city look fictional.",
        "Do not miss the heart or the connection.",
        "We are definitely taking this train too far.",
    ],
    "rooftop": [
        "The city looks harmless from up here.",
        "Secret ending energy detected.",
        "Sunrise is just the afterparty loading screen.",
        "You made it past every alternate reality.",
        "One more heart and the credits might roll.",
    ],
    "dragon": [
        "The cathedral runs entirely on dramatic tension.",
        "Heartfire is technically a renewable energy source.",
        "The dragon has excellent taste and terrible boundaries.",
        "This is no longer a meet-cute. This is a boss fight.",
        "Catch feelings later. Cast spells now.",
    ],
}


LEVEL_TITLES = [
    "STRANGER DANGER",
    "CRUSH BUFFERING",
    "DATEABLE ENTITY",
    "ROM-COM PROTOCOL",
    "BASSLINE BONDING",
    "STROBE-LIGHT CONFESSION",
    "AFTERPARTY LORE",
    "EMOTIONAL REMIX",
    "CLOSING SET",
    "MARGINALIA MODE",
    "THEORY AISLE TENSION",
    "DOG-EARED DESTINY",
    "CHECKOUT DESK YEARNING",
    "LAST PAGE PANIC",
    "PLATFORM CHEMISTRY",
    "RAIN-WINDOW ROUTE",
    "ONE EARBUD EACH",
    "MISSED CONNECTION",
    "FINAL TRANSFER",
    "ROOFTOP AFTERGLOW",
    "SECRET ENDING",
]


def clamp(value, low, high):
    return max(low, min(high, value))


def reality_for_level(level):
    result = REALITIES[0]
    for reality in REALITIES:
        if level >= reality["min_level"]:
            result = reality
    return result


def font_from_candidates(candidates, size, bold=False, italic=False):
    joined = ",".join(candidates)
    font = pygame.font.SysFont(joined, size, bold=bold, italic=italic)
    return font


def build_font_packs():
    return {
        "pixel": {
            "title": font_from_candidates(
                ["Lucida Console", "Consolas", "Courier New"], 45, bold=True
            ),
            "large": font_from_candidates(
                ["Consolas", "Lucida Console", "Courier New"], 29, bold=True
            ),
            "body": font_from_candidates(
                ["Consolas", "Lucida Console", "Courier New"], 21, bold=True
            ),
            "small": font_from_candidates(
                ["Consolas", "Lucida Console", "Courier New"], 16, bold=True
            ),
        },
        "club": {
            "title": font_from_candidates(
                ["Impact", "Arial Black", "Franklin Gothic Heavy"], 49
            ),
            "large": font_from_candidates(
                ["Arial Black", "Impact", "Consolas"], 28
            ),
            "body": font_from_candidates(
                ["Lucida Console", "Consolas", "Courier New"], 20, bold=True
            ),
            "small": font_from_candidates(
                ["Lucida Console", "Consolas", "Courier New"], 15, bold=True
            ),
        },
        "milan": {
            "title": font_from_candidates(
                ["Bodoni MT", "Georgia", "Times New Roman"], 45, bold=True
            ),
            "large": font_from_candidates(
                ["Bodoni MT", "Georgia", "Cambria"], 28, bold=True
            ),
            "body": font_from_candidates(
                ["Aptos", "Segoe UI", "Arial"], 20, bold=True
            ),
            "small": font_from_candidates(
                ["Aptos", "Segoe UI", "Arial"], 15, italic=True
            ),
        },
        "book": {
            "title": font_from_candidates(
                ["Georgia", "Times New Roman", "Cambria"], 43, bold=True
            ),
            "large": font_from_candidates(
                ["Georgia", "Cambria", "Times New Roman"], 27, bold=True
            ),
            "body": font_from_candidates(
                ["Georgia", "Cambria", "Times New Roman"], 20
            ),
            "small": font_from_candidates(
                ["Georgia", "Cambria", "Times New Roman"], 16, italic=True
            ),
        },
        "terminal": {
            "title": font_from_candidates(
                ["Bahnschrift", "Arial Narrow", "Consolas"], 43, bold=True
            ),
            "large": font_from_candidates(
                ["Bahnschrift", "Trebuchet MS", "Consolas"], 27, bold=True
            ),
            "body": font_from_candidates(
                ["Consolas", "Lucida Console", "Courier New"], 20, bold=True
            ),
            "small": font_from_candidates(
                ["Consolas", "Lucida Console", "Courier New"], 15
            ),
        },
        "future": {
            "title": font_from_candidates(
                ["Segoe UI Black", "Arial Black", "Impact"], 44, bold=True
            ),
            "large": font_from_candidates(
                ["Bahnschrift", "Segoe UI", "Arial"], 28, bold=True
            ),
            "body": font_from_candidates(
                ["Bahnschrift", "Segoe UI", "Arial"], 20, bold=True
            ),
            "small": font_from_candidates(
                ["Bahnschrift", "Segoe UI", "Arial"], 15
            ),
        },
    }


def draw_text(surface, text, font, color, pos, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surface.blit(image, rect)


def draw_heart(surface, x, y, size, color=PINK):
    radius = max(2, size // 4)
    pygame.draw.circle(surface, color, (x - radius, y - radius // 2), radius)
    pygame.draw.circle(surface, color, (x + radius, y - radius // 2), radius)
    pygame.draw.polygon(
        surface,
        color,
        [
            (x - size // 2, y - radius // 2),
            (x + size // 2, y - radius // 2),
            (x, y + size // 2),
        ],
    )


def draw_red_flag(surface, rect, pole_color=DARK):
    pole_x = rect.left + rect.width // 3
    pygame.draw.line(
        surface, pole_color, (pole_x, rect.top), (pole_x, rect.bottom), 5
    )
    pygame.draw.polygon(
        surface,
        RED,
        [
            (pole_x, rect.top + 3),
            (rect.right, rect.top + rect.height // 3),
            (pole_x, rect.top + rect.height // 2),
        ],
    )


def draw_vertical_gradient(surface, top_color, bottom_color):
    for y in range(HEIGHT):
        ratio = y / max(1, HEIGHT - 1)
        color = tuple(
            int(top_color[i] * (1 - ratio) + bottom_color[i] * ratio)
            for i in range(3)
        )
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))


def draw_bubblegum_world(surface, ticks):
    draw_vertical_gradient(surface, (255, 216, 237), (255, 238, 247))
    pygame.draw.circle(surface, (255, 245, 195), (110, 103), 62)
    pygame.draw.circle(surface, (255, 232, 244), (772, 112), 82)

    drift = int(math.sin(ticks / 1300) * 10)
    for cx, cy in [(205 + drift, 125), (665 - drift, 190), (405, 82)]:
        pygame.draw.circle(surface, WHITE, (cx, cy), 24)
        pygame.draw.circle(surface, WHITE, (cx + 25, cy - 8), 30)
        pygame.draw.circle(surface, WHITE, (cx + 53, cy), 23)
        pygame.draw.rect(surface, WHITE, (cx, cy, 55, 25))

    # Tiny dreamy skyline.
    for index, height in enumerate([58, 84, 45, 70, 95, 52, 77, 62, 89]):
        x = index * 104
        pygame.draw.rect(
            surface,
            (247, 191, 222),
            (x, HEIGHT - 42 - height, 78, height),
        )
        for wx in range(x + 12, x + 68, 22):
            pygame.draw.rect(
                surface,
                (255, 239, 170),
                (wx, HEIGHT - 34 - height, 10, 13),
                border_radius=2,
            )

    pygame.draw.rect(surface, (255, 242, 248), (0, HEIGHT - 42, WIDTH, 42))
    pygame.draw.line(surface, HOT_PINK, (0, HEIGHT - 42), (WIDTH, HEIGHT - 42), 3)


def draw_club_world(surface, ticks):
    pulse = (math.sin(ticks / 105) + 1) / 2
    surface.fill((12, 8, 24))

    # Back wall and pulsing neon frame.
    pygame.draw.rect(surface, (27, 16, 42), (0, 0, WIDTH, 400))
    neon = (
        int(70 + 100 * pulse),
        int(150 + 95 * (1 - pulse)),
        235,
    )
    pygame.draw.rect(surface, neon, (82, 72, 736, 260), 5)
    pygame.draw.rect(surface, HOT_PINK, (101, 91, 698, 222), 2)

    # Laser lines.
    laser_shift = int((ticks / 9) % WIDTH)
    pygame.draw.line(surface, CYAN, (0, 145), (laser_shift, 390), 2)
    pygame.draw.line(surface, HOT_PINK, (WIDTH, 105), (WIDTH - laser_shift, 390), 2)
    pygame.draw.line(surface, (168, 80, 255), (120, 0), (480, 380), 2)

    # Disco ball.
    pygame.draw.circle(surface, (190, 198, 226), (450, 52), 30)
    pygame.draw.line(surface, (130, 134, 160), (450, 0), (450, 22), 3)
    for x in range(430, 471, 10):
        pygame.draw.line(surface, WHITE, (x, 29), (x, 75), 1)
    for y in range(34, 73, 10):
        pygame.draw.line(surface, WHITE, (423, y), (477, y), 1)

    # Speakers.
    for x in (35, 775):
        pygame.draw.rect(surface, (18, 16, 24), (x, 252, 90, 216))
        pygame.draw.rect(surface, (70, 60, 86), (x, 252, 90, 216), 3)
        pygame.draw.circle(surface, (8, 7, 12), (x + 45, 318), 30)
        pygame.draw.circle(surface, neon, (x + 45, 318), 16, 3)
        pygame.draw.circle(surface, (8, 7, 12), (x + 45, 405), 38)
        pygame.draw.circle(surface, HOT_PINK, (x + 45, 405), 22, 3)

    # Equalizer.
    for index in range(22):
        bar_height = 18 + int(
            (math.sin(ticks / 130 + index * 0.75) + 1) * 25
        )
        pygame.draw.rect(
            surface,
            CYAN if index % 2 == 0 else HOT_PINK,
            (167 + index * 26, 350 - bar_height, 13, bar_height),
        )

    # Perspective dance floor.
    pygame.draw.polygon(
        surface,
        (20, 14, 34),
        [(110, 390), (790, 390), (900, 600), (0, 600)],
    )
    for y in range(400, 601, 35):
        pygame.draw.line(surface, (85, 45, 108), (0, y), (WIDTH, y), 1)
    for x in range(-200, 1101, 80):
        pygame.draw.line(surface, (48, 114, 122), (450, 390), (x, 600), 1)



def draw_milan_world(surface, ticks):
    # Warm aperitivo sunset.
    draw_vertical_gradient(surface, (255, 175, 136), (109, 67, 111))

    # Sun behind the skyline.
    pygame.draw.circle(surface, (255, 224, 157), (720, 126), 68)

    # Duomo-inspired silhouette: intentionally stylised rather than architectural.
    base_y = 362
    stone = (71, 55, 72)
    pygame.draw.rect(surface, stone, (310, 235, 280, 127))

    # Central roof and spires.
    pygame.draw.polygon(
        surface,
        stone,
        [(310, 235), (365, 195), (405, 230), (450, 160),
         (495, 230), (535, 195), (590, 235)],
    )
    for x, height in [(326, 66), (358, 92), (393, 72), (450, 125),
                      (507, 72), (542, 92), (574, 66)]:
        pygame.draw.polygon(
            surface,
            stone,
            [(x - 9, 235), (x, 235 - height), (x + 9, 235)],
        )

    # Gothic-ish windows.
    for x in range(335, 575, 38):
        pygame.draw.ellipse(surface, (224, 164, 120), (x, 276, 17, 43))
        pygame.draw.rect(surface, stone, (x, 298, 17, 22))

    # Side buildings.
    buildings = [
        (0, 280, 168, 145),
        (170, 302, 120, 123),
        (610, 276, 150, 149),
        (762, 310, 138, 115),
    ]
    for bx, by, bw, bh in buildings:
        pygame.draw.rect(surface, (52, 42, 60), (bx, by, bw, bh))
        for wy in range(by + 20, by + bh - 12, 30):
            for wx in range(bx + 17, bx + bw - 12, 28):
                pygame.draw.rect(surface, (255, 196, 115), (wx, wy, 10, 13))

    # Tram wires.
    pygame.draw.line(surface, (39, 33, 43), (0, 210), (900, 260), 2)
    pygame.draw.line(surface, (39, 33, 43), (0, 255), (900, 202), 2)
    pygame.draw.line(surface, (39, 33, 43), (480, 205), (480, 365), 2)

    # Moving classic yellow tram.
    tram_x = int((ticks / 16) % 1120) - 220
    tram_y = 386
    pygame.draw.rect(surface, (224, 174, 41), (tram_x, tram_y, 214, 91), border_radius=9)
    pygame.draw.rect(surface, (96, 62, 42), (tram_x, tram_y, 214, 91), 4, border_radius=9)
    pygame.draw.rect(surface, (47, 75, 88), (tram_x + 14, tram_y + 13, 48, 37))
    pygame.draw.rect(surface, (47, 75, 88), (tram_x + 70, tram_y + 13, 58, 37))
    pygame.draw.rect(surface, (47, 75, 88), (tram_x + 136, tram_y + 13, 62, 37))
    pygame.draw.line(surface, (96, 62, 42), (tram_x + 107, tram_y), (tram_x + 107, tram_y + 91), 3)
    pygame.draw.circle(surface, (27, 25, 29), (tram_x + 49, tram_y + 91), 14)
    pygame.draw.circle(surface, (27, 25, 29), (tram_x + 165, tram_y + 91), 14)
    pygame.draw.line(surface, (48, 39, 45), (tram_x + 107, tram_y), (tram_x + 132, tram_y - 46), 3)
    pygame.draw.line(surface, (48, 39, 45), (tram_x + 132, tram_y - 46), (tram_x + 154, tram_y), 3)

    # Street and aperitivo tables.
    pygame.draw.rect(surface, (55, 42, 52), (0, 477, WIDTH, 123))
    pygame.draw.line(surface, (234, 182, 95), (0, 477), (WIDTH, 477), 4)

    for table_x in (105, 780):
        pygame.draw.ellipse(surface, (92, 53, 43), (table_x - 42, 505, 84, 19))
        pygame.draw.line(surface, (92, 53, 43), (table_x, 519), (table_x, 576), 5)
        pygame.draw.circle(surface, (226, 75, 58), (table_x - 17, 499), 10)
        pygame.draw.rect(surface, (224, 214, 189), (table_x + 10, 486, 5, 19))
        pygame.draw.polygon(
            surface,
            (230, 108, 55),
            [(table_x + 2, 486), (table_x + 23, 486), (table_x + 17, 500), (table_x + 8, 500)],
        )

def draw_bookstore_world(surface, ticks):
    draw_vertical_gradient(surface, (55, 33, 35), (30, 22, 27))

    # Shelves and book spines.
    shelf_y_positions = [112, 238, 364]
    book_colors = [
        (148, 67, 58),
        (91, 111, 79),
        (179, 122, 61),
        (84, 86, 126),
        (125, 75, 105),
        (182, 154, 102),
    ]
    for shelf_y in shelf_y_positions:
        pygame.draw.rect(surface, (72, 43, 31), (18, shelf_y, 864, 14))
        x = 30
        while x < 870:
            width = random.Random(x + shelf_y).randint(13, 24)
            height = random.Random(x * 3 + shelf_y).randint(54, 94)
            color = book_colors[(x // 17 + shelf_y) % len(book_colors)]
            pygame.draw.rect(
                surface,
                color,
                (x, shelf_y - height, width, height),
                border_radius=2,
            )
            pygame.draw.line(
                surface,
                (235, 205, 151),
                (x + 4, shelf_y - height + 9),
                (x + width - 4, shelf_y - height + 9),
                1,
            )
            x += width + 5

    # Window with moon and rain.
    pygame.draw.rect(surface, (21, 29, 49), (351, 55, 198, 145))
    pygame.draw.rect(surface, (184, 148, 99), (351, 55, 198, 145), 5)
    pygame.draw.circle(surface, (255, 238, 186), (502, 91), 28)
    for index in range(15):
        rx = 365 + (index * 37 + int(ticks / 22)) % 170
        ry = 70 + (index * 29 + int(ticks / 13)) % 115
        pygame.draw.line(surface, (104, 155, 194), (rx, ry), (rx - 6, ry + 18), 1)

    # Warm reading lamps.
    for lamp_x in (170, 730):
        pygame.draw.circle(surface, (255, 201, 112), (lamp_x, 345), 66)
        pygame.draw.circle(surface, (255, 219, 145), (lamp_x, 345), 45)
        pygame.draw.polygon(
            surface,
            (101, 63, 45),
            [(lamp_x - 28, 325), (lamp_x + 28, 325), (lamp_x + 15, 365), (lamp_x - 15, 365)],
        )
        pygame.draw.line(surface, (70, 45, 36), (lamp_x, 365), (lamp_x, 511), 5)

    pygame.draw.rect(surface, (92, 58, 43), (0, 514, WIDTH, 86))
    for x in range(0, WIDTH, 74):
        pygame.draw.line(surface, (61, 42, 36), (x, 514), (x + 35, 600), 2)


def draw_metro_world(surface, ticks):
    surface.fill((10, 19, 35))
    pygame.draw.rect(surface, (24, 39, 62), (0, 0, WIDTH, 420))

    # Tunnel lights.
    light_offset = int((ticks / 6) % 160)
    for x in range(-160 + light_offset, WIDTH + 160, 160):
        pygame.draw.rect(surface, (166, 218, 255), (x, 55, 82, 9))
        pygame.draw.rect(surface, (47, 75, 101), (x, 66, 82, 3))

    # Train windows.
    for x in range(70, 831, 190):
        pygame.draw.rect(surface, (13, 24, 43), (x, 132, 150, 116))
        pygame.draw.rect(surface, (92, 157, 195), (x, 132, 150, 116), 4)
        # Moving rain/city reflections.
        for index in range(6):
            streak_x = x + 12 + ((index * 33 + int(ticks / 8)) % 126)
            pygame.draw.line(
                surface,
                (76, 112, 156),
                (streak_x, 143),
                (streak_x - 11, 232),
                2,
            )

    # Route line.
    pygame.draw.line(surface, (120, 137, 159), (115, 305), (785, 305), 5)
    stops = ["YOU", "MAYBE", "US", "HOME"]
    for index, stop in enumerate(stops):
        sx = 145 + index * 205
        pygame.draw.circle(surface, (255, 203, 89), (sx, 305), 9)
        tiny = pygame.font.SysFont("consolas", 13, bold=True)
        draw_text(surface, stop, tiny, WHITE, (sx, 325), center=True)

    # Platform and warning line.
    pygame.draw.rect(surface, (54, 60, 69), (0, 420, WIDTH, 180))
    pygame.draw.rect(surface, (248, 200, 62), (0, 449, WIDTH, 10))
    for x in range(0, WIDTH, 48):
        pygame.draw.rect(surface, (72, 77, 85), (x, 470, 45, 45), 1)


def draw_rooftop_world(surface, ticks):
    draw_vertical_gradient(surface, (29, 18, 58), (246, 112, 145))

    # Stars slowly fade with the implied sunrise.
    for index in range(55):
        sx = (index * 137) % WIDTH
        sy = 22 + (index * 83) % 275
        brightness = 155 + (index * 17) % 100
        pygame.draw.circle(
            surface,
            (brightness, brightness, min(255, brightness + 20)),
            (sx, sy),
            1 if index % 3 else 2,
        )

    # Neon sun.
    sun_y = 180 + int(math.sin(ticks / 2500) * 7)
    pygame.draw.circle(surface, (255, 191, 151), (730, sun_y), 71)
    for stripe in range(-48, 49, 16):
        pygame.draw.line(
            surface,
            (235, 104, 140),
            (670, sun_y + stripe),
            (790, sun_y + stripe),
            4,
        )

    # City silhouette.
    heights = [95, 160, 120, 190, 115, 145, 205, 130, 175, 105, 150]
    for index, height in enumerate(heights):
        x = index * 88
        pygame.draw.rect(surface, (24, 22, 43), (x, 440 - height, 74, height))
        for wy in range(440 - height + 18, 430, 27):
            for wx in range(x + 12, x + 63, 22):
                if (wx + wy + index) % 3:
                    pygame.draw.rect(surface, (255, 177, 111), (wx, wy, 7, 9))

    # Rooftop.
    pygame.draw.rect(surface, (24, 22, 38), (0, 440, WIDTH, 160))
    pygame.draw.line(surface, (255, 112, 169), (0, 440), (WIDTH, 440), 4)
    pygame.draw.rect(surface, (35, 31, 50), (72, 392, 74, 48))
    pygame.draw.line(surface, (35, 31, 50), (108, 392), (108, 330), 5)
    pygame.draw.line(surface, CYAN, (108, 330), (137, 344), 2)



def draw_dragon_world(surface, ticks):
    draw_vertical_gradient(surface, (34, 14, 42), (103, 29, 48))

    # Stained-glass moon/window.
    pygame.draw.circle(surface, (245, 165, 106), (450, 150), 105)
    pygame.draw.circle(surface, (55, 23, 63), (450, 150), 105, 8)
    pygame.draw.line(surface, (55, 23, 63), (345, 150), (555, 150), 6)
    pygame.draw.line(surface, (55, 23, 63), (450, 45), (450, 255), 6)
    pygame.draw.line(surface, (55, 23, 63), (376, 76), (524, 224), 5)
    pygame.draw.line(surface, (55, 23, 63), (524, 76), (376, 224), 5)

    # Cathedral arches.
    for arch_x in (75, 245, 655, 825):
        pygame.draw.rect(surface, (27, 19, 34), (arch_x - 55, 150, 110, 300))
        pygame.draw.arc(
            surface,
            (82, 48, 85),
            (arch_x - 55, 78, 110, 150),
            0,
            math.pi,
            7,
        )

    # Columns.
    for column_x in (135, 300, 600, 765):
        pygame.draw.rect(surface, (42, 27, 48), (column_x - 16, 92, 32, 391))
        pygame.draw.rect(surface, (86, 46, 79), (column_x - 24, 83, 48, 15))
        pygame.draw.rect(surface, (86, 46, 79), (column_x - 24, 475, 48, 15))

    # Floating embers.
    for index in range(28):
        ex = (index * 109 + int(ticks / 12)) % WIDTH
        ey = HEIGHT - ((index * 71 + int(ticks / 7)) % 410)
        pygame.draw.circle(
            surface,
            (255, 102 + index % 70, 63),
            (ex, ey),
            2 if index % 3 else 3,
        )

    # Stone floor with perspective.
    pygame.draw.polygon(
        surface,
        (27, 19, 31),
        [(90, 420), (810, 420), (900, 600), (0, 600)],
    )
    for y in range(430, 601, 34):
        pygame.draw.line(surface, (73, 39, 61), (0, y), (WIDTH, y), 1)
    for x in range(-180, 1081, 90):
        pygame.draw.line(surface, (61, 35, 58), (450, 420), (x, 600), 1)

    # Braziers.
    for bx in (96, 804):
        pygame.draw.rect(surface, (58, 40, 48), (bx - 18, 403, 36, 65))
        flame = 10 + int((math.sin(ticks / 110 + bx) + 1) * 6)
        pygame.draw.polygon(
            surface,
            (255, 91, 61),
            [(bx - 14, 407), (bx, 407 - flame * 2), (bx + 14, 407)],
        )
        pygame.draw.polygon(
            surface,
            (255, 203, 82),
            [(bx - 7, 407), (bx, 407 - flame), (bx + 7, 407)],
        )

def draw_reality(surface, reality, ticks):
    key = reality["key"]
    if key == "bubblegum":
        draw_bubblegum_world(surface, ticks)
    elif key == "club":
        draw_club_world(surface, ticks)
    elif key == "milan":
        draw_milan_world(surface, ticks)
    elif key == "bookstore":
        draw_bookstore_world(surface, ticks)
    elif key == "metro":
        draw_metro_world(surface, ticks)
    elif key == "rooftop":
        draw_rooftop_world(surface, ticks)
    else:
        draw_dragon_world(surface, ticks)


def draw_scanlines(surface, strength=24):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for y in range(0, HEIGHT, 4):
        pygame.draw.line(overlay, (0, 0, 0, strength), (0, y), (WIDTH, y))
    surface.blit(overlay, (0, 0))


def draw_waifu(surface, rect, reality, blink=False):
    """Original cartoon heroine whose styling changes with each reality."""
    cx = rect.centerx
    top = rect.top
    key = reality["key"]
    outfit = reality["outfit"]

    # Hair behind head.
    hair_color = {
        "bubblegum": (77, 44, 98),
        "club": (40, 25, 60),
        "milan": (70, 40, 47),
        "bookstore": (67, 40, 42),
        "metro": (31, 39, 66),
        "rooftop": (74, 37, 78),
        "dragon": (46, 20, 51),
    }[key]
    pygame.draw.ellipse(surface, hair_color, (cx - 52, top + 5, 104, 135))

    # Face.
    skin = (255, 220, 200)
    pygame.draw.ellipse(surface, skin, (cx - 39, top + 22, 78, 82))

    # Fringe.
    pygame.draw.polygon(
        surface,
        hair_color,
        [
            (cx - 42, top + 28),
            (cx - 22, top + 12),
            (cx - 8, top + 38),
            (cx + 7, top + 15),
            (cx + 22, top + 40),
            (cx + 43, top + 26),
            (cx + 31, top + 4),
            (cx - 30, top + 4),
        ],
    )

    # Eyes.
    if blink:
        pygame.draw.line(surface, DARK, (cx - 24, top + 60), (cx - 10, top + 60), 3)
        pygame.draw.line(surface, DARK, (cx + 10, top + 60), (cx + 24, top + 60), 3)
    else:
        pygame.draw.ellipse(surface, DARK, (cx - 25, top + 53, 13, 18))
        pygame.draw.ellipse(surface, DARK, (cx + 12, top + 53, 13, 18))
        pygame.draw.circle(surface, WHITE, (cx - 20, top + 57), 3)
        pygame.draw.circle(surface, WHITE, (cx + 17, top + 57), 3)

    pygame.draw.ellipse(surface, (255, 145, 160), (cx - 34, top + 72, 15, 7))
    pygame.draw.ellipse(surface, (255, 145, 160), (cx + 19, top + 72, 15, 7))
    pygame.draw.arc(surface, HOT_PINK, (cx - 9, top + 69, 18, 15), 0, math.pi, 2)

    # Reality-specific accessories.
    if key == "club":
        pygame.draw.line(surface, CYAN, (cx - 31, top + 55), (cx + 31, top + 55), 4)
        pygame.draw.rect(surface, (12, 12, 20), (cx - 30, top + 49, 23, 15), 2)
        pygame.draw.rect(surface, (12, 12, 20), (cx + 7, top + 49, 23, 15), 2)
    elif key == "milan":
        # Oversized sunglasses and a tiny red scarf.
        pygame.draw.ellipse(surface, (35, 28, 37), (cx - 33, top + 48, 27, 18))
        pygame.draw.ellipse(surface, (35, 28, 37), (cx + 6, top + 48, 27, 18))
        pygame.draw.line(surface, (35, 28, 37), (cx - 6, top + 56), (cx + 6, top + 56), 3)
        pygame.draw.polygon(
            surface,
            (226, 75, 58),
            [(cx - 26, top + 100), (cx + 26, top + 100), (cx + 12, top + 116), (cx - 12, top + 116)],
        )
    elif key == "bookstore":
        pygame.draw.circle(surface, DARK, (cx - 19, top + 61), 13, 2)
        pygame.draw.circle(surface, DARK, (cx + 19, top + 61), 13, 2)
        pygame.draw.line(surface, DARK, (cx - 6, top + 61), (cx + 6, top + 61), 2)
    elif key == "metro":
        # Headphones.
        pygame.draw.arc(surface, (112, 189, 235), (cx - 42, top + 32, 84, 65), math.pi, math.tau, 4)
        pygame.draw.rect(surface, (112, 189, 235), (cx - 46, top + 55, 9, 30), border_radius=4)
        pygame.draw.rect(surface, (112, 189, 235), (cx + 37, top + 55, 9, 30), border_radius=4)
    elif key == "rooftop":
        pygame.draw.polygon(
            surface,
            (255, 119, 154),
            [(cx + 28, top + 18), (cx + 52, top + 7), (cx + 44, top + 33)],
        )
    elif key == "dragon":
        # Tiny battle crown and cape clasp.
        pygame.draw.polygon(
            surface,
            (255, 197, 76),
            [
                (cx - 24, top + 21),
                (cx - 15, top + 3),
                (cx, top + 18),
                (cx + 15, top + 3),
                (cx + 24, top + 21),
            ],
        )
        pygame.draw.circle(surface, (255, 91, 82), (cx, top + 107), 7)

    # Outfit.
    pygame.draw.polygon(
        surface,
        outfit,
        [
            (cx - 33, top + 98),
            (cx + 33, top + 98),
            (cx + 55, rect.bottom),
            (cx - 55, rect.bottom),
        ],
    )

    collar = WHITE if key != "club" else CYAN
    pygame.draw.polygon(
        surface,
        collar,
        [(cx - 20, top + 99), (cx, top + 118), (cx + 20, top + 99)],
    )

    pygame.draw.rect(surface, skin, (cx - 31, rect.bottom - 5, 17, 25), border_radius=7)
    pygame.draw.rect(surface, skin, (cx + 14, rect.bottom - 5, 17, 25), border_radius=7)
    pygame.draw.ellipse(surface, DARK, (cx - 36, rect.bottom + 12, 28, 12))
    pygame.draw.ellipse(surface, DARK, (cx + 8, rect.bottom + 12, 28, 12))


class FallingItem:
    def __init__(self, kind, level):
        self.kind = kind
        self.size = 38 if kind == "heart" else 48
        self.x = random.randint(35, WIDTH - 35)
        self.y = -self.size
        self.speed = random.uniform(2.8, 4.4) + min(level - 1, 12) * 0.12
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = (self.x, self.y)

    def update(self):
        self.y += self.speed
        self.rect.center = (self.x, int(self.y))

    def draw(self, surface, reality):
        if self.kind == "heart":
            draw_heart(
                surface,
                self.rect.centerx,
                self.rect.centery,
                self.size,
                reality["accent"],
            )
        else:
            pole = WHITE if reality["key"] in ("club", "metro", "rooftop") else DARK
            draw_red_flag(surface, self.rect, pole)



class HeartBolt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.rect = pygame.Rect(0, 0, 20, 28)
        self.rect.center = (int(x), int(y))

    def update(self):
        self.y -= self.speed
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, surface, accent):
        pygame.draw.line(
            surface,
            WHITE,
            (int(self.x), int(self.y) + 12),
            (int(self.x), int(self.y) + 29),
            3,
        )
        draw_heart(surface, int(self.x), int(self.y), 18, accent)


class Fireball:
    def __init__(self, x, y, target_x, difficulty):
        self.x = float(x)
        self.y = float(y)
        dx = target_x - x
        distance = max(1.0, abs(dx))
        self.vx = clamp(dx / distance * (1.1 + difficulty * 0.08), -2.3, 2.3)
        self.vy = 3.1 + difficulty * 0.13
        self.rect = pygame.Rect(0, 0, 26, 30)
        self.rect.center = (int(self.x), int(self.y))

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 82, 56), self.rect.center, 13)
        pygame.draw.circle(surface, (255, 205, 76), self.rect.center, 7)
        pygame.draw.polygon(
            surface,
            (255, 112, 54),
            [
                (self.rect.centerx - 9, self.rect.centery - 9),
                (self.rect.centerx, self.rect.centery - 25),
                (self.rect.centerx + 9, self.rect.centery - 9),
            ],
        )


class DragonBoss:
    def __init__(self, stage, accent):
        self.stage = max(1, stage)
        self.accent = accent
        self.x = WIDTH // 2
        self.y = 142
        self.direction = random.choice([-1, 1])
        self.speed = min(4.2, 1.7 + self.stage * 0.18)
        self.max_health = 9 + self.stage * 3
        self.health = self.max_health
        self.fire_timer = 950
        self.hit_flash = 0
        self.rect = pygame.Rect(0, 0, 190, 112)
        self.rect.center = (self.x, self.y)

    def update(self, dt, target_x, fireballs):
        self.x += self.direction * self.speed
        if self.x < 145:
            self.x = 145
            self.direction = 1
        elif self.x > WIDTH - 145:
            self.x = WIDTH - 145
            self.direction = -1

        self.y = 138 + math.sin(pygame.time.get_ticks() / 420) * 20
        self.rect.center = (int(self.x), int(self.y))
        self.fire_timer -= dt
        self.hit_flash = max(0, self.hit_flash - dt)

        if self.fire_timer <= 0:
            fireballs.append(
                Fireball(
                    self.x,
                    self.y + 46,
                    target_x,
                    self.stage,
                )
            )
            self.fire_timer = max(420, 980 - self.stage * 48)

    def damage(self):
        self.health -= 1
        self.hit_flash = 100

    def draw(self, surface):
        body_color = WHITE if self.hit_flash > 0 else self.accent
        dark_scale = tuple(max(0, component - 70) for component in self.accent)

        # Wings.
        pygame.draw.polygon(
            surface,
            dark_scale,
            [
                (int(self.x - 54), int(self.y - 8)),
                (int(self.x - 128), int(self.y - 55)),
                (int(self.x - 102), int(self.y + 22)),
                (int(self.x - 55), int(self.y + 30)),
            ],
        )
        pygame.draw.polygon(
            surface,
            dark_scale,
            [
                (int(self.x + 54), int(self.y - 8)),
                (int(self.x + 128), int(self.y - 55)),
                (int(self.x + 102), int(self.y + 22)),
                (int(self.x + 55), int(self.y + 30)),
            ],
        )

        # Body and head.
        pygame.draw.ellipse(
            surface,
            body_color,
            (int(self.x - 62), int(self.y - 34), 124, 76),
        )
        pygame.draw.ellipse(
            surface,
            body_color,
            (int(self.x - 42), int(self.y - 62), 84, 62),
        )

        # Horns.
        pygame.draw.polygon(
            surface,
            YELLOW,
            [
                (int(self.x - 28), int(self.y - 54)),
                (int(self.x - 47), int(self.y - 92)),
                (int(self.x - 10), int(self.y - 61)),
            ],
        )
        pygame.draw.polygon(
            surface,
            YELLOW,
            [
                (int(self.x + 28), int(self.y - 54)),
                (int(self.x + 47), int(self.y - 92)),
                (int(self.x + 10), int(self.y - 61)),
            ],
        )

        # Eyes, nostrils and tail.
        pygame.draw.circle(surface, (255, 235, 104), (int(self.x - 18), int(self.y - 35)), 7)
        pygame.draw.circle(surface, (255, 235, 104), (int(self.x + 18), int(self.y - 35)), 7)
        pygame.draw.circle(surface, BLACK, (int(self.x - 18), int(self.y - 35)), 3)
        pygame.draw.circle(surface, BLACK, (int(self.x + 18), int(self.y - 35)), 3)
        pygame.draw.circle(surface, DARK, (int(self.x - 10), int(self.y - 12)), 3)
        pygame.draw.circle(surface, DARK, (int(self.x + 10), int(self.y - 12)), 3)

        pygame.draw.arc(
            surface,
            dark_scale,
            (int(self.x + 38), int(self.y + 5), 110, 67),
            0,
            math.pi * 1.35,
            12,
        )

class Sparkle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.life = 28
        angle = random.uniform(0, math.tau)
        speed = random.uniform(1.5, 4.0)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.08
        self.life -= 1

    def draw(self, surface):
        radius = max(1, self.life // 8)
        pygame.draw.circle(
            surface, self.color, (int(self.x), int(self.y)), radius
        )


def blit_scaled(canvas, display):
    display.fill(BLACK)
    display_w, display_h = display.get_size()
    scale = min(display_w / WIDTH, display_h / HEIGHT)
    scaled_w = max(1, int(WIDTH * scale))
    scaled_h = max(1, int(HEIGHT * scale))
    scaled = pygame.transform.smoothscale(canvas, (scaled_w, scaled_h))
    display.blit(
        scaled,
        ((display_w - scaled_w) // 2, (display_h - scaled_h) // 2),
    )
    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption("Waifu Heart Rush: Dragon Hearts v6.1")

    fullscreen = True
    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    canvas = pygame.Surface((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font_packs = build_font_packs()

    heroine = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 180, 120, 150)
    speed = 7

    items = []
    sparkles = []
    heart_bolts = []
    fireballs = []
    boss = None
    pending_level = None
    shoot_cooldown = 0
    player_invulnerability = 0
    score = 0
    lives = 3
    level = 1
    hearts_in_level = 0
    hearts_needed = 6
    spawn_timer = 0
    dialogue = "Catch my feelings. Avoid my terrible decisions."
    level_banner = ""
    level_banner_timer = 0
    reality_banner_timer = 0
    last_reality_key = reality_for_level(level)["key"]
    state = "start"
    blink_timer = 0

    def reset_game():
        nonlocal items, sparkles, heart_bolts, fireballs, boss
        nonlocal pending_level, shoot_cooldown, player_invulnerability
        nonlocal score, lives, level, hearts_in_level
        nonlocal hearts_needed, spawn_timer, dialogue, level_banner
        nonlocal level_banner_timer, reality_banner_timer, heroine
        nonlocal last_reality_key

        items = []
        sparkles = []
        heart_bolts = []
        fireballs = []
        boss = None
        pending_level = None
        shoot_cooldown = 0
        player_invulnerability = 0
        score = 0
        lives = 3
        level = 1
        hearts_in_level = 0
        hearts_needed = 6
        spawn_timer = 0
        dialogue = "Catch my feelings. Avoid my terrible decisions."
        level_banner = ""
        level_banner_timer = 0
        reality_banner_timer = 0
        last_reality_key = reality_for_level(level)["key"]
        heroine = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 180, 120, 150)

    running = True
    while running:
        dt = clock.tick(FPS)
        ticks = pygame.time.get_ticks()
        blink_timer = (blink_timer + dt) % 2600
        blinking = blink_timer > 2460

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        display = pygame.display.set_mode((WIDTH, HEIGHT))

                elif event.key == pygame.K_b and state == "playing":
                    # Summon a practice guardian without waiting for a reality shift.
                    items.clear()
                    heart_bolts.clear()
                    fireballs.clear()
                    pending_level = level
                    boss = DragonBoss(max(1, level // 3), reality["accent"])
                    dialogue = "Practice dragon summoned. SPACE casts heartfire."
                    state = "boss"

                elif event.key == pygame.K_n and state == "playing":
                    current_key = reality_for_level(level)["key"]
                    next_reality = None
                    for candidate in REALITIES:
                        if candidate["min_level"] > level:
                            next_reality = candidate
                            break

                    if next_reality is not None:
                        level = next_reality["min_level"]
                        hearts_in_level = 0
                        hearts_needed = min(9, 6 + max(0, (level - 1) // 3))
                        items.clear()
                        level_banner = f"REALITY SKIP // LEVEL {level}"
                        level_banner_timer = 850
                        reality_banner_timer = 1750
                        dialogue = f"Fast travel: {next_reality['name'].lower()}."
                        last_reality_key = next_reality["key"]
                    else:
                        dialogue = "You already reached the final reality."

                elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if state in ("start", "gameover"):
                        reset_game()
                        state = "playing"

        keys = pygame.key.get_pressed()
        reality = reality_for_level(level)
        fonts = font_packs[reality["font_pack"]]

        if state == "playing":
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                heroine.x -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                heroine.x += speed
            heroine.x = clamp(heroine.x, 12, WIDTH - heroine.width - 12)

            spawn_timer -= dt
            if spawn_timer <= 0:
                # Chill mode: hearts stay common and speed increases only gently.
                heart_chance = max(0.68, 0.82 - (level - 1) * 0.009)
                kind = "heart" if random.random() < heart_chance else "flag"
                items.append(FallingItem(kind, level))

                difficulty_step = min(level - 1, 12)
                min_delay = max(270, 405 - difficulty_step * 9)
                max_delay = max(475, 690 - difficulty_step * 13)
                spawn_timer = random.randint(min_delay, max_delay)

            for item in items[:]:
                item.update()

                if item.rect.colliderect(heroine.inflate(-28, -12)):
                    if item.kind == "heart":
                        score += 1
                        hearts_in_level += 1
                        scene_lines = SCENE_DIALOGUE[reality["key"]]
                        dialogue = scene_lines[(score + level) % len(scene_lines)]

                        for _ in range(14):
                            sparkles.append(
                                Sparkle(
                                    item.rect.centerx,
                                    item.rect.centery,
                                    random.choice(
                                        [reality["accent"], YELLOW, WHITE]
                                    ),
                                )
                            )

                        if hearts_in_level >= hearts_needed:
                            old_reality = reality
                            proposed_level = level + 1
                            new_reality = reality_for_level(proposed_level)
                            hearts_in_level = 0

                            if new_reality["key"] != old_reality["key"]:
                                # Every new reality is protected by a dragon boss.
                                pending_level = proposed_level
                                items.clear()
                                heart_bolts.clear()
                                fireballs.clear()
                                boss = DragonBoss(
                                    max(1, proposed_level // 3),
                                    new_reality["accent"],
                                )
                                dialogue = "A reality dragon blocks the portal. SPACE casts heartfire."
                                state = "boss"
                            else:
                                level = proposed_level
                                hearts_needed = min(
                                    9,
                                    hearts_needed + (1 if level % 3 == 0 else 0),
                                )
                                level_title = LEVEL_TITLES[
                                    min(level - 1, len(LEVEL_TITLES) - 1)
                                ]
                                level_banner = f"LEVEL {level} // {level_title}"
                                level_banner_timer = 850
                                dialogue = random.choice(
                                    [
                                        "Route advanced. Try not to ruin this.",
                                        "New level unlocked. The plot thickens.",
                                        "Affection overflow detected.",
                                        "We are now emotionally complicated.",
                                    ]
                                )
                    else:
                        lives -= 1
                        dialogue = random.choice(
                            [
                                "Red flag detected. Absolutely not.",
                                "We can fix him? No. Dodge.",
                                "That was emotionally expensive.",
                                "Bad vibe intercepted.",
                            ]
                        )
                        for _ in range(12):
                            sparkles.append(
                                Sparkle(
                                    item.rect.centerx,
                                    item.rect.centery,
                                    RED,
                                )
                            )

                    # A reality transition may have already cleared the full
                    # items list before this collision finishes processing.
                    if item in items:
                        items.remove(item)

                    # Stop processing the old snapshot immediately once a
                    # dragon battle begins.
                    if state == "boss":
                        break
                    continue

                if item.rect.top > HEIGHT:
                    if item.kind == "heart":
                        dialogue = "You missed a heart. Rude, but recoverable."
                    if item in items:
                        items.remove(item)

            for sparkle in sparkles[:]:
                sparkle.update()
                if sparkle.life <= 0:
                    sparkles.remove(sparkle)

            if level_banner_timer > 0:
                level_banner_timer = max(0, level_banner_timer - dt)
            if reality_banner_timer > 0:
                reality_banner_timer = max(0, reality_banner_timer - dt)

            if lives <= 0:
                state = "gameover"

        elif state == "boss":
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                heroine.x -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                heroine.x += speed
            heroine.x = clamp(heroine.x, 12, WIDTH - heroine.width - 12)

            shoot_cooldown = max(0, shoot_cooldown - dt)
            player_invulnerability = max(0, player_invulnerability - dt)

            if (keys[pygame.K_SPACE] or keys[pygame.K_z]) and shoot_cooldown <= 0:
                heart_bolts.append(
                    HeartBolt(heroine.centerx, heroine.top + 8)
                )
                shoot_cooldown = 210

            if boss is not None:
                boss.update(dt, heroine.centerx, fireballs)

            for bolt in heart_bolts[:]:
                bolt.update()
                if bolt.rect.bottom < 0:
                    heart_bolts.remove(bolt)
                    continue

                if boss is not None and bolt.rect.colliderect(boss.rect):
                    boss.damage()
                    for _ in range(8):
                        sparkles.append(
                            Sparkle(
                                bolt.rect.centerx,
                                bolt.rect.centery,
                                random.choice([boss.accent, YELLOW, WHITE]),
                            )
                        )
                    heart_bolts.remove(bolt)

            for fireball in fireballs[:]:
                fireball.update()
                if fireball.rect.top > HEIGHT:
                    fireballs.remove(fireball)
                    continue

                if (
                    player_invulnerability <= 0
                    and fireball.rect.colliderect(heroine.inflate(-30, -10))
                ):
                    lives -= 1
                    player_invulnerability = 1000
                    dialogue = "Dragonfire hurts. Very inconvenient."
                    fireballs.remove(fireball)

            for sparkle in sparkles[:]:
                sparkle.update()
                if sparkle.life <= 0:
                    sparkles.remove(sparkle)

            if boss is not None and boss.health <= 0:
                practice_fight = pending_level == level

                if practice_fight:
                    score += 3
                    lives = min(5, lives + 1)
                    dialogue = "Practice dragon defeated. Free therapy heart awarded."
                    boss = None
                    pending_level = None
                    heart_bolts.clear()
                    fireballs.clear()
                    state = "playing"
                else:
                    old_reality = reality
                    level = pending_level
                    pending_level = None
                    score += 5
                    lives = min(5, lives + 1)
                    hearts_needed = min(
                        9,
                        6 + max(0, (level - 1) // 3),
                    )
                    boss = None
                    heart_bolts.clear()
                    fireballs.clear()

                    new_reality = reality_for_level(level)
                    last_reality_key = new_reality["key"]
                    level_title = LEVEL_TITLES[
                        min(level - 1, len(LEVEL_TITLES) - 1)
                    ]
                    level_banner = f"DRAGON DOWN // LEVEL {level} // {level_title}"
                    level_banner_timer = 950
                    reality_banner_timer = 1750
                    dialogue = f"Portal unlocked: {new_reality['name'].lower()}."
                    state = "playing"

            if lives <= 0:
                state = "gameover"

        # Re-evaluate after a possible level-up.
        reality = reality_for_level(level)
        fonts = font_packs[reality["font_pack"]]

        draw_reality(canvas, reality, ticks)

        if state == "start":
            start_reality = REALITIES[0]
            start_fonts = font_packs[start_reality["font_pack"]]
            draw_text(
                canvas,
                "WAIFU HEART RUSH",
                start_fonts["title"],
                HOT_PINK,
                (WIDTH // 2, 145),
                center=True,
            )
            draw_text(
                canvas,
                "ALTERNATE REALITIES EDITION",
                start_fonts["large"],
                PURPLE,
                (WIDTH // 2, 202),
                center=True,
            )
            draw_text(
                canvas,
                "Catch hearts. Dodge red flags. Change realities.",
                start_fonts["body"],
                DARK,
                (WIDTH // 2, 250),
                center=True,
            )
            draw_waifu(canvas, heroine, start_reality, blinking)
            draw_text(
                canvas,
                "SPACE / ENTER  START",
                start_fonts["large"],
                PURPLE,
                (WIDTH // 2, 517),
                center=True,
            )
            draw_text(
                canvas,
                "A/D MOVE   B DRAGON PRACTICE   N NEXT REALITY   F11 WINDOW   ESC QUIT",
                start_fonts["small"],
                DARK,
                (WIDTH // 2, 557),
                center=True,
            )

        elif state == "playing":
            for item in items:
                item.draw(canvas, reality)
            for sparkle in sparkles:
                sparkle.draw(canvas)

            draw_waifu(canvas, heroine, reality, blinking)

            panel_text = reality["text"]
            panel_fill = reality["panel"]
            accent = reality["accent"]

            # HUD panel.
            hud_surface = pygame.Surface((294, 92), pygame.SRCALPHA)
            pygame.draw.rect(
                hud_surface,
                (*panel_fill, 232),
                hud_surface.get_rect(),
                border_radius=12,
            )
            pygame.draw.rect(
                hud_surface,
                accent,
                hud_surface.get_rect(),
                3,
                border_radius=12,
            )
            canvas.blit(hud_surface, (18, 16))

            draw_text(
                canvas,
                f"LVL {level:02d}  HEARTS {score:03d}",
                fonts["body"],
                panel_text,
                (35, 29),
            )
            draw_text(canvas, "LIVES", fonts["small"], panel_text, (36, 69))
            for life_index in range(lives):
                draw_heart(
                    canvas,
                    124 + life_index * 31,
                    82,
                    22,
                    RED,
                )

            # Reality title and BPM/status strip.
            draw_text(
                canvas,
                reality["name"],
                fonts["large"],
                accent,
                (WIDTH // 2, 27),
                center=True,
            )
            draw_text(
                canvas,
                reality["subtitle"],
                fonts["small"],
                panel_text,
                (WIDTH // 2, 61),
                center=True,
            )

            # Affection meter.
            meter_x, meter_y, meter_w, meter_h = 610, 29, 264, 28
            pygame.draw.rect(
                canvas,
                panel_fill,
                (meter_x, meter_y, meter_w, meter_h),
                border_radius=10,
            )
            progress = hearts_in_level / hearts_needed
            fill_w = int(meter_w * progress)
            if fill_w > 0:
                pygame.draw.rect(
                    canvas,
                    accent,
                    (meter_x, meter_y, fill_w, meter_h),
                    border_radius=10,
                )
            pygame.draw.rect(
                canvas,
                panel_text,
                (meter_x, meter_y, meter_w, meter_h),
                2,
                border_radius=10,
            )
            draw_text(
                canvas,
                f"AFFECTION {hearts_in_level:02d}/{hearts_needed:02d}",
                fonts["small"],
                panel_text,
                (meter_x, meter_y - 21),
            )

            # Dialogue box stays high enough to avoid the character.
            dialogue_rect = pygame.Rect(143, 119, 614, 58)
            dialogue_surface = pygame.Surface(
                (dialogue_rect.width, dialogue_rect.height),
                pygame.SRCALPHA,
            )
            pygame.draw.rect(
                dialogue_surface,
                (*panel_fill, 226),
                dialogue_surface.get_rect(),
                border_radius=13,
            )
            pygame.draw.rect(
                dialogue_surface,
                accent,
                dialogue_surface.get_rect(),
                3,
                border_radius=13,
            )
            canvas.blit(dialogue_surface, dialogue_rect)
            draw_text(
                canvas,
                dialogue,
                fonts["small"],
                panel_text,
                dialogue_rect.center,
                center=True,
            )

            if level_banner_timer > 0:
                banner_rect = pygame.Rect(171, 218, 558, 75)
                pygame.draw.rect(canvas, panel_fill, banner_rect, border_radius=7)
                pygame.draw.rect(canvas, accent, banner_rect, 4, border_radius=7)
                draw_text(
                    canvas,
                    level_banner,
                    fonts["body"],
                    accent,
                    banner_rect.center,
                    center=True,
                )

            if reality_banner_timer > 0:
                shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                shade.fill((0, 0, 0, 175))
                canvas.blit(shade, (0, 0))

                reality_rect = pygame.Rect(92, 195, 716, 180)
                pygame.draw.rect(
                    canvas,
                    panel_fill,
                    reality_rect,
                    border_radius=10,
                )
                pygame.draw.rect(
                    canvas,
                    accent,
                    reality_rect,
                    5,
                    border_radius=10,
                )
                draw_text(
                    canvas,
                    "REALITY SHIFT",
                    fonts["small"],
                    accent,
                    (WIDTH // 2, 226),
                    center=True,
                )
                draw_text(
                    canvas,
                    reality["name"],
                    fonts["title"],
                    panel_text,
                    (WIDTH // 2, 281),
                    center=True,
                )
                draw_text(
                    canvas,
                    reality["subtitle"],
                    fonts["small"],
                    panel_text,
                    (WIDTH // 2, 336),
                    center=True,
                )

            if reality["key"] in ("club", "metro", "rooftop", "dragon"):
                draw_scanlines(canvas, 18)

        elif state == "boss":
            # Fight in the current reality, with the portal color previewing
            # the world waiting behind the guardian.
            panel_text = reality["text"]
            panel_fill = reality["panel"]
            accent = boss.accent if boss is not None else reality["accent"]

            shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            shade.fill((0, 0, 0, 72))
            canvas.blit(shade, (0, 0))

            # Portal behind the dragon.
            portal_radius = 102 + int(math.sin(ticks / 160) * 7)
            pygame.draw.circle(
                canvas,
                accent,
                (WIDTH // 2, 145),
                portal_radius,
                8,
            )
            pygame.draw.circle(
                canvas,
                WHITE,
                (WIDTH // 2, 145),
                portal_radius - 18,
                2,
            )

            for bolt in heart_bolts:
                bolt.draw(canvas, accent)
            for fireball in fireballs:
                fireball.draw(canvas)
            for sparkle in sparkles:
                sparkle.draw(canvas)

            if boss is not None:
                boss.draw(canvas)

            # Blink heroine while temporarily invulnerable.
            if player_invulnerability <= 0 or (ticks // 90) % 2 == 0:
                draw_waifu(canvas, heroine, reality, blinking)

            draw_text(
                canvas,
                "REALITY GUARDIAN",
                fonts["large"],
                accent,
                (WIDTH // 2, 25),
                center=True,
            )
            draw_text(
                canvas,
                "MOVE: A/D OR ARROWS      CAST HEARTFIRE: SPACE OR Z",
                fonts["small"],
                panel_text,
                (WIDTH // 2, 57),
                center=True,
            )

            # Dragon health bar.
            if boss is not None:
                bar_x, bar_y, bar_w, bar_h = 214, 82, 472, 26
                pygame.draw.rect(
                    canvas,
                    panel_fill,
                    (bar_x, bar_y, bar_w, bar_h),
                    border_radius=9,
                )
                health_ratio = max(0, boss.health / boss.max_health)
                pygame.draw.rect(
                    canvas,
                    accent,
                    (bar_x, bar_y, int(bar_w * health_ratio), bar_h),
                    border_radius=9,
                )
                pygame.draw.rect(
                    canvas,
                    panel_text,
                    (bar_x, bar_y, bar_w, bar_h),
                    2,
                    border_radius=9,
                )
                draw_text(
                    canvas,
                    f"DRAGON HP {boss.health:02d}/{boss.max_health:02d}",
                    fonts["small"],
                    panel_text,
                    (WIDTH // 2, 95),
                    center=True,
                )

            # Lives and message.
            lives_rect = pygame.Rect(23, 22, 168, 70)
            pygame.draw.rect(canvas, panel_fill, lives_rect, border_radius=10)
            pygame.draw.rect(canvas, accent, lives_rect, 3, border_radius=10)
            draw_text(canvas, "LIVES", fonts["small"], panel_text, (37, 34))
            for life_index in range(lives):
                draw_heart(
                    canvas,
                    45 + life_index * 27,
                    72,
                    19,
                    RED,
                )

            dialogue_rect = pygame.Rect(150, 488, 600, 59)
            pygame.draw.rect(
                canvas,
                panel_fill,
                dialogue_rect,
                border_radius=12,
            )
            pygame.draw.rect(
                canvas,
                accent,
                dialogue_rect,
                3,
                border_radius=12,
            )
            draw_text(
                canvas,
                dialogue,
                fonts["small"],
                panel_text,
                dialogue_rect.center,
                center=True,
            )

        elif state == "gameover":
            draw_waifu(canvas, heroine, reality, blinking)
            draw_text(
                canvas,
                "EMOTIONAL DAMAGE",
                fonts["title"],
                RED,
                (WIDTH // 2, 151),
                center=True,
            )
            draw_text(
                canvas,
                f"LEVEL {level:02d} // HEARTS {score:03d}",
                fonts["large"],
                reality["text"],
                (WIDTH // 2, 221),
                center=True,
            )

            if score >= 80:
                rank = "Secret ending material"
            elif score >= 45:
                rank = "Main-character chemistry"
            elif score >= 22:
                rank = "Promising alternate timeline"
            else:
                rank = "Needs another season"

            draw_text(
                canvas,
                rank,
                fonts["body"],
                reality["accent"],
                (WIDTH // 2, 275),
                center=True,
            )
            draw_text(
                canvas,
                f"Reality reached: {reality['name']}",
                fonts["small"],
                reality["text"],
                (WIDTH // 2, 316),
                center=True,
            )
            draw_text(
                canvas,
                "SPACE / ENTER  TRY ANOTHER TIMELINE",
                fonts["body"],
                reality["text"],
                (WIDTH // 2, 520),
                center=True,
            )
            draw_text(
                canvas,
                "N  NEXT REALITY       F11  WINDOW MODE       ESC  QUIT",
                fonts["small"],
                reality["text"],
                (WIDTH // 2, 559),
                center=True,
            )

        blit_scaled(canvas, display)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
