---
permalink: /
---
# cdcl: `cron` & dashboard in cloud land

<!-- cron status -->
[![daily-gh](https://img.shields.io/github/workflow/status/casperdcl/cdcl/daily?label=daily&logo=GitHub)](https://github.com/casperdcl/cdcl/actions)

## Dashboard

<!-- pinned-gists -->
<div class="gist">37496a4e4c84aed9711fbe3ec560888a</div>
<div class="gist">060c106a2b42d68d20b2e832971e5e04</div>

<!-- Priority
1. any issues may affect lots of people
2. nobody else is likely to fix issues in a timely manner
-->
[![argopt](https://img.shields.io/github/workflow/status/casperdcl/argopt/Test?label=argopt)](https://github.com/casperdcl/argopt/actions/workflows/test.yml)
[![BrainWeb](https://img.shields.io/travis/casperdcl/brainweb?label=BrainWeb)](https://travis-ci.org/casperdcl/brainweb)
[![git-fame](https://img.shields.io/github/workflow/status/casperdcl/git-fame/Test?label=git-fame)](https://github.com/casperdcl/git-fame/actions/workflows/test.yml)
[![py-make](https://img.shields.io/travis/tqdm/py-make?label=py-make)](https://travis-ci.org/tqdm/py-make)
[![shtab](https://img.shields.io/github/workflow/status/iterative/shtab/Test?label=shtab)](https://github.com/iterative/shtab/actions/workflows/test.yml)
[![tqdm.cpp](https://img.shields.io/travis/tqdm/tqdm.cpp?label=tqdm.cpp)](https://travis-ci.org/tqdm/tqdm.cpp)
[![tqdm](https://img.shields.io/github/workflow/status/tqdm/tqdm/Test?label=tqdm)](https://github.com/tqdm/tqdm/actions/workflows/test.yml)

----

[![Conjuring](https://img.shields.io/github/workflow/status/conjuring/conjuring/Test?label=Conjuring)](https://github.com/conjuring/conjuring/actions/workflows/test.yml)
[![dvc](https://img.shields.io/github/workflow/status/iterative/dvc/Tests?label=dvc)](https://github.com/iterative/dvc/actions/workflows/tests.yaml)
[![dvc.org](https://img.shields.io/circleci/build/gh/iterative/dvc.org?label=dvc.org)](https://circleci.com/gh/iterative/dvc.org)
[![dvc-test](https://img.shields.io/travis/com/iterative/dvc-test?label=dvc-test)](https://travis-ci.com/iterative/dvc-test)
[![gist:COVID-19](https://img.shields.io/github/workflow/status/casperdcl/covid-19-box/covid-19-box?label=gist:COVID-19)](https://github.com/casperdcl/covid-19-box/actions/workflows/test.yml)
[![gist:ghstat](https://img.shields.io/github/workflow/status/casperdcl/ghstat/daily?label=gist:ghstat)](https://github.com/casperdcl/ghstat/actions/workflows/test.yml)
[![gist:Music](https://img.shields.io/github/workflow/status/casperdcl/music-box/music-box?label=gist:Music)](https://github.com/casperdcl/music-box/actions/workflows/music-box.yml)
[![gist:Strava](https://img.shields.io/circleci/build/gh/casperdcl/strava-box?label=gist:Strava)](https://circleci.com/gh/casperdcl/strava-box)
[![gist:Weather](https://img.shields.io/github/workflow/status/casperdcl/hl-weather-box/hl-weather-box?label=gist:Weather)](https://github.com/casperdcl/hl-weather-box/actions/workflows/hl-weather.yml)
[![miutil](https://img.shields.io/github/workflow/status/AMYPAD/miutil/Test?label=miutil)](https://github.com/AMYPAD/miutil/actions/workflows/test.yml)
[![NiftyPET-rtd](https://img.shields.io/readthedocs/niftypet?label=NiftyPET-rtd)](https://readthedocs.org/projects/niftypet/builds)
[![OpenWorm-docs](https://img.shields.io/circleci/build/gh/openworm/openworm_docs?label=OpenWorm-docs)](https://circleci.com/gh/openworm/openworm_docs)
[![SIRF](https://img.shields.io/travis/SynerBI/SIRF?label=SIRF)](https://travis-ci.org/SynerBI/SIRF)
[![SIRF-SuperBuild](https://img.shields.io/travis/SynerBI/SIRF-SuperBuild?label=SIRF-SuperBuild)](https://travis-ci.org/SynerBI/SIRF-SuperBuild)
[![SPM12](https://img.shields.io/github/workflow/status/AMYPAD/SPM12/Test?label=SPM12)](https://github.com/AMYPAD/SPM12/actions/workflows/test.yml)

![](https://gist.githubusercontent.com/casperdcl/7f351ce61f01cfcfb5cfa53097954435/raw/ghstats-5.svg)

<details><summary>Full breakdown</summary><img src="https://gist.githubusercontent.com/casperdcl/7f351ce61f01cfcfb5cfa53097954435/raw/ghstats-a.png"/><br/><img src="https://gist.githubusercontent.com/casperdcl/7f351ce61f01cfcfb5cfa53097954435/raw/ghstats-b-full.png"/></details>

----

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
  + con: can only re-run entire workflows (not individual jobs)
  + con: [can only cache on push and PR](https://help.github.com/en/actions/configuring-and-managing-workflows/caching-dependencies-to-speed-up-workflows#restrictions-for-accessing-a-cache)

### User Configuration

- In-place: the root config files (`.travis.yml`/`.circleci`/`.github/workflows/` etc.)
- TODO: or file layout: `(travis|circle|gh)_(day|week|month)_*.y(a)ml`?
