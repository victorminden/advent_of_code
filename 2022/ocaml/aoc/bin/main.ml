open Core
open Aoc
open Aoc.Util

let day_runner = function
  | 1, 'a' -> Day01.part_one >> string_of_int >> print_endline
  | 1, 'b' -> Day01.part_two >> string_of_int >> print_endline
  | 2, 'a' -> Day02.part_one >> string_of_int >> print_endline
  | 2, 'b' -> Day02.part_two >> string_of_int >> print_endline
  | 3, 'a' -> Day03.part_one >> string_of_int >> print_endline
  | 3, 'b' -> Day03.part_two >> string_of_int >> print_endline
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
