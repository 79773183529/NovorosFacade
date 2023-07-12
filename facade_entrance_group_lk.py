from main import Facade, Cassette

facade_entrance_group_lk = Facade({
    1: [Cassette(460, 445), Cassette(1000, 445), Cassette(400, 445), *Cassette(405, 445)*2, Cassette(400, 445),
        Cassette(1000, 445), Cassette(460, 445)],
    2: [Cassette(640, 635), Cassette(1000, 635), Cassette(400, 635), *Cassette(405, 635)*2, Cassette(400, 635),
        Cassette(1000, 635), Cassette(640, 635)],
    3: [Cassette(815, 635), Cassette(1000, 635), Cassette(400, 635), *Cassette(405, 635)*2, Cassette(400, 635),
        Cassette(1000, 635), Cassette(815, 635)],
    4: [Cassette(990, 635), Cassette(1000, 635), Cassette(400, 635), *Cassette(405, 635)*2, Cassette(400, 635),
        Cassette(1000, 635), Cassette(990, 635)],
    5: [Cassette(1165, 635), Cassette(1000, 635), Cassette(400, 635), *Cassette(405, 635)*2, Cassette(400, 635),
        Cassette(1000, 635), Cassette(1165, 635)],
    6: [Cassette(1340, 635), Cassette(1000, 635), *Cassette(700, 635)*2, Cassette(1420, 635), *Cassette(1165, 635)*2,
        Cassette(1420, 635), *Cassette(700, 635)*2, Cassette(1000, 635), Cassette(1340, 635)],
    7: [Cassette(1420, 300), Cassette(1000, 300), *Cassette(700, 300)*2, Cassette(1420, 300), *Cassette(1165, 300)*2,
        Cassette(1420, 300), *Cassette(700, 300)*2, Cassette(1000, 300), Cassette(1420, 300)]
})






