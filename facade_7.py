from main import Cassette, Facade

facade_7 = Facade({
    1: [Cassette(745, 385), Cassette(1270, 385), *Cassette(1420, 385)*2, Cassette(1374, 385)],
    2: [Cassette(745, 620), Cassette(1270, 620), *Cassette(1420, 620)*2, Cassette(1374, 620)],
    3: [Cassette(155, 620), Cassette(745, 620), Cassette(1270, 620), *Cassette(1420, 620)*2, Cassette(1374, 620)],
    4: [Cassette(323, 620), Cassette(745, 620), Cassette(1270, 620), *Cassette(1420, 620)*2, Cassette(1374, 620)],
    5: [Cassette(495, 620), Cassette(745, 620), Cassette(1270, 620), *Cassette(1420, 620)*2, Cassette(1374, 620)],
    6: [Cassette(666, 620), Cassette(745, 620), Cassette(1270, 620), *Cassette(1420, 620)*2, Cassette(1374, 620)],
    7: [Cassette(838, 620), *Cassette(1420, 620)*17, Cassette(1374, 620)],
    8: [Cassette(1019, 655), *Cassette(1420, 655)*17, Cassette(1374, 620)],
    9: [Cassette(1200, 655), *Cassette(1420, 655)*14, *Cassette(1420, 350)*3, Cassette(1374, 350)],
    10: [*Cassette(1420, 655)*15],
    11: [Cassette(180, 655), *Cassette(1420, 655)*15],
    12: [Cassette(287, 595), Cassette(1420, 595), Cassette(745, 595)],
    13: [Cassette(467, 655), Cassette(1420, 655), Cassette(745, 655)],
    14: [Cassette(648, 655), Cassette(1420, 655), Cassette(745, 655)],
    15: [Cassette(801, 550), *Cassette(1420, 550)*15],
    16: [Cassette(954, 550), *Cassette(1420, 550)*15],
    17: [Cassette(1137, 690), *Cassette(1420, 690)*14, Cassette(720, 690)],
    18: [*Cassette(1420, 720)*15, Cassette(720, 720)]
})

