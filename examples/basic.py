"""Minimal example for UpdateChaser."""

from updatechaser import updatechaser


def main():
 runner = updatechaser({"name": "UpdateChaser", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()