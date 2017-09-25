% Erlang - 20

-module(bug_fix).
-export([multiply/2]).

-spec multiply(integer(), integer()) -> integer().
multiply(A, B) -> A * B.