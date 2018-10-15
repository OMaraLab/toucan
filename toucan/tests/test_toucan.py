"""
Unit and regression test for the toucan package.
"""

# Import package, test suite, and other packages as needed
import toucan
import pytest
import sys

def test_toucan_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "toucan" in sys.modules
