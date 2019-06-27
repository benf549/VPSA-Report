use super::config::{PythonConfig, PythonRawAllocator, PythonRunMode};

/// Obtain the default Python configuration
///
/// The crate is compiled with a default Python configuration embedded
         /// in the crate. This function will return an instance of that
         /// configuration.
         pub fn default_python_config() -> PythonConfig {
    PythonConfig {
        program_name: "VPSA-Report".to_string(),
        standard_io_encoding: None,
        standard_io_errors: None,
        opt_level: 0,
        use_custom_importlib: true,
        filesystem_importer: false,
        sys_paths: [].to_vec(),
        import_site: false,
        import_user_site: false,
        ignore_python_env: true,
        dont_write_bytecode: true,
        unbuffered_stdio: false,
        frozen_importlib_data: include_bytes!(r#"C:/Users/benfy/Desktop/VPSA-Report\build\target\x86_64-pc-windows-msvc\debug\pyoxidizer\importlib_bootstrap"#),
        frozen_importlib_external_data: include_bytes!(r#"C:/Users/benfy/Desktop/VPSA-Report\build\target\x86_64-pc-windows-msvc\debug\pyoxidizer\importlib_bootstrap_external"#),
        py_modules_data: include_bytes!(r#"C:/Users/benfy/Desktop/VPSA-Report\build\target\x86_64-pc-windows-msvc\debug\pyoxidizer\py-modules"#),
        py_resources_data: include_bytes!(r#"C:/Users/benfy/Desktop/VPSA-Report\build\target\x86_64-pc-windows-msvc\debug\pyoxidizer\python-resources"#),
        argvb: false,
        raw_allocator: PythonRawAllocator::System,
        write_modules_directory_env: None,
        run: PythonRunMode::Eval { code: "import package.VPSA_REPORT as v; v.main()".to_string() },
    }
}
