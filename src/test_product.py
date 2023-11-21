from product import ProductState


def test_product_state_has_initial_value():
    # given
    state = ProductState(initial_value=1)

    # when / then
    assert state.value == 1

def test_product_state_adds_to_value():
    # given
    state = ProductState(initial_value=1)

    # when
    state.add(2)
    state.add(3)

    # then
    assert state.value == 6

def test_product_state_subtracts_to_value():
    # given
    state = ProductState(initial_value=5)

    # when
    state.subtract(2)
    state.subtract(2)

    # then
    assert state.value == 1