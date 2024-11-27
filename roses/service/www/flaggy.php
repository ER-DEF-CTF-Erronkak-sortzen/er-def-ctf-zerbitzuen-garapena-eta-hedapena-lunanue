<html>
    <head>
        <title>Welcome to the CTF</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body style="background-color:#000000;"><br><br><h1>Here are the FLAGS</h1>
        <center>
        <div class="container-fluid">
        
        <?php    
        $fp = fopen("dontlookhere.txt","r");
        echo fpassthru($fp);
        fclose($fp); ?>
            
        </div>
        </center>
    </body>
</html>
