type Input = Vec<Vec<u32>>;

pub fn parse(input: &str) -> Input {
    input.lines().map(descramble).collect()
}

pub fn part1(input: &Input) -> usize {
    input.iter().flatten().filter(|&&d| d == 1 || d == 4 || d == 7 || d == 8).count()
}

pub fn part2(input: &Input) -> u32 {
    input.iter().map(|digits| digits.iter().fold(0, |acc, d| 10 * acc + d)).sum()
}

fn descramble(line: &str) -> Vec<u32> {
    let mut frequency = [0u8; 104];
    let bytes = line.as_bytes();
    bytes[0..58].iter().for_each(|&b| frequency[b as usize] += 1);
    bytes[61..]
        .split(|&b| b == b' ')
        .map(|scrambled| {
            let total = scrambled.iter().map(|&b| frequency[b as usize]).sum();
            to_digit(total)
        })
        .collect()
}

fn to_digit(total: u8) -> u32 {
    match total {
        42 => 0,
        17 => 1,
        34 => 2,
        39 => 3,
        30 => 4,
        37 => 5,
        41 => 6,
        25 => 7,
        49 => 8,
        45 => 9,
        _ => unreachable!(),
    }
}
