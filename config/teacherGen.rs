use csv::Writer;
use rand::seq::SliceRandom;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let num_teachers = 10;

    let subjects = vec![
        vec!["Mathematics", "", "", ""],
        vec!["English Language", "English Literature", "", ""],
        vec!["Biology", "", "", ""],
        vec!["Chemistry", "", "", ""],
        vec!["Physics", "", "", ""],
        vec!["Religious Studies", "", "", ""],
        vec!["Physical Education", "", "", ""],
        vec!["Computer Science", "", "", ""],
        vec!["History", "", "", ""],
        vec!["Geography", "", "", ""],
        vec!["Modern Language", "French", "German", "Spanish"],
        vec!["Drama & Theatre Studies", "", "", ""],
        vec!["Music", "", "", ""],
        vec!["Electronics", "", "", ""],
    ];

    let mut rng = rand::thread_rng();
    let mut writer = Writer::from_path("teachers.csv")?;

    for teacher in 0..num_teachers {
        let mut row = vec![format!("teacher{}", teacher)];

        let chosen = subjects.choose(&mut rng).unwrap();
        row.extend(chosen.iter().map(|s| s.to_string()));

        writer.write_record(&row)?;
    }

    writer.flush()?;
    Ok(())
}