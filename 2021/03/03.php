<?php
include('..\utils\funcs.php');

part1();
part2();

function part1() {
    $contents = read_from_file("in");
    $bin_gamma_rate = '';
    $bin_epsilon_rate = '';

    foreach ($contents as $line) {
        $individual_bits = str_split($line);
        for ($i=0;$i<count($individual_bits);$i++){
            $groups[$i][] = $individual_bits[$i];
        }
    }

    foreach ($groups as $group) {
        $val_count = array_count_values($group);
        if ($val_count['0'] > $val_count['1']) {
            $bin_gamma_rate .= '0';
            $bin_epsilon_rate .= '1';
        } else {
            $bin_gamma_rate .= '1';
            $bin_epsilon_rate .= '0';
        }
    }

    var_dump(bindec($bin_gamma_rate) * bindec($bin_epsilon_rate));
}

function part2() {
    // not pretty but hey, it works!

    $contents_ori = read_from_file("in");

    $contents = $contents_ori;

    foreach ($contents as $line) {
        $individual_bits = str_split($line);
        for ($i=0;$i<count($individual_bits);$i++){
            $groups[$i][] = $individual_bits[$i];
        }
    }

    for ($i=0; $i < count($groups); $i++) { 
        $val_count = array_count_values($groups[$i]);
        
        if ($val_count['0'] > $val_count['1']) {
            for ($j=0; $j < count($contents); $j++) { 
                if (str_split($contents[$j])[$i] == '0') {
                    $keepers[] = $contents[$j];
                }
            }
        } elseif ($val_count['0'] < $val_count['1'] || $val_count['0'] == $val_count['1']) {
            for ($j=0; $j < count($contents); $j++) { 
                if (str_split($contents[$j])[$i] == '1') {
                    $keepers[] = $contents[$j];
                }
            }
        } 

        $contents = $keepers;
        $keepers = [];
        $groups = [];
        foreach ($contents as $line) {
            $individual_bits = str_split($line);
            for ($k=0;$k<count($individual_bits);$k++){
                $groups[$k][] = $individual_bits[$k];
            }
        }

        if (count($contents) == 1) {
            break;
        }
    }

    $oxygen_generator_rating = bindec($contents[0]);

    $contents = $contents_ori;
    foreach ($contents as $line) {
        $individual_bits = str_split($line);
        for ($i=0;$i<count($individual_bits);$i++){
            $groups[$i][] = $individual_bits[$i];
        }
    }

    for ($i=0; $i < count($groups); $i++) { 
        $val_count = array_count_values($groups[$i]);
        
        if ($val_count['0'] > $val_count['1']) {
            for ($j=0; $j < count($contents); $j++) { 
                if (str_split($contents[$j])[$i] == '1') {
                    $keepers[] = $contents[$j];
                }
            }
        } elseif ($val_count['0'] < $val_count['1'] || $val_count['0'] == $val_count['1']) {
            for ($j=0; $j < count($contents); $j++) { 
                if (str_split($contents[$j])[$i] == '0') {
                    $keepers[] = $contents[$j];
                }
            }
        } 

        $contents = $keepers;
        $keepers = [];
        $groups = [];
        foreach ($contents as $line) {
            $individual_bits = str_split($line);
            for ($k=0;$k<count($individual_bits);$k++){
                $groups[$k][] = $individual_bits[$k];
            }
        }

        if (count($contents) == 1) {
            break;
        }
    }
    $co2_scrubber_rating = bindec($contents[0]);

    var_dump($oxygen_generator_rating * $co2_scrubber_rating);
}