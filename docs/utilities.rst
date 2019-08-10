
Toucan command-line utilities
=============================

Toucan mostly consists of command-line fun times to make your life easier.


``binlink``
=============

``binlink`` symlinks scripts to ``$HOME/bin``.
  

Here's the ``binlink`` help text. ::

  $ binlink -h
  usage: binlink [-h] [--force] source [target]

  symlink to $HOME/bin

  positional arguments:
      source      source
      target      target
    
  optional arguments:
      -h, --help  show this help message and exit
      --force     overwrite an existing target in $HOME/bin

``gclone``
=============

``gclone`` clones a repository from GitHub. It's a shortcut to save you 
from actually finding the repo and copying the address. If you are 
cloning your own repository and you have set up your `~/.usr_profile`, 
you don't have to specify the username.
  

Here's the ``gclone`` help text. ::

  $ gclone -h
  usage: gclone [-h] [-f] [user] repo [dest]

  Clone repos from GitHub.

  positional arguments:
    user         username (default: lilyminium)
    repo         repository name
    dest         destination directory

  optional arguments:
    -h, --help   show this help message and exit
    -f, --force  Skip command check

``randomize``
=============

Marking, and your Learning Management System can't anonymize student submissions?
Use ``randomize`` to hash submissions while you mark and unhash them 
when you're done with one easy line. The hashes are freely available in 
the file, but you can just drag the file out 
for safekeeping.

This module uses default libraries but likely requires Python 3. It's 
not the most robustly written as we didn't need it to be.
  

Here's the ``randomize`` help text. ::

  $ randomize -h
  usage: randomize [-h] [--back] [path]

  hash paths

  positional arguments:
    path        path to folder of Wattle submissions
    
  optional arguments:
      -h, --help  show this help message and exit
      --back      unhash things

Usage
::

    $ ls *
    +-- examples/
        +-- camel/
        |    +-- camel.png
        |    +-- camel_data.csv
        |    +-- camel_report.docx

        +-- goat/
        |    +-- lab2.docx

        +-- okapi/
        |    +-- psych_report.pdf

        +-- toucan/
        |    +-- toucan_graphs.csv
        |    +-- toucan_submission.pdf

::

    $ randomize
    $ ls *
    +-- examples/
        +-- hashed-4534227490278080168/
        |    +-- hashed-5268810318780526497.pdf
        |    +-- hashed7240516292622205258.csv

        +-- hashed-5807559932020193675/
        |    +-- hashed9023048498483281096.pdf

        +-- hashed-8635424089026415006/
        |    +-- hashed-8352870137889654378.docx

        +-- hashed1862819106113257637/
        |    +-- hashed-4325006337967117557.csv
        |    +-- hashed-892738159033623075.docx
        |    +-- hashed1862819106113257637.png

::

    $ randomize --back
    $ ls *
    +-- examples/
        +-- camel/
        |    +-- camel.png
        |    +-- camel_data.csv
        |    +-- camel_report.docx

        +-- goat/
        |    +-- lab2.docx

        +-- okapi/
        |    +-- psych_report.pdf

        +-- toucan/
        |    +-- toucan_graphs.csv
        |    +-- toucan_submission.pdf
    
