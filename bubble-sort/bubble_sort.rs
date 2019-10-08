fn main() {
    let mut arr: [i32; 5] = [5, 8, 2, 7, 6];
    let length = arr.len();
    let mut swapped = true;

    print_array(&arr);

    while swapped {
        swapped = false;
        for i in 1..length {
            let previous_element = arr[i - 1];
            let current_element = arr[i];

            if previous_element > current_element {
                arr.swap(i - 1, i);
                swapped = true;
            }
        }
    }

    print_array(&arr);
}

fn print_array<T: std::fmt::Display>(array: &[T]) {
    print!("[");
    for (i, elem) in array.iter().enumerate() {
        print!("{}", elem);

        if i != array.len() - 1 {
            print!(",");
        }
    }
    println!("]");
}
