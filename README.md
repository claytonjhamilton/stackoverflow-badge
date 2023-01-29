[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![first-timers-only Friendly](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)
![example workflow](https://github.com/claytonjhamilton/stackoverflow-badge/actions/workflows/python-tests-action.yml/badge.svg)
[![Flake8 Status](./reports/report_badges/flake8-badge.svg?dummy=8484744)](./reports/flake8/index.html)

<h1 align = "center">Display your stats with this unique StackOverflow Badge</h1>
<p align="center">
<a
href="https://stackoverflow.com/users/14122375/hamiltonpharmd" target="_blank"><img alt="StackOverflow user information"
src="https://stackoverflow-badge.onrender.com/api/StackOverflowBadge/14122375" ></a>
</p>
<h2>Why</h2>
<text>This repository is my experiment with setting up an API from scratch and serving data to end users. Along the way I was able to learn how to use GitHub Actions, write simple Python tests, and improve my understanding of FastAPI.</text>
<h2>How to use</h2>
<text>Update the following to include your StackOverflow UserID and embed in your GitHub profile's README or other markdown document:</text>

```
[![HamiltonPharmD StackOverflow](https://stackoverflow-badge.onrender.com/api/StackOverflowBadge/14122375)](https://stackoverflow.com/users/14122375/hamiltonpharmd)
```

<h2>Setting up your local environment to contribute</h2>

1. Find an issue you're interested in resolving
2. Fork and clone this repo
3. Create a virtual environment
4. Run `pip install -r dev-requirements.txt`
5. Complete code edits
6. To start the app run `uvicorn main:api`
7. Open this address in your browser to view the badge: http://127.0.0.1:8000/api/StackOverflowBadge/14122375
8. Run tests using from project root dir `python -m pytest tests/` and ensure all pass
9. Update flake8 badge `genbadge flake8 --output-file ./reports/report_badges/flake8-badge.svg`
10. Submit changes as a PR
