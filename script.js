// Get all anchor elements on the page
const anchorElements = document.getElementsByTagName("a");

// Loop through each anchor element and print its href attribute
for (let i = 0; i < anchorElements.length; i++) {
    //it print 2 times same value so i put one condition
    if(i%2==1){
        console.log(anchorElements[i].href);console.log(i);
    }
}
