use std::{env, path::{PathBuf, Path}, fs::File, error::Error, io::Write};

use bedrock_rs::world::World;
use clap::Parser;

#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None, arg_required_else_help = true)]
struct Cli {
    world: PathBuf,
    #[arg(short, long, default_value = env::current_dir().unwrap().into_os_string())]
    output: PathBuf,
}

fn main() -> Result<(), Box<dyn Error>> {
    let cli = Cli::parse();

    let mut world = World::new(cli.world.to_str().unwrap().to_string());
    world.open();

    let mut export_success_count = 0;
    let maps = world.get_all_maps()?;
    for map in maps {
        if map.is_empty() {
            continue;
        }
        let path = Path::new(&cli.output).join(format!("{}.png", map.map_id));
        File::create(path)?.write_all(&map.encode_png())?;
        export_success_count += 1;
    }

    println!("Exported {} maps", export_success_count);

    world.close()?;

    Ok(())
}
