function abc()
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