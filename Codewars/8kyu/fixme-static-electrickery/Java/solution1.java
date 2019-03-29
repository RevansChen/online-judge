// Java - 11

public class Dinglemouse {
    public final static Dinglemouse INST = new Dinglemouse();
    private final static int ONE_HUNDRED = 100;
    private final int value;

    private Dinglemouse() {
        value = ONE_HUNDRED;
    }

    public int plus100(int n) {
        return value + n;
    }
}
