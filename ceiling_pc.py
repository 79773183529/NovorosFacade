from main import Cassette, Ceiling

ceiling_pc = Ceiling({
    1: [Cassette(2180, 1130), *Cassette(1420, 1130) * 4, Cassette(1341, 1130), Cassette(1145, 1130),
        *Cassette(1420, 1130) * 3, Cassette(1055, 1130), Cassette(685, 1130)]
})


