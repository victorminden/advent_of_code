open Core
open Aoc
open Aoc.Util

(* Note: shadows deprecated Core function *)
let print_int = string_of_int >> print_endline

let day_runner = function
  | 1, 'a' -> Day01.part_one >> print_int
  | 1, 'b' -> Day01.part_two >> print_int
  | 2, 'a' -> Day02.part_one >> print_int
  | 2, 'b' -> Day02.part_two >> print_int
  | 3, 'a' -> Day03.part_one >> print_int
  | 3, 'b' -> Day03.part_two >> print_int
  | 4, 'a' -> Day04.part_one >> print_int
  | 4, 'b' -> Day04.part_two >> print_int
  | 5, 'a' -> Day05.part_one >> print_endline
  | 5, 'b' -> Day05.part_two >> print_endline
  | 6, 'a' -> Day06.part_one >> print_int
  | 6, 'b' -> Day06.part_two >> print_int
  | 7, 'a' -> Day07.part_one >> print_int
  | 7, 'b' -> Day07.part_two >> print_int
  | 8, 'a' -> Day08.part_one >> print_int
  | 8, 'b' -> Day08.part_two >> print_int
  | 9, 'a' -> Day09.part_one >> print_int
  | 9, 'b' -> Day09.part_two >> print_int
  | _ -> failwith "unrecognized day or part"

let command =
  Command.basic
    ~summary:
      "Run the solution for [day] [part] on the input [filename] and print the \
       result"
    (let%map_open.Command day = anon ("day" %: int)
     and part = anon ("part" %: char)
     and filename = anon ("filename" %: Filename_unix.arg_type) in
     fun () -> filename |> In_channel.read_all |> day_runner (day, part))

let () = Command_unix.run ~version:"1.0" ~build_info:"AOC" command
