// JavaScript - Node v8.1.3

const uefaEuro2016 = (teams, scores) => {
    let msg;
    if (scores[0] === scores[1]) {
        msg = 'teams played draw.';
    }
    else {
        msg = `${(scores[0] > scores[1]) ? teams[0] : teams[1]} won!`;
    }
    return `At match ${teams.join(' - ')}, ${msg}`;
}
