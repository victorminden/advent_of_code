open Core
open Aoc
open Aoc.Util

(* Note: shadows deprecated Core function *)
let print_int = string_of_int >> print_endline

let day_runner = function
  | 1, 'a' -> Day01.part_one >> print_int
  | 1, 'b' -> Day01.part_two >> print_int
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
