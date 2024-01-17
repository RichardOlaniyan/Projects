<?php
$countries = file_get_contents("countries.json");
$country = json_decode($countries, true);
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="style.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <div id="container"> 
            <h1>Facts about countries</h1>
            <ul>
            <?php
            foreach ($country['countries'] as $key => $value) {
            echo '<h4>'.$value['emoji']." ".$value['name'].'<br /br></h4>';
            echo '<li> Region:'.' '.$value['region'].'</li>';
            echo '<li> Capital:'.' '.$value['capital'].'</li>';
            echo '<li> Phone Code:'.' '.$value['phone_code'].'</li>';
            echo '<li> Currency:'.' '.$value['currency_name'].' '.($value['currency_symbol']).'</li>';
            }
            ?>
        </ul>
        </div>
    </body>
</html>