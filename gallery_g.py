from main import Facade, Cassette
from datetime import date

gallery_g = Facade({
    1: [*Cassette(1200, 1000, 9003)*17],
    2: [*Cassette(1200, 640, 9003)*17],
    3: [*Cassette(1200, 640, 9003)*17],
})

the_date = date(2023, 7, 6)
gallery_g.put_into_production(the_date, 1, 1, 2, 3, 4)
gallery_g.put_into_production(the_date, 2, "1-3")



