# send-loadtests

[![](https://pbs.twimg.com/profile_images/2596464442/datadoglogo_normal.png)](https://app.datadoghq.com/dash/326406/send?live=true&page=0&is_auto=false&from_ts=1500658530453&to_ts=1500662130453&tile_size=m&tpl_var_env=stage)

Load tests for [Firefox Send](https://github.com/mozilla/send).

## Linting (flake8)

```sh
$ tox -e flake8
```

## Docker

There are three different tox targets for Docker:

1. `$ tox -e docker-build`: Builds the latest code into a Docker image.
1. `$ tox -e docker-run`: Runs the latest Docker image.
1. `$ tox -e docker-push`: Pushes the latest Docker image to dockerhub.
