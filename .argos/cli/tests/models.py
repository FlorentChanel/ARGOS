from dataclasses import dataclass


@dataclass(frozen=True)
class TestSuite:
    """
    Data class representing the result of a test suite.
    """

    name: str
    total_tests: int
    failed_tests: int
    test_cases: list["TestCase"]
    output: str | None = None

    def __str__(self) -> str:
        lines: list[str] = []
        for case in self.test_cases:
            icon = "🟢" if case.success else "🔴"
            lines.append(f"{icon} {self.name}_{case.name}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return (
            f"TestSuite(name={self.name!r}, total={self.total_tests}, "
            f"failed={self.failed_tests})"
        )


@dataclass(frozen=True)
class TestCase:
    """
    Data class representing the result of a test case.
    """

    name: str
    status: str
    success: bool
    message: str | None = None

    def __str__(self) -> str:
        icon = "🟢" if self.success else "🔴"
        return f"{icon} {self.name}"

    def __repr__(self) -> str:
        return f"TestCase(name={self.name!r}, status={self.status!r}, success={self.success})"
