<?php
$login = false;
unset($ID);
require './session.php';

/*
 * session.php will contain login details
 * like the student currently loged in
 * etc etc
 * 
 * $ID is the student ID used at login
 * if ID< 100 it implies a senior and 
 * for ID>=100 we have student volunteers
 * The definition is in ./session.php
 */


if (!$login) {
    if ($_SESSION["student"] == $VOLUNTEER_LOGIN) {
        require './volunredirect.php';
    } else if ($_SESSION["student"] == $SENIOR_LOGIN) {
        require './seniorredirect.php';
    }
}


?>
<!DOCTYPE html> 

<html>

    <head>
        <style>
            /*
            * this is for the message box : logout etc
            */
            
            #msg_box{
                   width:30%;
                   height:40%;
                   opacity :1;
                   position:fixed;
                   margin-left:-200px; /* half of width */
                   margin-top:-150px;  /* half of height */
                   top:10%;
                   left:50%;
                                
            }
            
            #reg{
                    text-align: center;
                    width:30%;
                   height:40%;
                   opacity :1;
                   position:fixed;
                   margin-left:-200px; /* half of width */
                   margin-top:-150px;  /* half of height */
                   top:90%;
                   left:50%;
                                
            }
            /*
            * addition 1
            * To ()absolute) center the code
            * find a method to do relative center
            */
            #box{
                   
                   width:30%;
                   height:40%;
                   opacity :1;
                   position:fixed;
                   margin-left:-200px; /* half of width */
                   margin-top:-150px;  /* half of height */
                   top:50%;
                   left:50%;
                }
                
            /*
            * addition 2
            * A background texture
            */
            html{ 
                    background: url('img/bg.png') no-repeat center center fixed; 
                    -webkit-background-size: cover;
                    -moz-background-size: cover;
                    -o-background-size: cover;
                    background-size: cover;
                }
              /*
               * addition 3
               * Loginbox shadow
              */ 
              #loginbox
              {
                  opacity : 0.7;               
                  box-shadow: 15px 15px 15px #4F4A4A;
              }
              
              #box2.td
              {
                   opacity : 0.5;
                  
              }
            
            input {
                border:0px solid #ffcfa4;
                border-radius:10px;
                padding:3px 5px;
            }

            input:hover, input:focus {
                box-shadow: 0px 0px 10px 2px rgba(48, 38, 141, 1);
            }
        </style>
        <title>Sponsorship Login Portal</title> 
    </head>

    <body>

        <!--<img src="http://localhost/projects/aegis/bg2.jpg" alt="Background"> -->
        
        
        <table id="msg_box" width="100%">
            <tr>
                <td style=" text-align:center;
                    <?php
                    /* this piece of php is for rediect messages
                     * if you are redirected from some other page,say a logout
                     * caused you to be here , that message will be printed
                     * the msg and the colour is set by the page redirecting you
                     */
                                if (isset($_GET["color"])) {
                                    echo "color:#{$_GET["color"]};";
                                }
                           ?>font-weight:bolder;">
                <?php
                if (isset($_GET["msg"]))
                    {
                    echo $_GET["msg"];
                }
                ?>
                </td>
            </tr>
        </table>

        <!-- it seems the form action login.php is called upon after the form 
            terminates -->

        <form action="login.php" method="post" name="login_form">

            <table id="box" <!--bgcolor="#ffffff" border="0" cellspacing="0" cellpadding="0" width="100%"-->
                
                <tr>
                    <td align="center" >
                <center>
                    
                    <!--border:10px solid #EE872A;-->
                    <div id="loginbox"  style="font-family:verdana;background-color:#9FA4B5;padding:20px;border-radius:10px;width:350px;">
                        <table id="box2" style="border:0px;width:350">
                            <tr>
                                    
                                <td  id="td" style="background-color:#fffff;text-align:center;">
                                    <b>IIT Patna Sponsorship Portal </b>
                                </td>
                            
                            </tr>
                                

                            <tr>
                                <td align="left">
                                    <table align="center" border="0" width="100%">
                                        <tr > <b></br></b></tr>
                                        <tr>
                                            <td align="right" width="30%">StudentID:</td> 
                                            <td align="left" width="70%">
                                                <input type="text" name="login_id" value="" autofocus="autofocus"/>
                                            </td>
                                        </tr>

                                        <tr>
                                            <td align="right" width="30%">Password:</td>
                                            <td align="left" width="70%">
                                                <input type="password" name="login_pwd" />
                                            </td>
                                        </tr>
                                        
                                    </table>
                                    <tr > <b></br></b></tr>
                                </td>
                            </tr>
                            
                            <tr><td align="left"><center><input type="submit" value="Login" /></center></td>
                            </tr>
                        </table>
                    </div>
                </center></td>
                </tr>
                
        <tr>
            <td id="reg"> <a style="color:  #000000;"href="register.php">Register new user</a></td>
        </tr>
            </table>

        </form>

    </body>
</html> 
