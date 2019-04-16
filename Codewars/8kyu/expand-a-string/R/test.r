# R - 3.4.1

test_that("Sample Tests", {
    expect_equal(expand("hello"), c("h", "e", "l", "l", "o"))
    expect_equal(expand(""), character(0))
})
