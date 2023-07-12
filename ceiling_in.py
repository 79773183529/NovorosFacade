from main import Cassette, Ceiling

ceiling_in = Ceiling({
    1: [Cassette(1125, 1080)],
    2: [Cassette(1130, 1380)],
    3: [Cassette(1130, 1555)],
    4: [Cassette(1130, 1555)],
    5: [Cassette(1130, 1880)],
    6: [Cassette(1130, 700)],
    7: [Cassette(1130, 1420)],
    8: [Cassette(1130, 1420)],
    9: [Cassette(1130, 470)],
    10: [*Cassette(1130, 1030)*2],
    11: [*Cassette(1130, 1420)*2],
    12: [*Cassette(1130, 1420)*2],
    13: [*Cassette(1130, 382)*2],
})


