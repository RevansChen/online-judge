// JavaScript - Node v8.1.3

describe('class Labrador', _ => {
    it('should instantiate objects as expected', _ => {
        var spitsy = new Labrador('Spitsy', 10, 'Male', 'Donald');
        Test.assertEquals(spitsy.name, 'Spitsy');
        Test.assertEquals(spitsy.age, 10);
        Test.assertEquals(spitsy.gender, 'Male');
        Test.assertEquals(spitsy.species, 'Labrador');
        Test.assertEquals(spitsy.legs, 4);
        Test.assertEquals(spitsy.size, 'Large');
        Test.assertEquals(spitsy.master, 'Donald');
        Test.assertEquals(spitsy.loyal, true);

        var edward = new Labrador('Edward', 3, 'Male', 'Emma');
        Test.assertEquals(edward.name, 'Edward');
        Test.assertEquals(edward.age, 3);
        Test.assertEquals(edward.gender, 'Male');
        Test.assertEquals(edward.species, 'Labrador');
        Test.assertEquals(edward.legs, 4);
        Test.assertEquals(edward.size, 'Large');
        Test.assertEquals(edward.master, 'Emma');
        Test.assertEquals(edward.loyal, true);
    });
});
