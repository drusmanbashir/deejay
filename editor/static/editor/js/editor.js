$(document).ready(function(){
    $("#slider").slider({
        orientation:"vertical",
        range:"true",
        value:1,
        animate:true,
        max:array.length,
        slide: imageManipulate,
        change: imageManipulate,
    });

    imageManipulate();

    });

function imagePut(ev){

    element = document.getElementById("canvas");
    c = element.getContext("2d");

    // width = element.width;
    // height = element.height;
    im = ev.target;
    c.drawImage(im,0,0);
}


function imageManipulate(){
    var slice = $("#slider").slider("value");


    element = document.getElementById("array_canvas");
    c = element.getContext("2d");


    // read the width and height of the canvas
    width = element.width;
    height = element.height;
    var im = c.createImageData(width,height); // the image, assumed to be 200x200
    i=0;   
    var pos=0;
    // for (y=0;y<height;y++){
    for (x=0;x<size;x++){

        im.data[pos++]=array[slice][0][i];
        im.data[pos++]=array[slice][0][i];
        im.data[pos++]=array[slice][0][i];
        im.data[pos++]=255;
        i++;

    }
    c.putImageData(im,0,0);

}









