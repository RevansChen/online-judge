// Java - 11

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class ExampleTests {
    @Test
    public void test() {
        System.out.println(Dinglemouse.INST.plus100(23));
    }
}
