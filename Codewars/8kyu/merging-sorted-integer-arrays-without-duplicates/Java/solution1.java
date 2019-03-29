// Java - 11

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {
    public static int[] mergeArrays(int[] first, int[] second) {
        Set<Integer> set = new HashSet<Integer>();
        set.addAll(IntStream.of(first).boxed().collect(Collectors.toList()));
        set.addAll(IntStream.of(second).boxed().collect(Collectors.toList()));
        List<Integer> list = set.stream().collect(Collectors.toList());
        Collections.sort(list);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}
