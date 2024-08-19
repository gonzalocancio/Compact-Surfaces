from classification import remove_adjacent_edges, max_tuple, min_tuple, reverse_edges, reverse_list, remove_projective_plane, identify_torus, remove_torus, surface_classification_printing
from objects import CompactSurface

def test_step1():
        # Test Surface 1: Should remove the pair ((5, 0), (5, 4))
    surface1 = CompactSurface(
        vertices=6,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (5, 4), (5, 0)},
        gluing={((5, 0), (5, 4)), ((0, 1), (2, 3)), ((1, 2), (3, 4))}
    )
    new_surface1 = remove_adjacent_edges(surface1)
    assert new_surface1.vertices == 4
    assert new_surface1.edges == {(0, 1), (1, 2), (2, 3), (3, 0)}
    assert new_surface1.gluing == {((0, 1), (2, 3)), ((1, 2), (3, 0))}

    # Test Surface 2: Should remove the pair ((0, 1), (0, 5))
    surface2 = CompactSurface(
        vertices=6,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)},
        gluing={((0, 1), (0, 5)), ((1, 2), (2, 3)), ((3, 4), (4, 5))}
    )
    new_surface2 = remove_adjacent_edges(surface2)
    assert new_surface2.vertices == 4
    assert new_surface2.edges == {(0, 1), (1, 2), (2, 3), (3, 0)}
    assert new_surface2.gluing == {((0, 1), (1, 2)), ((2, 3), (3,0))}

    # Test Surface 3: Should remove the pair ((1, 0), (1, 2))
    surface3 = CompactSurface(
        vertices=6,
        edges={(1, 0), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)},
        gluing={((1, 0), (1, 2)), ((2, 3), (3, 4)), ((4, 5), (5, 0))}
    )
    new_surface3 = remove_adjacent_edges(surface3)
    assert new_surface3.vertices == 4
    assert new_surface3.edges == {(0, 1), (1, 2), (2, 3), (3, 0)}
    assert new_surface3.gluing == {((0, 1), (1, 2)), ((2, 3), (3,0))}

    # Test Surface 4: Should remove the pair ((4, 5), (4, 3))
    surface4 = CompactSurface(
        vertices=6,
        edges={(0, 1), (1, 2), (2, 3), (4, 3), (4, 5), (5, 0)},
        gluing={((4, 5), (4, 3)), ((0, 1), (1, 2)), ((2, 3), (5, 0))}
    )
    new_surface4 = remove_adjacent_edges(surface4)
    assert new_surface4.vertices == 4
    assert new_surface4.edges == {(0, 1), (1, 2), (2, 3), (3, 0)}
    assert new_surface4.gluing == {((0, 1), (1, 2)), ((2, 3), (3,0))}

# Test cases for max_tuple
def test_max_tuple_normal_case():
    assert max_tuple((1, 2), (3, 4)) == (3, 4)
    assert max_tuple((5, 6), (3, 4)) == (5, 6)
    assert max_tuple((2, 3), (4, 5)) == (4, 5)

def test_max_tuple_degenerate_case():
    assert max_tuple((5, 0), (4, 5)) == (5, 0)

# Test cases for min_tuple
def test_min_tuple_normal_case():
    assert min_tuple((1, 2), (3, 4)) == (1, 2)
    assert min_tuple((5, 6), (3, 4)) == (3, 4)
    assert min_tuple((2, 3), (4, 5)) == (2, 3)

def test_min_tuple_degenerate_case():
    assert min_tuple((5, 0), (1, 2)) == (1, 2)


# Test cases for reverse_edges
def test_reverse_edges():
    assert reverse_edges([(1, 2), (3, 4)]) == [(2, 1), (4, 3)]
    assert reverse_edges([(0, 5), (5, 0)]) == [(5, 0), (0, 5)]
    assert reverse_edges([(7, 3), (2, 6)]) == [(3, 7), (6, 2)]

def test_reverse_edges_empty():
    assert reverse_edges([]) == []

# Test cases for reverse_list
def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([7, 8, 9]) == [9, 8, 7]
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']

def test_reverse_list_empty():
    assert reverse_list([]) == []


def test_remove_projective_plane_basic():
    # Basic case with a clear projective plane
    surface = CompactSurface(
        vertices=6,
        edges={(0, 1), (2, 1), (3, 2), (3, 4), (4, 5), (5, 0)},
        gluing={((4, 5), (0, 1)), ((5, 0), (3, 2)), ((2, 1), (3, 4))}
    )
    result_surface = remove_projective_plane(surface)

    # Expected result: the projective plane should be removed
    expected_vertices = 4
    expected_edges = {(1, 0), (2, 1), (3, 2), (3, 0)}
    expected_gluing = {((1, 0), (3, 2)), ((2, 1), (3, 0))}

    assert result_surface.vertices == expected_vertices
    assert result_surface.edges == expected_edges
    assert result_surface.gluing == expected_gluing

def test_remove_projective_plane_no_plane():
    # Case where there is no projective plane
    surface = CompactSurface(
        vertices=4,
        edges={(0, 1), (1, 2), (3, 2), (0, 3)},
        gluing={((0, 1), (3, 2)), ((1, 2), (0, 3))}
    )
    result_surface = remove_projective_plane(surface)

    # Expected result: no change since no projective plane is present
    assert result_surface.vertices == surface.vertices
    assert result_surface.edges == surface.edges
    assert result_surface.gluing == surface.gluing


def test_remove_projective_plane_multiple_planes():
    # Surface with multiple projective planes (only one should be removed)
    surface = CompactSurface(
        vertices=8,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0)},
        gluing={((0, 1), (4, 5)), ((1, 2), (5, 6)), ((2, 3), (6, 7)), ((3, 4), (7, 0))}
    )
    result_surface = remove_projective_plane(surface)

    # Expected result: one projective plane removed
    expected_vertices = 6
    expected_edges = {(1, 0), (2, 1), (3, 2), (3, 4), (4, 5), (5, 0)}
    expected_gluing = {((5, 0), (1, 0)), ((4, 5), (2, 1)), ((3, 4), (3, 2))}

    assert result_surface.vertices == expected_vertices
    assert result_surface.edges == expected_edges
    assert result_surface.gluing == expected_gluing

def test_identify_torus():
    surface = CompactSurface(
        vertices=6,
        edges={(0, 1), (2, 1), (3, 2), (3, 4), (4, 5), (5, 0)},
        gluing={((4, 5), (0, 1)), ((5, 0), (3, 2)), ((2, 1), (3, 4))}
    )
    assert identify_torus(surface) == (((2, 1), (3, 4)), ((5, 0), (3, 2)))
    surface1 = CompactSurface(
        vertices=6,
        edges={(0, 1), (2, 1), (3, 2), (3, 4), (4, 5), (0, 5)},
        gluing={((4, 5), (0, 1)), ((0, 5), (3, 2)), ((2, 1), (3, 4))}
    )
    assert identify_torus(surface1) == None

    surface2 = CompactSurface(
        vertices=8,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0)},
        gluing={((0, 1), (4, 5)), ((1, 2), (5, 6)), ((2, 3), (6, 7)), ((3, 4), (7, 0))}
    )

    assert identify_torus(surface2) == None

    surface3 = CompactSurface(
        vertices=8,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (5, 4), (5, 6), (7, 6), (7, 0)},
        gluing={((0, 1), (5, 4)), ((1, 2), (5, 6)), ((2, 3), (7, 6)), ((3, 4), (7, 0))}
    )

    assert identify_torus(surface3) == (((0, 1), (5, 4)), ((2, 3), (7, 6)) )


def test_remove_torus():
    surface = CompactSurface(
        vertices=8,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (5, 4), (5, 6), (7, 6), (7, 0)},
        gluing={((0, 1), (5, 4)), ((1, 2), (5, 6)), ((2, 3), (7, 6)), ((3, 4), (7, 0))}
    )
    new_surface = remove_torus(surface)
    assert new_surface.vertices == 4
    assert new_surface.edges == {(0, 1), (1, 2), (2, 3), (3, 0)}
    assert new_surface.gluing == {((3, 0), (0, 1)), ((2, 3), (1, 2))}


    surface1 = CompactSurface(
        vertices=8,
        edges={(0, 1), (1, 2), (2, 3), (3, 4), (5, 4), (6, 5), (7, 6), (0, 7)},
        gluing={((0, 1), (5, 4)), ((1, 2), (6, 5)), ((2, 3), (7, 6)), ((3, 4), (0, 7))}
    )
    new_surface1 = remove_torus(surface1)
    assert new_surface1.vertices == 4
    assert new_surface1.edges == {(1, 0), (2, 1), (2, 3), (3, 0)}
    assert new_surface1.gluing == {((2, 3), (1, 0)), ((3, 0), (2, 1))}


def test_surface_classification_printing():
    # we test the most typical surfaces
    sphere = CompactSurface(
    vertices=2,
    edges={(0, 1)},  # A single edge
    gluing={((0, 1), (0, 1))}  # Glue the edge to itself in the same orientation
    )

    projective_plane = CompactSurface(
        vertices=2,
        edges={(0, 1), (1, 0)},  # A single edge
        gluing={((0, 1), (1, 0))}  # Glue the edge to itself with a twist
    )

    torus = CompactSurface(
        vertices=4,
        edges={(0, 1), (1, 2), (3, 2), (0, 3)},  # A square with four edges
        gluing={((0, 1), (3, 2)), ((1, 2), (0, 3))}  # Opposite sides are glued together
    )

    klein_bottle = CompactSurface(
        vertices=4,
        edges={(0, 1), (1, 2), (2, 3), (0, 3)},  # A square with four edges
        gluing={((0, 1), (2, 3)), ((1, 2), (0, 3))}  # Opposite sides are glued together
    )

    assert surface_classification_printing(sphere) == "This is a sphere"
    assert surface_classification_printing(projective_plane) == "This is a projective plane"
    assert surface_classification_printing(torus) == "This is a torus"
    assert surface_classification_printing(klein_bottle) == "This is a Klein Bottle"

    # no we test some non-orientable surfaces

    compact_surface_6 = CompactSurface(
    vertices=6,
    edges={(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)},
    gluing={((0,1), (1, 2)), ((2, 3), (3, 4)), ((4, 5), (5, 0))}
    )

    compact_surface_8 = CompactSurface(
    vertices=8,
    edges={(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0)},
    gluing={((0,1), (1, 2)), ((2, 3), (3, 4)), ((4, 5), (5, 6)), ((6, 7), (7, 0))}
    )
    compact_surface_10 = CompactSurface(
    vertices=10,
    edges={(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)},
    gluing={((0,1), (1, 2)), ((2, 3), (3, 4)), ((4, 5), (5, 6)), ((6, 7), (7, 8)), ((8, 9), (9, 0))}
    )
    compact_surface_12 = CompactSurface(
    vertices=12,
    edges={(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 0)},
    gluing={((0,1), (1, 2)), ((2, 3), (3, 4)), ((4, 5), (5, 6)), ((6, 7), (7, 8)), ((8, 9), (9, 10)), ((10, 11), (11, 0))}
    )

    assert surface_classification_printing(compact_surface_6) == "This is a connected sum of 3 projective planes"
    assert surface_classification_printing(compact_surface_8) == "This is a connected sum of 4 projective planes"
    assert surface_classification_printing(compact_surface_10) == "This is a connected sum of 5 projective planes"
    assert surface_classification_printing(compact_surface_12) == "This is a connected sum of 6 projective planes"

    compact_osurface_8 = CompactSurface(
    vertices=8,
    edges={(0, 1), (1, 2), (3, 2), (4, 3), (4, 5), (5, 6), (7, 6), (0, 7)},
    gluing={((0, 1), (3, 2)), ((1, 2), (4, 3)), ((4, 5), (7, 6)), ((5, 6), (0, 7))}
    )

    compact_osurface_12 = CompactSurface(
    vertices=12,
    edges={(0, 1), (1, 2), (3, 2), (4, 3), (4, 5), (5, 6), (7, 6), (8, 7), (8, 9), (9, 10), (11, 10), (0, 11)},
    gluing={((0, 1), (3, 2)), ((1, 2), (4, 3)), ((4, 5), (7, 6)), ((5, 6), (8, 7)), ((8, 9), (11, 10)), ((9, 10), (0, 11))}
    )

    compact_osurface_16 = CompactSurface(
    vertices=16,
    edges={
        (0, 1), (1, 2), (3, 2), (4, 3),
        (4, 5), (5, 6), (7, 6), (8, 7),
        (8, 9), (9, 10), (11, 10), (12, 11),
        (12, 13), (13, 14), (15, 14), (0, 15)
    },
    gluing={
        ((0, 1), (3, 2)), ((1, 2), (4, 3)),
        ((4, 5), (7, 6)), ((5, 6), (8, 7)),
        ((8, 9), (11, 10)), ((9, 10), (12, 11)),
        ((12, 13), (15, 14)), ((13, 14), (0, 15))
    }
    )

    compact_osurface_20 = CompactSurface(
    vertices=20,
    edges={
        (0, 1), (1, 2), (3, 2), (4, 3),
        (4, 5), (5, 6), (7, 6), (8, 7),
        (8, 9), (9, 10), (11, 10), (12, 11),
        (12, 13), (13, 14), (15, 14), (16, 15),
        (16, 17), (17, 18), (19, 18), (0, 19)
    },
    gluing={
        ((0, 1), (3, 2)), ((1, 2), (4, 3)),
        ((4, 5), (7, 6)), ((5, 6), (8, 7)),
        ((8, 9), (11, 10)), ((9, 10), (12, 11)),
        ((12, 13), (15, 14)), ((13, 14), (16, 15)),
        ((16, 17), (19, 18)), ((17, 18), (0, 19))
    }
    )

    assert surface_classification_printing(compact_osurface_8) == "This is a connected sum of 2 tori"
    assert surface_classification_printing(compact_osurface_12) == "This is a connected sum of 3 tori"
    assert surface_classification_printing(compact_osurface_16) == "This is a connected sum of 4 tori"
    assert surface_classification_printing(compact_osurface_20) == "This is a connected sum of 5 tori"












