open Core

let dir_sizes s =
  let h = Hashtbl.of_alist_exn (module String) [ ("/", 0) ] in

  let process_line cwd line =
    match String.split ~on:' ' line with
    | [ _; "cd"; dir ] ->
        if String.equal ".." dir then Filename.dirname cwd
        else Filename.concat cwd dir
    | [ _; "ls" ] -> cwd
    | [ "dir"; dir ] ->
        Hashtbl.add_exn h ~key:(Filename.concat cwd dir) ~data:0;
        cwd
    | [ size; _file ] ->
        for i = 1 to String.length cwd do
          let s = String.sub cwd ~pos:0 ~len:i in
          Hashtbl.change h s ~f:(function
            | Some x -> Some (x + int_of_string size)
            | None -> None)
        done;

        cwd
    | _ -> failwith "ruh roh!"
  in
  s |> String.split_lines |> List.fold ~init:"/" ~f:process_line |> ignore;
  h

let part_one s =
  s |> dir_sizes |> Hashtbl.data
  |> List.fold ~init:0 ~f:(fun acc x -> if x < 100_000 then acc + x else acc)

let part_two s =
  let sizes = s |> dir_sizes in
  let used_size = Hashtbl.find_exn sizes "/" in
  sizes |> Hashtbl.data
  |> List.filter ~f:(fun x -> 70_000_000 - used_size + x >= 30_000_000)
  |> List.fold ~init:Int.max_value ~f:min

let example_data =
  {|$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 95437
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 24933642
