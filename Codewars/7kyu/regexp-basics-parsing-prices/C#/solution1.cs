// C# - 7.3

using System.Linq;
using System.Text.RegularExpressions;

public static class String {
    public static int? ToCents(this string price) =>
        Regex.IsMatch(price, @"\A\$\d+.\d{2}\z") ?
            (int?)int.Parse(string.Concat(price.Where(c => char.IsNumber(c)))) :
            null;
}
