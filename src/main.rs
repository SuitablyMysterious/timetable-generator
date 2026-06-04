mod config;

use std::time::Instant;

use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Studentgen {
        #[arg(short, long, default_value_t = 100)]
        num: u32,
    },
    Teachergen {
        #[arg(short, long, default_value_t = 10)]
        num: u32,
    },
}

fn main() {
    let cli = Cli::parse();
    let start = Instant::now();

    match &cli.command {
        Commands::Studentgen { num } => {
            if let Err(e) = config::student_gen::run(*num) {
                eprintln!("Error generating students: {}", e);
            }
        }
        Commands::Teachergen { num } => {
            if let Err(e) = config::teacher_gen::run(*num) {
                eprintln!("Error generating teachers: {}", e);
            }
        }
    }

    let elapsed = start.elapsed();
    println!("Took {}.{:03}s", elapsed.as_secs(), elapsed.subsec_millis());
}
