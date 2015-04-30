The `dynamic_composite` module provides a `DynamicComposite` class that
delegates attribute access to a set of subordinate objects. Each
subordinate object is given an opportunity to get or set a given
attribute, until one succeeds. The order in which those subordinates are
asked to handle an attribute access is the same as the order the
subordinates were provided to the `DynamicComposite` constructor.

