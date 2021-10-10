[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![first-timers-only Friendly](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)
![example workflow](https://github.com/claytonjhamilton/stackoverflow-badge/actions/workflows/python-tests-action.yml/badge.svg)
[![Tests Status](./reports/report_badges/tests-badge.svg?dummy=8484744)](./reports/junit/report.html)
[![Coverage Status](./reports/report_badges/coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html)
[![Flake8 Status](./reports/report_badges/flake8-badge.svg?dummy=8484744)](./reports/flake8/index.html)

<h1 align = "center">Display your stats with this unique StackOverflow Badge</h1>
<p align="center">
<a
href="https://stackoverflow.com/users/14122375/hamiltonpharmd" target="_blank"><img alt="StackOverflow user information"
src="https://stackoverflow-badge.herokuapp.com/api/StackOverflowBadge/14122375" ></a>
</p>
<h2>Why</h2>
<text>This repository is my experiment with setting up an API from scratch and serving data to end users. Along the way I was able to learn how to use GitHub Actions, write simple Python tests, and improve my understanding of FastAPI.</text>
<h2>How to use</h2>
<text>Update the following to include your StackOverflow UserID and embed in your GitHub profile's README or other markdown document:</text>

```
[![HamiltonPharmD StackOverflow](https://stackoverflow-badge.herokuapp.com/api/StackOverflowBadge/14122375)](https://stackoverflow.com/users/14122375/hamiltonpharmd)
```
`python -m pytest --junitxml=reports/junit/junit.xml`

`genbadge coverage --output-file ./reports/report_badges/coverage-badge.svg`

