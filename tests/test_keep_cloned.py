import os

import pytest

from keep_cloned import refresh, repo_path


@pytest.fixture(autouse=True)
def tmp_cwd(tmp_path):
    os.chdir(tmp_path)


def test_refresh(tmp_path):
    assert not repo_path.exists()
    refresh()
    assert repo_path.exists()
    refresh()
