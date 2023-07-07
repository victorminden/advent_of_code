open Core

let make_grid s =
  let lines = String.split_lines s in
  let n = List.length lines in
  let grid = Array.make_matrix ~dimx:n ~dimy:n 0 in
  List.iteri lines ~f:(fun i line ->
      String.iteri line ~f:(fun j c -> grid.(i).(j) <- Char.get_digit_exn c));
  grid

let part_one s =
  let grid = make_grid s in
  let n = Array.length grid in
  let v = ref 0 in
  for i = 0 to n - 1 do
    for j = 0 to n - 1 do
      let curr = grid.(i).(j) in
      let is_visible = Array.of_list [ true; true; true; true ] in
      for k = 1 to n - 1 do
        if i - k >= 0 && grid.(i - k).(j) >= curr then is_visible.(0) <- false;
        if j - k >= 0 && grid.(i).(j - k) >= curr then is_visible.(1) <- false;
        if i + k < n && grid.(i + k).(j) >= curr then is_visible.(2) <- false;
        if j + k < n && grid.(i).(j + k) >= curr then is_visible.(3) <- false
      done;
      v :=
        !v
        + Array.fold is_visible ~init:0 ~f:(fun acc x -> if x then 1 else acc)
    done
  done;
  !v

let part_two s =
  let grid = make_grid s in
  let n = Array.length grid in
  let v = ref 0 in
  for i = 0 to n - 1 do
    for j = 0 to n - 1 do
      let curr = grid.(i).(j) in
      let is_visible = Array.of_list [ true; true; true; true ] in
      let score = Array.of_list [ i; j; n - i - 1; n - j - 1 ] in
      for k = 1 to n - 1 do
        if is_visible.(0) && i - k >= 0 && grid.(i - k).(j) >= curr then (
          is_visible.(0) <- false;
          score.(0) <- k);
        if is_visible.(1) && j - k >= 0 && grid.(i).(j - k) >= curr then (
          is_visible.(1) <- false;
          score.(1) <- k);
        if is_visible.(2) && i + k < n && grid.(i + k).(j) >= curr then (
          is_visible.(2) <- false;
          score.(2) <- k);
        if is_visible.(3) && j + k < n && grid.(i).(j + k) >= curr then (
          is_visible.(3) <- false;
          score.(3) <- k)
      done;
      v := max !v (Array.fold score ~init:1 ~f:( * ))
    done
  done;
  !v

let example_data = {|30373
25512
65332
33549
35390|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 21
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 8
