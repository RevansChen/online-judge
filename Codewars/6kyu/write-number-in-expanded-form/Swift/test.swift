// Swift - 4

import XCTest

class ExampleTest: XCTestCase {
    static let testValues = [
        (12, "10 + 2"),
        (42, "40 + 2"),
        (70304, "70000 + 300 + 4")
    ]

    static var allTests = [
        ("Simple Tests", tests)
    ]

    func tests() {
        for test in ExampleTest.testValues {
            XCTAssertEqual(expandedForm(test.0), test.1)
        }
    }
}

XCTMain([
    testCase(ExampleTest.allTests)
])
