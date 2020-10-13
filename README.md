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

# Usefull terminal tools

## Peco

Great tool to chain / pipe commands which allows you to make a decission in the middle of commands chain
`https://github.com/peco/peco`

# First Installation of Postgresql
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
