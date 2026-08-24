use dbc_codegen2::{CodegenConfig, CodegenPipeline, Language};
use std::collections::HashMap;

fn main() -> anyhow::Result<()> {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-changed=ter.dbc");

    let config = CodegenConfig {
        inputs: vec!["ter.dbc".to_string()],
        output: format!("{}/generated", std::env::var("OUT_DIR")?),
        lang: Language::Rust,
        no_enum_other: true, // Maybe we want this set to false?
        no_enum_dedup: false,
        zero_zero_range_allows_all: false,
        rust_code_injections: HashMap::new(),
        cpp_code_injections: HashMap::new(),
        generate_tests: true,
        separate: false,
    };

    CodegenPipeline::run(config)
}
