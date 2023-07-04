open Core

let parse s =
  let parse_boxes s' =
    let lines = s' |> String.split_lines |> List.rev in
    let count =
      lines |> List.hd_exn |> Str.split (Str.regexp "  ") |> List.length
    in
    let boxes = Array.init count ~f:(fun _ -> Stack.create ()) in
    let parse line =
      let i = ref 0 in
      while !i < count do
        (match String.sub ~pos:(4 * !i) ~len:3 line with
        | "   " -> ()
        | abc -> Stack.push boxes.(!i) (String.get abc 1));
        Int.incr i
      done
    in
    lines |> List.tl_exn |> List.iter ~f:parse;
    boxes
  in
  let parse_instructions s' =
    let parse line =
      let arr = line |> String.split ~on:' ' |> Array.of_list in
      (Int.of_string arr.(1), Int.of_string arr.(3), Int.of_string arr.(5))
    in
    s' |> String.split_lines |> List.map ~f:parse
  in
  match Str.split (Str.regexp "\n\n") s with
  | [ b; i ] -> (parse_boxes b, parse_instructions i)
  | _ -> failwith "Bad input"

let read_tops boxes =
  boxes
  |> Array.map ~f:(fun box -> Stack.top_exn box)
  |> Array.to_list |> String.of_char_list

let part_one s =
  let boxes, instructions = parse s in
  let process (n, i, j) =
    for _ = 0 to n - 1 do
      Stack.push boxes.(j - 1) (Stack.pop_exn boxes.(i - 1))
    done
  in

  List.iter ~f:process instructions;
  read_tops boxes

let part_two s =
  let boxes, instructions = parse s in
  let process (n, i, j) =
    let buf = Stack.create () in
    for _ = 0 to n - 1 do
      Stack.push buf (Stack.pop_exn boxes.(i - 1))
    done;
    for _ = 0 to n - 1 do
      Stack.push boxes.(j - 1) (Stack.pop_exn buf)
    done
  in

  List.iter ~f:process instructions;
  read_tops boxes

let example_data =
  {|    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
|}

let%test_unit "part_one" = [%test_eq: string] (example_data |> part_one) "CMZ"
let%test_unit "part_two" = [%test_eq: string] (example_data |> part_two) "MCD"
