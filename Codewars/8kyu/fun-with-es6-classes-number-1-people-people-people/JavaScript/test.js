// JavaScript - Node v8.1.3

describe('Example Tests', _ => {
    // Default Arguments Test
    Test.assertEquals(new Person().firstName, 'John');
    Test.assertEquals(new Person().lastName, 'Doe');
    Test.assertEquals(new Person().age, 0);
    Test.assertEquals(new Person().gender, 'Male');
    Test.assertEquals(new Person().sayFullName(), 'John Doe');

    // Example Custom Test
    Test.assertEquals(new Person('Jane', 'Doe', 25, 'Female').firstName, 'Jane');
    Test.assertEquals(new Person('Jane', 'Doe', 25, 'Female').lastName, 'Doe');
    Test.assertEquals(new Person('Jane', 'Doe', 25, 'Female').age, 25);
    Test.assertEquals(new Person('Jane', 'Doe', 25, 'Female').gender, 'Female');
    Test.assertEquals(new Person('Jane', 'Doe', 25, 'Female').sayFullName(), 'Jane Doe');
});
