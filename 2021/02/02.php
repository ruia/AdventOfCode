<?php
include('..\utils\funcs.php');

part1();
part2();


function part1() {
    $contents = read_from_file("in");

    $horizontal_pos = 0;
    $depth = 0;

    foreach ($contents as $line) {
        $movement = explode(" ", $line);
        $command = $movement[0];
        $value = (int) $movement[1];  

        switch ($command) {
            case 'forward':
                $horizontal_pos += $value;
                break;
            case 'down':
                $depth += $value;
                break;
            case 'up':
                $depth -= $value;
                break;
        }
    }

    var_dump($horizontal_pos * $depth);

}

function part2() {
    $contents = read_from_file("in");

    $horizontal_pos = 0;
    $depth = 0;
    $aim = 0;

    foreach ($contents as $line) {
        $movement = explode(" ", $line);
        $command = $movement[0];
        $value = (int) $movement[1];  

        switch ($command) {
            case 'forward':
                $horizontal_pos += $value;
                $depth += ($aim * $value);
                break;
            case 'down':
                $aim += $value;
                break;
            case 'up':
                $aim -= $value;
                break;
        }
    }

    var_dump($horizontal_pos * $depth);
}