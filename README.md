# cdcl: `cron` & dashboard in cloud land

## Dashboard

<!-- Priority
1. any issues may affect lots of people
2. nobody else is likely to fix issues in a timely manner
-->
[![argopt](https://img.shields.io/travis/casperdcl/argopt?label=argopt)](https://travis-ci.org/casperdcl/argopt)
[![git-fame](https://img.shields.io/travis/casperdcl/git-fame?label=git-fame)](https://travis-ci.org/casperdcl/git-fame)
[![py-make](https://img.shields.io/travis/tqdm/py-make?label=py-make)](https://travis-ci.org/tqdm/py-make)
[![tqdm.cpp](https://img.shields.io/travis/tqdm/tqdm.cpp?label=tqdm.cpp)](https://travis-ci.org/tqdm/tqdm.cpp)
[![tqdm-feedstock](https://img.shields.io/travis/com/conda-forge/tqdm-feedstock?label=tqdm-feedstock)](https://travis-ci.com/conda-forge/tqdm-feedstock)
[![tqdm](https://img.shields.io/travis/tqdm/tqdm?label=tqdm)](https://travis-ci.org/tqdm/tqdm)

----

[![BrainWeb](https://img.shields.io/travis/casperdcl/brainweb?label=BrainWeb)](https://travis-ci.org/casperdcl/brainweb)
[![Conjuring](https://img.shields.io/travis/conjuring/conjuring?label=Conjuring)](https://travis-ci.org/conjuring/conjuring)
[![dvc](https://img.shields.io/travis/com/iterative/dvc?label=dvc)](https://travis-ci.com/iterative/dvc)
[![dvc.org](https://img.shields.io/circleci/build/gh/iterative/dvc.org?label=dvc.org)](https://circleci.com/gh/iterative/dvc.org)
[![dvc-test](https://img.shields.io/travis/com/iterative/dvc-test?label=dvc-test)](https://travis-ci.com/iterative/dvc-test)
[![gist:Music](https://img.shields.io/circleci/build/gh/casperdcl/music-box?label=gist:Music)](https://circleci.com/gh/casperdcl/music-box)
[![gist:Strava](https://img.shields.io/circleci/build/gh/casperdcl/strava-box?label=gist:Strava)](https://circleci.com/gh/casperdcl/strava-box)
[![NiftyPET-rtd](https://img.shields.io/readthedocs/niftypet?label=NiftyPET-rtd)](https://readthedocs.org/projects/niftypet/builds)
[![OpenWorm-docs](https://img.shields.io/circleci/build/gh/openworm/openworm_docs?label=OpenWorm-docs)](https://circleci.com/gh/openworm/openworm_docs)
[![SIRF](https://img.shields.io/travis/CCPPETMR/SIRF?label=SIRF)](https://travis-ci.org/CCPPETMR/SIRF)
[![SIRF-SuperBuild](https://img.shields.io/travis/CCPPETMR/SIRF-SuperBuild?label=SIRF-SuperBuild)](https://travis-ci.org/CCPPETMR/SIRF-SuperBuild)

## Cron

Run tasks at scheduled times in the cloud.

## Backends/providers

- Travis CI
  - con: can be at most daily
- Circle CI
- GitHub Actions
  + pro: everything in one place (no reliance on third-party providers)

## User Configuration

- In-place the root config files (`.travis.yml`/`.circleci`/`.github/workflows/` etc.)
- TODO: or file layout: `(travis|circle|gh)_(day|week|month)_*.y(a)ml`?
