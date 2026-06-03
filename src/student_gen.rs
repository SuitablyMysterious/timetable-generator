use rand::prelude::SliceRandom;
use rand::rng;
use std::fs::File;
use std::io::{BufWriter, Write};

pub fn run(num_students: u32) -> std::io::Result<()> {
    let num_subjects_per = 9;

    let subjects = vec![
        "Mathematics",
        "English Language",
        "English Literature",
        "Biology",
        "Chemistry",
        "Physics",
        "Modern Language",
        "Religious Studies",
        "Physical Education",
        "Computer Science",
        "History",
        "Geography",
        "French",
        "German",
        "Spanish",
        "Drama & Theatre Studies",
        "Music",
        "Electronics",
    ];

    let file = File::create("students.csv")?;
    let mut writer = BufWriter::new(file);
    let mut rng = rng();

    for student in 0..num_students {
        let mut shuffled_subjects = subjects.clone();
        shuffled_subjects.shuffle(&mut rng);

        let selected_subjects = &shuffled_subjects[..num_subjects_per];

        write!(writer, "student{}", student)?;

        for subject in selected_subjects {
            write!(writer, ",{}", subject)?;
        }

        writeln!(writer)?;
    }

    Ok(())
}
