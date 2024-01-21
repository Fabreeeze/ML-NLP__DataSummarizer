function show_value2(x){
    document.getElementById("slider_value2").innerHTML=x;
}

function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myInput");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
}
    
function Check() {

    var reg = /<(.|\n)*>/g;

    if (reg.test(document.getElementById("data").value) == true) {
        var ErrorText = 'Make Sure You Provide Valid Data.';
        alert('Error Text');

    }
}