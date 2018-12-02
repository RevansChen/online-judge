# Ruby - MRI 2.5.0

def change(cents)
    cs = [25, 10, 5, 1]
    rc = {}
    cs.each do |c|
        rc[c] = 0
    end
    if cents > 0
        cs.each do |c|
            rc[c] = cents / c
            cents = cents % c
        end
    end
    rc
end
