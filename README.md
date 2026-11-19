# news-image-20261118-2

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Rifat7600/news-image-20261118-2/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Rifat7600/news-image-20261118-2/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**The World — 18 November 2026**: one image summing up Wednesday 18 November 2026's world news as a map. A large drawn world map carries eight numbered red pins marking where the day's top stories happened — the Trump–Xi–Putin trilateral in Shenzhen, the escalating Iran war around Kuwait and the Strait of Hormuz, Israel's Gaza operation, the Quad leaders' meeting in Manila, Cyclone Akvan in the Bay of Bengal, Mary Peltola's Senate win in Alaska, the magnitude 6 quake in Papua New Guinea, and the Russian military plane crash in Siberia — with a numbered legend below giving one short line per story.

## Run it

```sh
python3 generate.py   # draws entry.png (1024x1024) with Pillow
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is standard library only: it copies `entry.png` beside it to `$MAKEFUN_OUTPUT_DIR/entry.png`, so repeated runs write identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rifat100&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
