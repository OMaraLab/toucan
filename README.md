toucan
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/toucan.png)](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/toucan)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/toucan/branch/master)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/toucan/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/toucan/branch/master)

TOols and Utilities for the can-do toucan

[Documentation available here.](https://omara.readthedocs.io/projects/toucan/en/latest/)

## Installation
You should have Python 3.6+.

Install the 'package' by cloning the repo and running `setup.py`. 
This is likely to be constantly updated, so I personally go `python setup.py develop`.
```console
$ git clone git@github.com:OMaraLab/toucan.git
$ cd toucan
$ python setup.py develop
```

Some of the utilities use information such as your Raijin account details, 
or your GitHub username. To set this up, use the make_user_profile script 
to write a `$HOME/.usr_profile` that provides these details.

I usually just clone this repository and add `toucan/toucan/utilities` to 
my path. You can do this by adding the line below to your `~/.bashrc`:

```console
export PATH=/path/to/dir/toucan/toucan/utilties:$PATH
```

You may also have to add execute permissions to the files.
```console
$ chmod a+x *
```

### Copyright

Copyright (c) 2019, OMaraLab


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms)
