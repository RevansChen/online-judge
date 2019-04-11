// C++ - 14

Describe(person_test) {
    It(should_return_location) {
        Person* person = new Person(1, 2, 3);
        int x = 0, y = 0, z = 0;
        person->location(x, y, z);
        Assert::That(x, Equals(1));
        Assert::That(y, Equals(2));
        Assert::That(z, Equals(3));
    }
};
