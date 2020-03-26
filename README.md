---
permalink: /
---
# cdcl: `cron` & dashboard in cloud land

<!-- cron status -->
[![daily-gh](https://img.shields.io/github/workflow/status/casperdcl/cdcl/daily?label=daily&logo=GitHub)](https://github.com/casperdcl/cdcl/actions?query=workflow%3Adaily)

## Dashboard

<!-- pinned-gists -->
<div class="gist">37496a4e4c84aed9711fbe3ec560888a</div>
<div class="gist">060c106a2b42d68d20b2e832971e5e04</div>

<!-- Priority
1. any issues may affect lots of people
2. nobody else is likely to fix issues in a timely manner
-->
[![argopt](https://img.shields.io/travis/casperdcl/argopt?label=argopt)](https://travis-ci.org/casperdcl/argopt)
[![git-fame](https://img.shields.io/travis/casperdcl/git-fame?label=git-fame)](https://travis-ci.org/casperdcl/git-fame)
[![py-make](https://img.shields.io/travis/tqdm/py-make?label=py-make)](https://travis-ci.org/tqdm/py-make)
[![tqdm.cpp](https://img.shields.io/travis/tqdm/tqdm.cpp?label=tqdm.cpp)](https://travis-ci.org/tqdm/tqdm.cpp)
[![tqdm-feedstock](https://img.shields.io/travis/com/conda-forge/tqdm-feedstock?label=tqdm-feedstock)](https://travis-ci.com/conda-forge/tqdm-feedstock)
[![tqdm](https://img.shields.io/travis/tqdm/tqdm/master.svg?label=tqdm)](https://travis-ci.org/tqdm/tqdm)

----

[![BrainWeb](https://img.shields.io/travis/casperdcl/brainweb?label=BrainWeb)](https://travis-ci.org/casperdcl/brainweb)
[![Conjuring](https://img.shields.io/travis/conjuring/conjuring?label=Conjuring)](https://travis-ci.org/conjuring/conjuring)
[![dvc](https://img.shields.io/travis/com/iterative/dvc?label=dvc)](https://travis-ci.com/iterative/dvc)
[![dvc.org](https://img.shields.io/circleci/build/gh/iterative/dvc.org?label=dvc.org)](https://circleci.com/gh/iterative/dvc.org)
[![dvc-test](https://img.shields.io/travis/com/iterative/dvc-test?label=dvc-test)](https://travis-ci.com/iterative/dvc-test)
[![gist:Music](https://img.shields.io/github/workflow/status/casperdcl/music-box/music-box?label=gist:Music)](https://github.com/casperdcl/music-box/actions?query=workflow%3Amusic-box)
[![gist:Strava](https://img.shields.io/circleci/build/gh/casperdcl/strava-box?label=gist:Strava)](https://circleci.com/gh/casperdcl/strava-box)
[![gist:Weather](https://img.shields.io/github/workflow/status/casperdcl/hl-weather-box/hl-weather-box?label=gist:Weather)](https://github.com/casperdcl/hl-weather-box/actions?query=workflow%3Ahl-weather-box)
[![gist:COVID-19](https://img.shields.io/github/workflow/status/casperdcl/covid-19-box/covid-19-box?label=gist:COVID-19)](https://github.com/casperdcl/covid-19-box/actions?query=workflow%3Acovid-19-box)
[![NiftyPET-rtd](https://img.shields.io/readthedocs/niftypet?label=NiftyPET-rtd)](https://readthedocs.org/projects/niftypet/builds)
[![OpenWorm-docs](https://img.shields.io/circleci/build/gh/openworm/openworm_docs?label=OpenWorm-docs)](https://circleci.com/gh/openworm/openworm_docs)
[![SIRF](https://img.shields.io/travis/CCPPETMR/SIRF?label=SIRF)](https://travis-ci.org/CCPPETMR/SIRF)
[![SIRF-SuperBuild](https://img.shields.io/travis/CCPPETMR/SIRF-SuperBuild?label=SIRF-SuperBuild)](https://travis-ci.org/CCPPETMR/SIRF-SuperBuild)

## Cron

Run tasks at scheduled times in the cloud.

### Backends/providers

- Travis CI
  - con: [can be at most daily](https://docs.travis-ci.com/user/cron-jobs)
  - con: [caches are accessible by PRs](https://docs.travis-ci.com/user/caching/)
- Circle CI
  + pro: can cache between cron runs
- GitHub Actions
  + pro: everything in one place (no reliance on third-party providers)
  + con: [can only cache on push and PR](https://help.github.com/en/actions/configuring-and-managing-workflows/caching-dependencies-to-speed-up-workflows#restrictions-for-accessing-a-cache)

### User Configuration

- In-place: the root config files (`.travis.yml`/`.circleci`/`.github/workflows/` etc.)
- TODO: or file layout: `(travis|circle|gh)_(day|week|month)_*.y(a)ml`?
