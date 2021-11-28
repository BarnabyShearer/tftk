"""Test filtering Terraform plan."""

from io import StringIO

from tftool import _filter


def test_filter() -> None:
    """Test filtering."""
    assert (
        list(
            _filter(
                StringIO(
                    """{
  "resource_changes": [
    {
      "address": "somthing.main",
      "name": "main",
      "type": "somthing",
      "change": {
        "actions": ["create"]
      }
    },
    {
      "address": "github_repository_file.main",
      "name": "main",
      "type": "github_repository_file",
      "change": {
        "actions": ["create"],
        "after": {
          "repository": "repo",
          "file": "main.py"
        }
      }
    },
    {
      "address": "somthing.else",
      "type": "somthing",
      "change": {
        "actions": ["create"]
      }
    },
    {
      "address": "somthing.main2",
      "type": "somthing",
      "change": {
        "actions": ["no-op"]
      }
    }
  ]
}"""
                ),
                "main",
                True,
                True,
                True,
                False,
            )
        )
        == [("somthing.main", "main"), ("github_repository_file.main", "repo/main.py")]
    )
