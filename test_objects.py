import pytest
from objects import CompactSurface

# Test case for vertices property and setter
def test_vertices_property_and_setter():
    vertices = 4
    edges = {(0, 1), (1, 2), (2, 3), (3, 0)}
    gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0))}
    surface = CompactSurface(vertices, edges, gluing)
    assert surface.vertices == vertices

    with pytest.raises(ValueError):
        CompactSurface(3, edges, gluing)  # Odd number of vertices should raise ValueError

    with pytest.raises(ValueError):
        CompactSurface(-4, edges, gluing)  # Negative vertices should raise ValueError

# Test case for edges property and setter
def test_edges_property_and_setter():
    vertices = 4
    edges = {(0, 1), (1, 2), (2, 3), (3, 0)}
    gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0))}
    surface = CompactSurface(vertices, edges, gluing)
    assert surface.edges == edges

    invalid_edges = {(0, 1), (1, 2), (2, 3)}  # Missing one edge
    with pytest.raises(ValueError):
        CompactSurface(vertices, invalid_edges, gluing)  # Should raise ValueError

    invalid_edges2 = {(0, 1), (1, 2), (2, -1), (-1, 0)}  # Invalid vertex (-1)
    with pytest.raises(ValueError):
        CompactSurface(vertices, invalid_edges2, gluing)  # Should raise ValueError

    conflicting_edges = {(0, 1), (1, 0), (2, 3), (3, 2)}  # Conflicting edges
    with pytest.raises(ValueError):
        CompactSurface(vertices, conflicting_edges, gluing)  # Should raise ValueError

# Test case for gluing property and setter
def test_gluing_property_and_setter():
    vertices = 4
    edges = {(0, 1), (1, 2), (2, 3), (3, 0)}
    valid_gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0))}
    surface = CompactSurface(vertices, edges, valid_gluing)
    assert surface.gluing == valid_gluing

    invalid_gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0)), ((0, 1), (1, 2))}  # Extra pair
    with pytest.raises(ValueError):
        CompactSurface(vertices, edges, invalid_gluing)  # Should raise ValueError

    missing_edge_gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0)), ((0, 1), (1, 3))}  # Missing one edge in gluing
    with pytest.raises(ValueError):
        CompactSurface(vertices, edges, missing_edge_gluing)  # Should raise ValueError

# full initialization and properties
def test_compact_surface_initialization():
    vertices = 4
    edges = {(0, 1), (1, 2), (2, 3), (3, 0)}
    valid_gluing = {((0, 1), (2, 3)), ((1, 2), (3, 0))}
    surface = CompactSurface(vertices, edges, valid_gluing)

    assert surface.vertices == vertices
    assert surface.edges == edges
    assert surface.gluing == valid_gluing


