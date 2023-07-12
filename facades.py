from main import Facade, Cassette
from datetime import date

facade_c = Facade({
    1: [Cassette(1170, 585), Cassette(1920, 590), Cassette(1920, 600), Cassette(1920, 610), Cassette(1205, 645),
        Cassette(1920, 660), Cassette(1920, 670), Cassette(1920, 680), Cassette(1920, 690), Cassette(845, 685),
        Cassette(880, 1090)],
    2: [Cassette(1170, 1130), Cassette(1920, 1130), Cassette(1920, 1130), Cassette(1205, 1090), Cassette(1920, 1090),
        Cassette(1920, 1090), Cassette(1920, 1090), Cassette(1920, 1090), Cassette(845, 1090), Cassette(880, 1090)],
    3: [Cassette(1920, 1005), Cassette(1920, 1005), Cassette(1920, 375), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1300, 1045)],
    4: [Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045), Cassette(1920, 1045),
        Cassette(1920, 1045), Cassette(1920, 1045)],
    5: [Cassette(1920, 1090), Cassette(725, 1090), Cassette(831, 1090, 9003), Cassette(831, 1090, 9003),
        Cassette(831, 1090, 9003), Cassette(831, 1090, 9003)],
    6: [Cassette(1920, 1090), Cassette(725, 1090), Cassette(831, 1090, 9003), Cassette(831, 1090, 9003),
        Cassette(831, 1090, 9003), Cassette(831, 1090, 9003)],
    7: [*Cassette(1920, 1125) * 17, Cassette(1300, 1125)],
    8: [*Cassette(1920, 1155)*17, Cassette(1300, 1155)]
})

the_date = date(2023, 7, 6)
facade_c.put_into_production(the_date, 5, 1, 2, 3, 4)
facade_c.put_into_production(the_date, 7, "1-3")


