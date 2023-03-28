<?php
function read_from_file($file_name) {
    $contents = [];

    $file = fopen($file_name, "r") or die("Unable to open file!");
    
    while(!feof($file)) {
        $contents[] = str_replace(array("\r", "\n"), '', fgets($file));
    }
    
    fclose($file);

    return $contents;
}

