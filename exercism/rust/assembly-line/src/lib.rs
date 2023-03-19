const CARS_PER_HOUR: u8 = 221;

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let success_rate = match speed {
        1..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        _ => -1.0,
    };

    return (speed as u16 * CARS_PER_HOUR as u16) as f64 * success_rate;
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / 60.0) as u32
}
