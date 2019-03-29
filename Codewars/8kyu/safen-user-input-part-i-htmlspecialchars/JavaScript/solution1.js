// JavaScript - Node v8.1.3

const htmlspecialchars = (formData) => {
    let es = [
        ['&', '&amp;'],
        ['<', '&lt;'],
        ['>', '&gt;'],
        ['"', '&quot;']
    ];
    for (let i in es) {
        formData = formData.replace(new RegExp(es[i][0], 'g'), es[i][1]);
    }
    return formData;
}
