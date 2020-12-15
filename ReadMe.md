MatAndVecSer.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-libs/MatAndVecSer.py/-/jobs/artifacts/master/raw/dist/MatAndVecSer-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/MatAndVecSer.py/workflows/CI/master/MatAndVecSer-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/KOLANICH-libs/MatAndVecSer.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH-libs/MatAndVecSer.py/badges/master/coverage.svg)~~
[![GitHub Actions](https://github.com/KOLANICH-libs/MatAndVecSer.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/MatAndVecSer.py/actions/)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/MatAndVecSer.py.svg)](https://libraries.io/github/KOLANICH-libs/MatAndVecSer.py)

Often one needs to store a matrix and a vector, usually making no sense without each other.

Examples:
* 1-st order Markov chain initial distribution and transition matrix.
* PCA / ICA basis vectors and means.

These all have to be manipulated as a single object.

This is a small lib to which the code manipulating them has been extracted from my several projects.
