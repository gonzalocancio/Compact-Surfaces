# Compact-Surfaces

In this repository we created python class called CompactSurface which represents compact surfaces in the topological sense of the term, and we implemented the algorithm to classify compact surfaces

In this repository we can find four files: classification.py, test_classifiaction.py, objects.py and test_objects.py. Of course, classification.py and objects.py contain the meaningful part of the code, an the other two files just test some of the functions and methods defined in them.

In objects.py we created a python class that is meant to represent compact surfaces:

A compact surface can be represented by a regular polygon with an even number of vertices
where the edges are glued in pairs. Basically it is a directed graph where the underlying
undirected graph is an even polygon, with the edges grouped in pairs forming a partition of
the edge set. The direction of the edges gives a direction to the gluing, so it is important
to keep track of it.

Thus, the CompactSurface class that we have created has three attributes: vertices, edges, and gluing.

The attribute vertices must be an even positive integer, containing the information of the amount of vertices that the polygonal representation of thecompact surface in question has.
The attribute edges must be a set of tuples of the form (i, i+1 ) or (i+1, i) wher 0<= i <= vertices - 1
and in the case i+1 = vertices we write i+1 as 0. That is, we are basically working with the succesor operation in the integers modulo the vertices.
Finally, the gluing attribute is a set of tuples of edges in the edges set just described. It must form a partition of the gluing set.

There are some dgenerate cases when vertices = 2, which amount to the projective plane or the sphere. The encoding for them is handled slightly differently, but the programme works fine with them.

We incorporated some methods for the CompactSurface class that are used in some of the functions in classification.py. The most obvious one is the class method CompactSurface.get() which asks the user for a compact surface.


In classification.py we implemented all the functions that we found necessary for the algorithm to classify compact surfaces.
The algorithm is divided in three main steps: remove spheres, remove projective planes and remove tori, encoded in the functions remove_adjacent_edges, remove_projective_plane and remove_torus, respectively. the idea of the algorithm is to execute them in order at every iteration, and in every iteration, we execute only one of the functions. That is, if there is a spher to remove, we remove it. If not, we move on to try to remove a projective plane, if we succed then we go back to try to remove a sphere. If not, we move into trying to remove a torus. And so on, until we run out of vertices, which, eventually, will happen.


