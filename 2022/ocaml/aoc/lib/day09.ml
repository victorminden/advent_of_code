open Core

module IntPair = struct
  module T = struct
    type t = int * int [@@deriving sexp, compare, hash]
  end

  include T
  include Comparable.Make (T)
end

let parse s =
  let parse_dir = function
    | "U" -> (0, 1)
    | "D" -> (0, -1)
    | "L" -> (-1, 0)
    | "R" -> (1, 0)
    | _ -> failwith "ruh roh!"
  in
  s |> String.split_lines
  |> List.map ~f:(fun line ->
         match String.split ~on:' ' line with
         | [ dir; i ] -> (parse_dir dir, int_of_string i)
         | _ -> failwith "ruh roh!")

let new_tpos (hx, hy) (tx, ty) =
  let dx, dy = (hx - tx, hy - ty) in
  match (dx, dy) with
  | 2, 0 | -2, 0 | 0, 2 | 0, -2 -> (tx + (dx / 2), ty + (dy / 2))
  | -1, -1 | -1, 0 | -1, 1 | 0, -1 | 0, 0 | 0, 1 | 1, -1 | 1, 0 | 1, 1 ->
      (tx, ty)
  | _ ->
      let sign v = if v > 0 then 1 else -1 in
      (tx + sign dx, ty + sign dy)

let part_one s =
  let hpos = ref (0, 0) in
  let tpos = ref (0, 0) in
  let h = Hashtbl.create (module IntPair) in
  parse s
  |> List.iter ~f:(fun ((dx, dy), n) ->
         for _step = 1 to n do
           let x, y = !hpos in
           hpos := (x + dx, y + dy);
           tpos := new_tpos !hpos !tpos;
           Hashtbl.add h ~key:!tpos ~data:1 |> ignore
         done);
  Hashtbl.length h

let part_two s =
  let rope_pos = Array.init 10 ~f:(fun _ -> (0, 0)) in
  let h = Hashtbl.create (module IntPair) in
  parse s
  |> List.iter ~f:(fun ((dx, dy), n) ->
         for _step = 1 to n do
           let x, y = rope_pos.(0) in
           rope_pos.(0) <- (x + dx, y + dy);
           for i = 1 to 9 do
             rope_pos.(i) <- new_tpos rope_pos.(i - 1) rope_pos.(i)
           done;
           Hashtbl.add h ~key:rope_pos.(9) ~data:1 |> ignore
         done);
  Hashtbl.length h

let example_data = {|R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2|}

let bigger_example_data = {|R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 13
let%test_unit "part_two" = [%test_eq: int] (bigger_example_data |> part_two) 36
