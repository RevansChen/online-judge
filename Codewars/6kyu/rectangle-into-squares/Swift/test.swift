// Swift - 4

import XCTest

class SolutionTest: XCTestCase {
    static var allTests = [
        ("sqInRect", testExample)
    ]

    func testing(_ lng: Int, _ wdth: Int, _ expected: [Int]?) {
        XCTAssert(sqInRect(lng, wdth)! == expected!, "should return \(expected!)")
    }

    func testingNil(_ lng: Int, _ wdth: Int) {
        XCTAssertTrue(sqInRect(lng, wdth) == nil, "Should return nil")
    }

    func testExample() {
        testing(5, 3, [3, 2, 1, 1])
        testing(3, 5, [3, 2, 1, 1])
        testingNil(5, 5)
        testing(20, 14, [14, 6, 6, 2, 2, 2])
    }
}

XCTMain([
    testCase(SolutionTest.allTests)
])
