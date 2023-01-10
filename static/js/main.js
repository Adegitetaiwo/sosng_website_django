const clickToCopyBtn = document.getElementById("clickToCopy");
function myFunction() {
  /* Get the text field */
  const copyText = document.getElementById("myInput");

   /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.innerText);
    clickToCopyBtn.innerText = "Text Copied to clipboard!"
  /* Alert the copied text */
    setTimeout((e) => {
        clickToCopyBtn.innerText = "Click to Copy text"
    }, 1000)
}