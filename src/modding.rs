use pyo3::prelude::*;

#[pyclass]
struct Color {
    r: i32,
    g: i32,
    b: i32,
}

#[pyclass] 
struct Rectangle {
    x: f32,
    y: f32,
    width: f32,
    height: f32,
    color: Color
}