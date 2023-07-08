open Core

type operation = Nop | Add of int

let parse s =
  s |> String.split_lines
  |> List.map ~f:(fun line ->
         match String.split ~on:' ' line with
         | [ "noop" ] -> Nop
         | [ "addx"; n ] -> Add (int_of_string n)
         | _ -> failwith "ruh roh!")

let part_one s =
  let process t x v =
    incr t;
    match !t with
    | 20 | 60 | 100 | 140 | 180 | 220 -> v := !v + (!t * !x)
    | _ -> ()
  in
  let t = ref 0 in
  let x = ref 1 in
  let v = ref 0 in
  parse s
  |> List.iter ~f:(fun op ->
         match op with
         | Nop -> process t x v
         | Add n ->
             process t x v;
             process t x v;
             x := !x + n);
  !v

let part_two s =
  let process t x v =
    let x0 = !t mod 40 in
    v := !v ^ if !x = x0 || !x + 1 = x0 || !x - 1 = x0 then "#" else ".";
    incr t;
    match !t with 40 | 80 | 120 | 160 | 200 -> v := !v ^ "\n" | _ -> ()
  in
  let t = ref 0 in
  let x = ref 1 in
  let v = ref "" in
  parse s
  |> List.iter ~f:(fun op ->
         match op with
         | Nop -> process t x v
         | Add n ->
             process t x v;
             process t x v;
             x := !x + n);
  !v

let example_data =
  {|addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop|}

let expected_part2_output =
  {|##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 13140

let%test_unit "part_two" =
  [%test_eq: string] (example_data |> part_two) expected_part2_output
