class MyTestCases extends TestCase {
    public function test_static_operations() {
        $this->assertEquals("I", solution(1));
        $this->assertEquals("IV", solution(4));
        $this->assertEquals("VI", solution(6));
        $this->assertEquals("CLXXXII", solution(182));
        $this->assertEquals("MCMXC", solution(1990));
        $this->assertEquals("MDCCCLXXV", solution(1875));
        $this->assertEquals("MMVIII", solution(2008));
        $this->assertEquals("MDCLXVI", solution(1666));
        $this->assertEquals("M", solution(1000));
        $this->assertEquals("MMVII", solution(2007));
    }
}