function xyz()
{
if($("#first").val()=='' || $("#last").val()==''){alert("First & Last name required");}
    else
{
    if($("#em2").val()==''){alert("kindly put your mail id !");}
else
{
if($("#pass1").val()=='' || $("#pass2").val()==''){alert("Password area required");}
            else{
if($("#pass1").val()!=$("#pass2").val()){alert("Passwords Does not matched");}
                else{
localStorage.setItem("email",$("#em2").val());
localStorage.setItem("password",$("#pass1").val());
    alert("sign up successfull");
    window.location.href="LogIn.html";
                }
            }
        }
    }
}

function abc(){
    if($("#em1").val()==''){alert("Enter Email id");}
    else{
        if($("#em1").val()==localStorage.getItem("email")){
            if($("#pass").val()==''){alert("Enter Password");}
            else{
if($("#pass").val()==localStorage.getItem("password")){
    alert("Sign in Successful");
window.location.href="Menu.html";
                }
else{alert("Wrong Password");}
            }
        }
        else{
    alert("Invalid ID");
        }
    }}
function abc1()
{
    var ksit=navigator.geolocation.getCurrentPosition(onSuccess,onError); //fetch the current location
    function onSuccess(position)  //position -gets current position when called with latitude and longitude
    {
      alert('Latitude:'+position.coords.latitude+'\n'+'Longitude:'+position.coords.longitude+'\n');
    window.location.href="https://www.latlong.net/c/?lat="+position.coords.latitude+"&long="+position.coords.longitude+""
    }
    function onError(error)
    {
        alert('code:'+error.code+'\n'+'message:'+error.message+'\n'); //to get error from service and get message error from given by service
    }
}
