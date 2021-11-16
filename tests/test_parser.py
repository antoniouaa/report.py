from report_py.main import parse_log, get_repo_name


def test_parse_log(test_log):
    result = parse_log(test_log)
    assert "DOCS" in result
    assert "VBA" in result
    assert "TOOLS" in result
    assert "PARSERS" in result


def test_repo_name():
    name = get_repo_name()
    assert name == "report.py"
