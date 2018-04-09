function setSelection() {
    let sel = document.getElementById('sel1');
    switch(sel.options[sel.selectedIndex].innerHTML) {
        case 'Administrator':
            document.getElementById('administrator-window').hidden = false;
            break;
        case 'Security':
            document.getElementById('security-window').hidden = false;
            break;
        case 'Faculty':
            document.getElementById('faculty-window').hidden = false;
            break;
        case 'Student':
            document.getElementById('student-window').hidden = false;
            break;
    }
    document.getElementById('select-window').hidden = true;
}

function stupidFunction() {

    
}