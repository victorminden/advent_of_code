#load "str.cma"

(* Reads the lines of a file into a list of strings.
 * Taken from https://stackoverflow.com/a/23456034 *)
let read_lines (filename : string) : string list =
  let ic = open_in filename in
  let try_read () = try Some (input_line ic) with End_of_file -> None in
  let rec loop acc =
    match try_read () with
    | Some s -> loop (s :: acc)
    | None ->
        close_in ic;
        List.rev acc
  in
  loop []

let str2pair (str : string) : string * int =
  let parts = Str.split (Str.regexp " +") str in
  (List.hd parts, int_of_string (List.hd (List.tl parts)))

let parse_input (lines : string list) : (string * int) list =
  List.map str2pair lines

(* An exception to handle any input command string we don't recognize. *)
exception BadInput of string

(* Update the current submarine position (a 2D state) for part1. *)
let update_state_part1 (old : int * int) (delta : string * int) : int * int =
  let old_h, old_d = old and next_command, step = delta in
  match next_command with
  | "forward" -> (old_h + step, old_d)
  | "down" -> (old_h, old_d + step)
  | "up" -> (old_h, old_d - step)
  | _ -> raise (BadInput "Ruh-roh!")

let part1 (commands : (string * int) list) : int =
  let initial_state = (0, 0) in
  let final_state = List.fold_left update_state_part1 initial_state commands in
  let h, d = final_state in
  h * d

(* Update the current submarine position + aim (a 3D state) for part2. *)
let update_state_part2 (old : int * int * int) (delta : string * int) :
    int * int * int =
  let old_h, old_d, old_aim = old and next_command, step = delta in
  match next_command with
  | "forward" -> (old_h + step, old_d + (old_aim * step), old_aim)
  | "down" -> (old_h, old_d, old_aim + step)
  | "up" -> (old_h, old_d, old_aim - step)
  | _ -> raise (BadInput "Ruh-roh!")

let part2 (commands : (string * int) list) : int =
  let initial_state = (0, 0, 0) in
  let final_state = List.fold_left update_state_part2 initial_state commands in
  let h, d, _ = final_state in
  h * d

let () =
  let lines = read_lines "input.txt" in
  let commands = parse_input lines in
  Printf.printf "Part1:\t%d\n\n" (part1 commands);
  Printf.printf "Part2:\t%d\n\n" (part2 commands)
