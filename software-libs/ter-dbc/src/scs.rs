use embassy_time::{Duration, Instant};

pub const DEFAULT_SCS_TIMEOUT: Duration = Duration::from_millis(500);

/// System critical signal wrapper
pub struct SCS<T> {
    message: Option<T>,
    instant: Instant,
    timeout: Duration,
}

impl<T> SCS<T> {
    pub const fn new() -> Self {
        Self {
            message: None,
            instant: Instant::MIN,
            timeout: DEFAULT_SCS_TIMEOUT,
        }
    }

    pub const fn new_with_timeout(timeout: Duration) -> Self {
        Self {
            message: None,
            instant: Instant::MIN,
            timeout,
        }
    }

    pub fn set(&mut self, msg: T) {
        self.instant = Instant::now();
        self.message = Some(msg);
    }

    pub fn get(&self) -> Option<Result<&T, SCSError<'_, T>>> {
        let Some(msg) = &self.message else {
            return None;
        };

        if self.instant.elapsed() > self.timeout {
            return Some(Err(SCSError::SCSTimedOut(msg)));
        }

        Some(Ok(msg))
    }
}

pub enum SCSError<'a, T> {
    SCSTimedOut(&'a T),
}
