<?php
include('..\utils\funcs.php');

part1();
part2();


function part1() {
    $contents = read_from_file("in");

    $count = 0;
    $cur = $contents[0];
    for($i=1; $i < count($contents); $i++) {
    if ($contents[$i] > $cur) {
        $count++;
    }
    $cur = $contents[$i];
    }
    
    var_dump($count);
}

function part2() {
    $contents = read_from_file("in");

    $count = 0;
    $cur = $contents[0]+$contents[1]+$contents[2];

    for($i=1; $i < count($contents)-2; $i++) {
        $group_sum = $contents[$i] + $contents[$i+1] + $contents[$i+2];
        if ($group_sum > $cur) {
            $count++;
        }

        $cur = $group_sum;
    }   

    var_dump($count);
}