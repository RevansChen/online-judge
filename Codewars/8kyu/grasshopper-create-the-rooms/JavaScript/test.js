// JavaScript - Node v6.11.0

describe('room creation', () => {
    const keys = Object.keys(rooms);
    it('should have at least three rooms', () => {
        Test.assertEquals(keys.length >= 3, true);
    })
    it('each room should be an object', () => {
        keys.forEach(name => {
            Test.expect(typeof(rooms[name]) === 'object', `${name} should be an object`);
        })
    })
    it('should contain at least three properties per room', () => {
        keys.forEach(name => {
            let numKeys = Object.keys(rooms[name]).length;
            Test.expect(numKeys >= 3, `not enough properties for room: ${name}`);
        })
    })
})
