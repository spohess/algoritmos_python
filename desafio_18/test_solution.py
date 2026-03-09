from solution import simplify_path


class TestSimplifyPath:
    def test_basic(self):
        assert simplify_path("/home/") == "/home"

    def test_double_dot(self):
        assert simplify_path("/a/b/../c") == "/a/c"

    def test_root(self):
        assert simplify_path("/") == "/"

    def test_multiple_slashes(self):
        assert simplify_path("/home//foo/") == "/home/foo"

    def test_dot(self):
        assert simplify_path("/a/./b/./c") == "/a/b/c"

    def test_double_dot_at_root(self):
        assert simplify_path("/../") == "/"

    def test_complex(self):
        assert simplify_path("/a/b/c/../../d") == "/a/d"

    def test_triple_dot_is_name(self):
        assert simplify_path("/a/.../b") == "/a/.../b"

    def test_many_slashes(self):
        assert simplify_path("///a///b///") == "/a/b"

    def test_only_dots_and_slashes(self):
        assert simplify_path("/./././.") == "/"

    def test_deep_back(self):
        assert simplify_path("/a/b/c/d/../../../../e") == "/e"

    def test_back_beyond_root(self):
        assert simplify_path("/a/../../../b") == "/b"
