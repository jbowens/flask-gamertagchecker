$(document).ready(function(){

    $("#gamertagForm").submit( function() {

        var span = document.createElement("span");
        $(span).addClass( 'checkInProgress' );
        $(span).html( 'Checking&hellip;' );

        $(span).insertAfter( $("#submit") );

    });

    $("#gamertagBox").keypress( function( e ) {

        if( e.keyCode )
            code = e.keyCode;
        else
            code = e.which;

        var character = String.fromCharCode( code );

        var possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ";

        if( character.length != 0 && possibleChars.indexOf( character ) == -1 && code != 13 )
            e.preventDefault();
        if( $("#gamertagBox").val()[$("#gamertagBox").val().length-1] == " " && code == 32 )
            e.preventDefault();
        if( $("#gamertagBox").val().length == 0 && code == 32 )
            e.preventDefault();
    });

});
