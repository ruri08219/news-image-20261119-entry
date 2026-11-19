[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ruri08219/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ruri08219/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119)

# THE WORLD IN A DAY — 19 November 2026

One image, one day: this repository's program writes a front page
summing up the world news of Thursday 19 November 2026 to
`/output/entry.png`.

This one is built around the day's **rare** news — the stories
every other front page will miss:

- **Lead:** Voyager 1 confirmed a light-day from home — NASA's JPL
  briefing today marks the first human-made object 16.1 billion
  miles out — beside a four-scene illustration of the day (the probe
  in interstellar space, the Osaka quantum lab, Earth's ancient rock
  strata, a brain scan).
- **Three more fronts:** a new quantum state found in Osaka, a brain
  score that sees Alzheimer's 12 years early, and Pew's projection
  that Islam becomes the world's largest faith by 2035.
- **Nine more stories:** Earth's missing billion years may be
  explained, Somalia accuses the UAE of secret bases, an LPG tanker
  sunk off Bulgaria was 'hit by projectiles', Deutsche Bank handled
  $582m in Epstein-linked deals, police clash with protesters as
  Spain strikes, Liu Yunping becomes the first Taiwanese American to
  chair the House Democrats, India and Japan review defence ties,
  Duckett's 133 in the ODI, and French protests swell — plus a ticker
  carrying the big headlines (APEC trilateral, GTA VI, Jeffries,
  Cyclone Akvan, Nvidia, the EU's €45bn Ukraine loan).

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.jpg` to `/output/entry.png` and verifies it by size, SHA-256
and JPEG markers before and after the copy. No network, no clock, no
randomness: two runs write identical bytes.

Built for make.fun competition `news-image-20261119`.
