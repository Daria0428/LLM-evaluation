def calculate_accuracy(correct: int, total: int) -> float:
    """计算准确率，并处理空数据。"""
    if total == 0:
        return 0.0

    return correct / total


def main() -> None:
    correct = 8
    total = 10

    accuracy = calculate_accuracy(correct, total)

    print(f"正确数量：{correct}")
    print(f"总样本数：{total}")
    print(f"准确率：{accuracy:.2%}")


if __name__ == "__main__":
    main()