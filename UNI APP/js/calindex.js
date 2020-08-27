var x=document.getElementById("id1"); //code reusability
function abc(obj)                       //name of the key which u press on calculator is in obj
{
    var pushed=obj.innerHTML;
    if(pushed=="=")
        {
            x.innerHTML=eval(x.innerHTML); //inbuilt function to perform operations parameter=where the result to be printed
        }
    else if(pushed=="AC")
        {
            x.innerHTML="0";
        }
    else
        {
            if(x.innerHTML=="0") //if initially 0 display the key pressed
                {
                    x.innerHTML=pushed;
                }
            else                    //else concatenate with previously entered value
                {
                    x.innerHTML=x.innerHTML+pushed;
                }
        }
}
