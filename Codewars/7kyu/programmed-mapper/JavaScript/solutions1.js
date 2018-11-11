// JavaScript - Node v8.1.3

function mapEmUp(input, mappers) {
    var output = [];
    var flag = true;
    for (var inputIndex in input) {
        flag = true;
        for (var i in mappers) {
            if (mappers[i][0](input[inputIndex])) {
                output.push(mappers[i][1](input[inputIndex]));
                flag = false;
                break;
            }
        }
        if (flag) {
            output.push(-1);
        }
    }
    return output;
}
