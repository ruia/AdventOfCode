<?php
include('..\utils\funcs.php');

part1();
part2();

function part1() {
    // does not account to an win in a columns only rows. 
    // still worked with my input

    $contents_ori = read_from_file("in");
    $numbers = explode(',', $contents_ori[0]);
    $boards = generate_boards($contents_ori);
    
    $numbers_matched = [];
    $last_number = null;
    $winner_board_id = null;

    for ($i=0; $i < count($numbers); $i++) { 
        for ($board_id=0; $board_id < count($boards); $board_id++) { 
            for ($row=0; $row < count($boards[$board_id]); $row++) { 
                for ($col=0; $col < count($boards[$board_id][$row]); $col++) { 
                    if ($numbers[$i] == $boards[$board_id][$row][$col]) {
                        $numbers_matched[$board_id][$row][$col] = $numbers[$i];
                        $boards[$board_id][$row][$col] = '';
                        if (count($numbers_matched[$board_id][$row]) == 5) {
                            $last_number = $numbers[$i];
                            $winner_board_id = $board_id;
                            
                            // echo "BINGO\n";
                            // echo "Board id: $board_id - ROW: $row\n";
                            // echo "Last called number: $numbers[$i]\n";
                            // echo "Winning row: " . implode(' ', $numbers_matched[$board_id][$row]);

                            break 4;
                        }
                    }
                }
            }
        }
    }

    $sum = 0;
    for ($row=0; $row < count($boards[$winner_board_id]); $row++) { 
        for ($col=0; $col < count($boards[$winner_board_id][$row]); $col++) { 
            if ($boards[$winner_board_id][$row][$col] != '') {
                $sum += $boards[$winner_board_id][$row][$col];
            }
        }
    }

    var_dump($sum * $last_number);
}

function part2() {
    $contents_ori = read_from_file("in");
    $numbers = explode(',', $contents_ori[0]);
    $boards = generate_boards($contents_ori);
    
    $last_number = null;
    $winner_board_id = null;
    $victory_count = 0;
    $victory_boards = [];

    for ($i=0; $i < count($numbers); $i++) { 

        for ($board_id=0; $board_id < count($boards); $board_id++) { 

            for ($row=0; $row < 5; $row++) { 
                for ($col=0; $col < 5; $col++) { 

                    if ($boards[$board_id][$row][$col] == $numbers[$i] && !in_array($board_id, $victory_boards)) {
                        $boards[$board_id][$row][$col] = '';
                        $line = false;
                        $column = false;

                        $mark_count = 0;
                        for ($j=0; $j < 5; $j++) { 
                            if ($boards[$board_id][$row][$j] == '') {
                                $mark_count++;
                            } else {
                                break;
                            }
                        }
                        if ($mark_count == 5) {
                            $line = true;
                        }

                        $mark_count = 0;
                        for ($j=0; $j < 5; $j++) { 
                            if ($boards[$board_id][$j][$col] == '') {
                                $mark_count++;
                            } else {
                                break;
                            }
                        }
                        if ($mark_count == 5) {
                            $column = true;
                        }

                        if (($line || $column) && ($victory_count < count($boards)))  {
                            $victory_count++;
                            $last_number = $numbers[$i];
                            $winner_board_id = $board_id;
                            $line = false;
                            $column = false;
                            $victory_boards[] = $winner_board_id;
                        }
                    }
                }
            }
        }
    }

    $sum = 0;
    for ($row=0; $row < count($boards[$winner_board_id]); $row++) { 
        for ($col=0; $col < count($boards[$winner_board_id][$row]); $col++) { 
            if ($boards[$winner_board_id][$row][$col] != '') {
                $sum += $boards[$winner_board_id][$row][$col];
            }
        }
    }

    var_dump($sum * $last_number);
}


function generate_boards($contents_ori) {
    $boards = [];
    $board_id = 0;
    for ($i=2; $i < count($contents_ori); $i++) { 
        if ($contents_ori[$i] == '') {
            $board_id++;
            continue;
        }
        $boards[$board_id][] = explode(' ', str_replace('  ', ' ', trim($contents_ori[$i])));
    }
    return $boards;
}