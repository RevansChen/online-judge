// C++ - 14

Describe(must_work) {
    It(should_actually_work) {
        Assert::That(brainfuck::execute(to_brainfuck("Hello World!")), Equals("Hello World!"));
        Assert::That(brainfuck::execute(to_brainfuck("Bye bye birdy")), Equals("Bye bye birdy"));
    }
};
