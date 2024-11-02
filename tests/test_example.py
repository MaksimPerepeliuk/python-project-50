from gendiff.scripts.gendiff import generate_diff
import json


RIGHT_DIFF_STR = """{
  "- follow": false,
  "  host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50,
  "+ timeout": 20,
  "+ verbose": true
}"""


def test_generate_diff():
    obj1 = json.load(open('tests/fixtures/file1.json'))
    obj2 = json.load(open('tests/fixtures/file2.json'))

    result = generate_diff(obj1, obj2)
    assert RIGHT_DIFF_STR == result
