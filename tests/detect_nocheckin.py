import pytest

from pre_commit_hooks.detect_nocheckin import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'),
    (
        ('nocheckin_with_multiple_sections.ini', 1),
        ('nonsense.txt', 0),
        ('ok_json.json', 0),
    ),
)
def test_detect_nocheckin(filename, expected_retval):
    ret = main((
        get_resource_path(filename),
    ))
    assert ret == expected_retval


def test_allows_arbitrarily_encoded_files(tmpdir):
    f = tmpdir.join('f')
    f.write_binary(b'\x12\x9a\xe2\xf2')

    ret = main([str(f)])
    assert ret == 0
