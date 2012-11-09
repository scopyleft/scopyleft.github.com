# Scopyleft site generator

Clone the repo, init submodules:

```
$ git co sources
$ git submodule init
$ git submodule update
```

Create a Python virtualenv:

```
$ virtualenv --no-site-packages `pwd`/env
$ pip install -r requirements.txt
$ source enb/bin/activate
```

From the `sources` branch, serve the site locally:

```
$ ./builder.py serve --debug
```

To build the static site into the `master` submodule:

```
$ ./builder.py build
```

Update and deploy to the `master` branch:

```
$ cd master # hint: it's a submodule, hence the trick
$ git ci -a -m"updated new version"
$ git push
```

It's automatically pushed online at [scopyleft.fr](http://scopyleft.fr) thanks to github pages.
