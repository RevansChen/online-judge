// Swift - 3.1.1

import XCTest

class SolutionTest: XCTestCase {
    static var allTests = [
        ("Test Example #1", testExample1),
        ("Test Example #2", testExample2),
        ("Test Example #3", testExample3),
        ("Test Example #4", testExample4),
        ("Test Example #5", testExample5),
        ("Test Example #6", testExample6),
        ("Test Example #7", testExample7),
        ("Test Example #8", testExample8),
        ("Test Example #9", testExample9),
        ("Test Example #10", testExample10),
        ("Test Example #11", testExample11),
        ("Test Example #12", testExample12)
    ]

    func testExample1() {
        XCTAssertEqual(multiply(-10, 10), -100)
    }
    
    func testExample2() {
        XCTAssertEqual(multiply(10, -10), -100)
    }
    
    func testExample3() {
        XCTAssertEqual(multiply(0, 1), 0)
    }
    
    func testExample4() {
        XCTAssertEqual(multiply(1, 1), 1)
    }
    
    func testExample5() {
        XCTAssertEqual(multiply(2, 2), 4)
    }
    
    func testExample6() {
        XCTAssertEqual(multiply(3, 3), 9)
    }
    
    func testExample7() {
        XCTAssertEqual(multiply(4, 3), 12)
    }
    
    func testExample8() {
        XCTAssertEqual(multiply(5, 3), 15)
    }
    
    func testExample9() {
        XCTAssertEqual(multiply(10, 8), 80)
    }
    
    func testExample10() {
        XCTAssertEqual(multiply(10, 10), 100)
    }
    
    func testExample11() {
        XCTAssertEqual(multiply(-10, -10), 100)
    }
    
    func testExample12() {
        XCTAssertEqual(multiply(20, 10), 200)
    }
}

XCTMain([
    testCase(SolutionTest.allTests)
])