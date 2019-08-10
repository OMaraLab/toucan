.. _setup::

Setup
=====

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