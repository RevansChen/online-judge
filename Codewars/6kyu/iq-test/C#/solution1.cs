// C# - 7.3

using System;
using System.Linq;
using System.Collections.Generic;

public class IQ {
    public static int Test(string numbers) {
        List<int> nums = new List<int>();
        foreach (string number in numbers.Split(' ')) {
            nums.Add(Convert.ToInt32(number) & 1);
        }
        int target = ((nums.Sum() == 1) ? 1 : 0);

        return nums.IndexOf(target) + 1;
    }
}
