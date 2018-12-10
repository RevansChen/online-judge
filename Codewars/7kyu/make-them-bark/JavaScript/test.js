// JavaScript - Node v8.1.3

console.log('Can you make newly created dogs bark?');
var apollo = new Dog('Apollo', 'Dobermann', 'male', '4');
var zeus = new Dog('Zeus', 'Dobermann', 'male', '4');

Test.assertEquals(apollo.bark(), 'Woof!');
Test.assertEquals(zeus.bark(), 'Woof!');
