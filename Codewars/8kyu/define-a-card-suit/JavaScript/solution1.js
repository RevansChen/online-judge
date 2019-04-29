// JavaScript - Node v8.1.3

function defineSuit(card) {
    suits = {'♣': 'clubs', '♦': 'diamonds', '♥': 'hearts', '♠': 'spades'};
    return suits[card[card.length - 1]];
}
