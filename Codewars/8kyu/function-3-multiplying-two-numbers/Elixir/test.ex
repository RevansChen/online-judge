# Elixir - 1.2.4

defmodule TestSimpleMath do
    use ExUnit.Case

    test "module provides multiply function" do
        assert {:multiply, 2} in SimpleMath.__info__(:functions)
    end

    test "calculates multiplications for different numbers" do
        assert SimpleMath.multiply(0, 1) == 0
        assert SimpleMath.multiply(1, 1) == 1
        assert SimpleMath.multiply(2, 2) == 4
        assert SimpleMath.multiply(3, 3) == 9
        assert SimpleMath.multiply(4, 3) == 12
        assert SimpleMath.multiply(5, 3) == 15
        assert SimpleMath.multiply(10, 8) == 80
        assert SimpleMath.multiply(10, 10) == 100
        assert SimpleMath.multiply(10, -10) == -100
        assert SimpleMath.multiply(-10, 10) == -100
        assert SimpleMath.multiply(-10, -10) == 100
        assert SimpleMath.multiply(20, 10) == 200
    end
end