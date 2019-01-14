// C++ - 14

Describe(greet_normally) {
    It(should_append_names) {
        Assert::That(greet("James"), Equals("Hello, James!"));
        Assert::That(greet("Jane"), Equals("Hello, Jane!"));
        Assert::That(greet("Jim"), Equals("Hello, Jim!"));
    }
};

Describe(greet_johnny) {
    It(should_be_a_little_more_special) {
        Assert::That(greet("Johnny"), Equals("Hello, my love!"));
    }
};
