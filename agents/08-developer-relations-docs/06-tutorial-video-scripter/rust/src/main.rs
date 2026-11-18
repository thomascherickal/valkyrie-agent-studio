pub fn script_video_beats(input: &str) -> String {
    format!("[script_video_beats] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[06-tutorial-video-scripter:gemini-4-hydrogen:low] {}", script_video_beats(input))
}

fn main() {
    println!("{}", run_agent("sample"));
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_run() {
        let out = run_agent("verify");
        assert!(out.contains("06-tutorial-video-scripter"));
        assert!(out.contains("script_video_beats"));
    }
}
