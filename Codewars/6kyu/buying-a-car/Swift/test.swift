// Swift - 4

import XCTest
import Glibc

class SolutionTest: XCTestCase {
    static var allTests = [
        ("nbMonths", testExample)
    ]

    func testing(_ startPriceOld: Int, _ startPriceNew: Int, _ savingPerMonth: Int, _ percentLossByMonth: Double, _ expected: (Int, Int)) {
        let act: (Int, Int) = nbMonths(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth)
        XCTAssertEqual(act.0, expected.0)
        XCTAssertEqual(act.1, expected.1)
    }

    func testExample() {
        testing(2000, 8000, 1000, 1.5, (6, 766))
        testing(12000, 8000, 1000, 1.5 , (0, 4000))
        testing(8000, 12000, 500, 1.0, (8, 597))
        testing(18000, 32000, 1500, 1.25, (8, 332))
        testing(7500, 32000, 300, 1.55, (25, 122))
    }
}

XCTMain([
    testCase(SolutionTest.allTests)
])
