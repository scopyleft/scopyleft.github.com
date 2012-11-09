# Scopylefyt site generator

Clone the repo, then:

```
$ git co sources
$ virtualenv --no-site-packages `pwd`/env
$ pip install -r requirements.txt
$ source enb/bin/activate
```

To serve the site locally:

```
$ ./build serve --debug
```

To build the static site into the `master` submodule:

```
$ ./build build master
```

Update and deploy to master:

```
$ cd master
$ git ci -a -m"updated new version"
$ git push
```

It's automatically pushed online at http://scopyleft.fr thanks to github pages.
