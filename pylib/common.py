
import os
import sys
import tempfile

class Error(Exception):
    pass

def mkdir(path):
    path = str(path)
    if not os.path.exists(path):
        os.makedirs(path)

def get_tmpdir():
    """return unique temporary directory path"""
    tmpdir = os.environ.get('FAB_TMPDIR', '/var/tmp')
    if not os.path.isabs(tmpdir):
        raise Error('FAB_TMPDIR is not absolute path')

    mkdir(tmpdir)
    return tempfile.mkdtemp(prefix="fab-", dir=tmpdir)

## cli common
def fatal(s):
    print >> sys.stderr, "error: " + str(s)
    sys.exit(1)

def warn(s):
    print >> sys.stderr, "warning: " + str(s)
