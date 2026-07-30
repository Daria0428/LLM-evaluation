import json
from pathlib import Path
from typing import Any


def read_jsonl(file_path: str) -> list[dict[str, Any]]:
    """读取JSONL文件并返回字典列表。"""
    records: list[dict[str, Any]] = []
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                record = json.loads(line)
                records.append(record)
            except json.JSONDecodeError as error:
                print(f"第{line_number}行JSON格式错误：{error}")

    return records


def main() -> None:
    records = read_jsonl("data/sample.jsonl")

    print(f"成功读取 {len(records)} 条数据")

    for index, record in enumerate(records, start=1):
        print(f"{index}. {record['question']} -> {record['answer']}")


if __name__ == "__main__":
    main()