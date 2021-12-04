open List

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

(* Counts the number of times an element is greater than its predecessor. *)
(* let rec count_increases (depths : int list) : int =
  match depths with
  | a :: b :: tl -> Bool.to_int (b > a) + count_increases (b :: tl)
  | [ a ] -> 0
  | [] -> 0 *)


(* Returns a new list without the first k elements. *)
let drop (lst: int list) (k : int) : int list =
  let f i x : bool = i >= k in
    filteri f lst


(* Returns a new list without the last k elements. *)
let drop_end (lst : int list) (k : int) : int list =
  let len = length lst in
  let f i x : bool = i < len - k in
    filteri f lst


(* Returns the count of the number of times a_k > a_{k-1}. *)
let part1 (depths : int list) : int =
  let acc a b c : int = a + Bool.to_int (b < c) in
  fold_left2 acc 0 (drop_end depths 1) (drop depths 1)


(* Returns the count of the number of times a_k > a_{k-3}.
 * This exploits the observation a + b + c < b + c + d exactly when
 * a < d. *)
let part2 (depths : int list) : int =
  let acc a b c : int = a + Bool.to_int (b < c) in
  fold_left2 acc 0 (drop_end depths 3) (drop depths 3)


let () =
let lines = read_lines "input.txt" in
let depths = List.map int_of_string lines in
  Printf.printf "Part1:\t%d\n\n" (part1 depths);
  Printf.printf "Part2:\t%d\n\n" (part2 depths)
