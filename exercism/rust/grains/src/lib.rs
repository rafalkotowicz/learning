pub fn square(s: u32) -> u64 {
    match s {
        1..=64 => 2_u64.pow(s - 1),
        // 1..=64 => 1 << (s - 1),
        _ => panic!("Square must be between 1 and 64"),
    }
}

pub fn total() -> u64 {
    (1..=64).map(|x| square(x)).fold(0, |a, b| a + b) as u64
    // ((1_u128 << 64) - 1_u128) as u64
    // u64::MAX
}
