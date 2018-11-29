// Swift - 4

import XCTest
import Glibc

class SolutionTest: XCTestCase {
    static var allTests = [
        ("fcn", testExample)
    ]

    func testequal(_ n: UInt64, _ expected: UInt64) {
        XCTAssertEqual(fcn(n), expected)
    }

    func testExample() {
        testequal(17, 131072)
        testequal(21, 2097152)
    }
}

XCTMain([
    testCase(SolutionTest.allTests)
])
