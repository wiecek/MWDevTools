# MWDevTools
Stash for useful things

# BashProfile
My bash configuration including custom Prompt and some Git Aliases

## Copy scripts

Script for custom PWD in prompt:
```
 cp scripts/short.pwd.py ~/bin/short.pwd.py
```

## Linking
Execute from the root directory:

```
 ln -s `find $PWD -name ".bash_profile"` ~/.bash_profile
```

# Tools

## Peco

Great tool to chain / pipe commands which allows you to make a decission in the middle of commands chain
`https://github.com/peco/peco`

## PG gem
When working with a clean instance of Mac OS you probably don't have the Postgresql client installed.
During the first attempt to install the `pg` gem it will fail, because of missing build libraries.
I prefer not to install the Postgres Client at all, so in order to work around it you can:

Install Postgres Libraries:
`brew install libpq`

Locacate the proper path for this library:
`brew list libpq | grep bin/pg_config`

Configure the bundler to use installed libraries when building Postgres
`bundle config build.pg --with-pg-config=/usr/local/Cellar/libpq/13.0_1/bin/pg_config`

Bundle:
`bundle install`

It should not fail on Postgres anymore ;)

## Dekstop App for Docker
Current version: `https://hub.docker.com/editions/community/docker-ce-desktop-mac/`

## Local Postgres
I prefer to run Postgres via Docker.
In order to start a Docker Container with latest Postgres (you may have to specifiy a version for you project).
Don't forget to change the `PASSWORD` and `NAME` for the Super User

`docker run -d --restart unless-stopped -p 5432:5432 -e POSTGRES_PASSWORD=PASSWORd -e POSTGRES_USER=NAME postgres`

To connect to your brand ne Postgres instance use:
`psql -U maw -W -h localhost -p 5432`

In case that the system does not recognise the `psql` command, you have to link it from Libraries we installed earlier:
`brew link --force libpq`

# Quality of Life improvements

## Enable Auto complete with Git

Source: `https://apple.stackexchange.com/questions/55875/git-auto-complete-for-branches-at-the-command-line`

1. Run `curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash`
2. Restart Terminal (necessary changes in `.bash_profile` where already made)
