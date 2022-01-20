use pyo3::prelude::*;

#[pyclass]
struct Color {
    r: i32,
    g: i32,
    b: i32,
}

#[pyclass]
struct Vector {
    x: f32,
    y: f32,
    z: f32,
}

#[pyclass]
struct Triangle {
    v1: Vector,
    v2: Vector,
    v3: Vector,
    color: Color,
}