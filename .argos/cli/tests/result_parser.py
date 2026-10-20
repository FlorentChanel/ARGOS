import re
import xml.etree.ElementTree as ET

from .models import TestCase, TestSuite

TEST_SUITE_ATTRIBUTE_NAME = "testsuite"
TEST_CASE_ATTRIBUTE_NAME = "testcase"
FAILURE_ATTRIBUTE_NAME = "failure"

# GTest drops ESC (illegal in XML) from failure messages, leaving bare "[1;37;41m"
# fragments from Utils::formatError(); put it back so the terminal renders colors.
_STRIPPED_ANSI = re.compile(r"(?<!\x1b)\[([0-9;]*)m")


class ResultParser:
    """
    Parses the GTest XML Ouput
    """

    def parse(self, xml_content: str) -> TestSuite:
        xml = ET.fromstring(xml_content)
        testsuites = xml.findall(TEST_SUITE_ATTRIBUTE_NAME)
        if not testsuites:
            raise ValueError("No test suites found in the XML content")

        if len(testsuites) > 1:
            raise ValueError(
                "Multiple test suites found in the XML content. Expected only one."
            )

        test_cases = testsuites[0].findall(TEST_CASE_ATTRIBUTE_NAME)
        if not test_cases:
            raise ValueError("No test cases found in the XML content")

        cases = [self._parse_test_case(test_case) for test_case in test_cases]
        total_tests = len(cases)
        failed_tests = len([case for case in cases if not case.success])
        return TestSuite(
            name=testsuites[0].get("name", "Unnamed Test Suite"),
            total_tests=total_tests,
            failed_tests=failed_tests,
            test_cases=cases,
        )

    def _parse_test_case(self, test_case_element: ET.Element) -> TestCase:
        name = test_case_element.get("name")
        status = test_case_element.get("status")
        success = True
        message = None
        failure_element = test_case_element.find(FAILURE_ATTRIBUTE_NAME)
        if failure_element is not None:
            message = failure_element.get("message")
            if message is not None:
                message = _STRIPPED_ANSI.sub("\x1b[\\1m", message)
            success = False

        if name is None:
            raise ValueError("Test case element is missing the 'name' attribute")

        if status is None:
            raise ValueError("Test case element is missing the 'status' attribute")

        return TestCase(name=name, status=status, success=success, message=message)
