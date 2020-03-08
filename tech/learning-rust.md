# Set up your RUST + Cargo environment

## Installation

Let us start setting up our environment by following what is in the official documentation.
You can check it out in [here.](https://www.rust-lang.org/tools/install)
We should just copy the next line and paste it in our terminal:

```bash
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

You can select the default installation option by typing `1`.
After this you should go to your `~/.zshrc` or `~/.bash_profile` and add at the end the next line:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

When you have completed this previous step, go back to your terminal and then type:

```bash
$ source ~/.zshrc
```

With this you will have the RUST tool available in your terminal.
You can verify the installation and that you have added the tools to your path successfully when you input:

```bash
$ rustc --version
##Output: rustc 1.41.1 (f3e1a954d 2020-02-24)
```

### Alternative to installation.

If you just want to play with RUST without installing it in your machine, you can do it in [its official playground.](https://play.rust-lang.org/)

## Your first "Hello, World!" with RUST

Now that you have the RUST tools available in your environment, let us create a new file called `hello.rs`:

```bash
touch hello.rs
```

And inside this file we will copy and paste the following:

```rust
fn main() {
    println!("Hello, world!");
}
```

After we added the code inside the file, we can go back to the terminal and type:

```bash
rustc hello.rs
```

The result of the command will be an executable file that should output: `Hello, world!`.
To execute the file in MacOS you can type:

```bash
$ ./hello
## Output: Hello, world!
```

## Using a Package Manager named Cargo

Nowadays almost every tool has its own package manager, which makes our lives way more easier than in the past. The package manager for RUST is called **Cargo** and you have already installed if you have followed the steps in the first section of this article.
To start using it, we will need some things:

1. Have a folder named `src`
2. Have a file named `main.rs` for applications or `lib.rs` for libraries.
3. A TOML file named `Cargo.toml`
4. Run `cargo build` or `cargo run`

if you are in a Mac you can type the following commands:

```bash
$ mkdir src
$ mv hello.rs ./src/main.rs
$ touch Cargo.toml
```

Inside your `Cargo.toml` file, you can put:

```toml
[package]
name = "hello_world"
version = "1.0.0"
authors = ["YourName <xxxxx@gmail.com>"]
```

Once you have written this, you can build your RUST app with:

```bash
$ cargo build
```

and to run it

```bash
$ cargo run
```

As output you must me seeing now:

```bash
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/hello_world`
Hello, world!
```

### Shortcut to use Cargo

If you do not want to go through the hassle of doing all of the previous step, you can use a command that cargo offers:

```bash
$ cargo new my_rust_app --bin
```

And Voila!
You have now the same files we've just created.

## A simple function

As a natural next step, you would like to create a function.
Let's have a simple function that will sum two signed integers that each takes up to 8 bits of space.

```rust
fn sum(x:i8, y:i8) -> i8{
    x + y
}
```

We need to update our `main.rs` to print out the result from calling the new function:

```rust
fn main() {
    let a:i8 = 1;
    let b:i8 = 2;
    let mut total:i8 = sum(a,b);
    println!("a = {}, b = {}, a+b = {}", a, b, total);
    total = -100;
    println!("New total = {}", total);
}
```

Now run `cargo run` in your terminal, and you should see the beauty of rust.
Try to change some things in the main method, to see how RUST will point out the possible mistakes you have.

## The RUST Book - Documentation

If you want to learn more about RUST you can check its documentation [in HERE.](https://doc.rust-lang.org/book/)
And about Data Types in [this section of the book.](https://doc.rust-lang.org/book/ch03-02-data-types.html)

## End

Hey people, I hope you like this small tutorials, and let me know if you want to learn something else or any other feedback you may have.

Cheers!
