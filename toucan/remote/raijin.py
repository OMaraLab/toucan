#!/usr/bin/env python3

import os
import sys
import subprocess

# environment stuff
REMOTE_DIR = os.environ.get('RJ_HOME_DIR')
USER = os.environ.get('RJ_USER')
PROJECT = os.environ.get('RJ_PROJECT')

# commands
ADDRESS = f'{USER}@raijin.nci.org.au'
HOME = f'{ADDRESS}:/home/{REMOTE_DIR}/{USER}'
SHORT = f'{ADDRESS}:/short/{PROJECT}/{USER}'
RECORDFILE = f'{HOME}/.recordfile'
QSTAT = '/opt/pbs/default/bin/qstat'
QDEL = '/opt/pbs/default/bin/qdel'
DATE = '/bin/echo $(date +%d/%m/%Y)'
NCI_ACCOUNT = '/opt/bin/nci_account'
SHORT_REPORT = f'/opt/bin/short_files_report -P {PROJECT}'
QUEUED = f'{QSTAT} -u {USER} | grep {USER}'
SSH = f'ssh -t -q {ADDRESS}'


def remote(cmd):
    encoding = sys.stdout.encoding
    return subprocess.run(f'{SSH} {cmd}', shell=True,  # necessary for SSH
                          encoding=encoding, stdout=subprocess.PIPE)
